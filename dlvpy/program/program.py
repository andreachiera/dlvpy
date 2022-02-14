import json
import os.path
from abc import ABC
from dlvpy.utilities.utility import Utils
from dlvpy.program.options import Options

from dlvpy.entity_schema.entity_schema_component import EntitySchemaComponent, SchemaComponentVisitor, EntityComponentVisitor

import subprocess

class Program(ABC):
    def __init__(self):
        self.__id_entity_schema_components = 0
        self._entity_schema_components = {}
        self.__id_logic_rules = 0
        self._logic_rules = {}
        self._schemas_from_logic_rules = {}
        self.__id_results = 0
        self._last_result = None
        self._results = {}

    def add_input(self, value) -> int:
        """
        Add Input for future execution
        :param value: Input for future execution
        :return: positive int identifier if input is valid, -1 otherwise
        """
        # Mapping degll'input, se è una lista o una tupla contiene i dati e il config e bisogna verificare se bisogna mapparlo in un dizionario
        # Se è un dizionario il valore lo lasciamo in questo modo, se stringa ci aspettiamo un json da convertire in dizionario
        # Alla fine della conversione ci sarà o una lista di 1 o 2 elementi, oppure un dizionario
        cValue = None
        if Utils.isTuple(value):
            cValue = (
                self.__map_json_to_dict(value[0]) if Utils.isStr(value[0]) else value[0],
                self.__map_json_to_dict(value[1]) if Utils.isStr(value[1]) else value[1]
            )
        elif Utils.isStr(value):
            cValue = self.__map_json_to_dict(value)
        else:
            cValue = value

        #A partire dai dati e dalla possibile configurazione generiamo l'alberatura delle entità e da questa ne estraiamo lo schema, se l'operazione non va a buon fine stampiamo gli errori!
        entity_schema_component, errors = EntitySchemaComponent.build(cValue)
        if errors is not None or entity_schema_component is None:
            if entity_schema_component is None:
                errors.extend(["[-] Invalid Input!"])
            Utils.print(errors)
            return -1

        self.__id_entity_schema_components += 1
        self._entity_schema_components[self.__id_entity_schema_components] = entity_schema_component
        return self.__id_entity_schema_components

    def remove_input(self, identifier: int) -> bool:
        """
        Remove Input from identifier
        :param identifier: identifier of Input to remove
        :return: True if Input with identifier is removed, False otherwise
        """
        if identifier not in self._entity_schema_components:
            return False
        del self._entity_schema_components[identifier]
        return True

    def add_inputs(self, values: list) -> list[int]:
        """
        Add Inputs for future execution :param values: Inputs for future execution
        :return: list with identifiers of Inputw where list[i] is positive int if values[i] is
        added correctly or -1 if add of values[i] failed, None if values isn't a list
        """
        if not values or not Utils.isList(values):
            return None
        return [self.add_input(value) for value in values]


    def remove_inputs(self, identifiers: list[int]) -> list[bool]:
        """
        Remove Inputs from identifiers :param identifiers: identifier of Inputs to remove :return:
        list where list[i] is True if Input with identifier in position i is removed, False otherwise. None
        if identifiers isn't a list
        """
        if not identifiers or not Utils.isList(identifiers):
            return None
        return [self.remove_input(identifier) for identifier in identifiers]

    def remove_all_inputs(self):
        self.__id_entity_schema_components = 0
        self._entity_schema_components = {}

    def add_logic_rules(self, logic_rules: str) -> int:
        """
        Add Logic Rules for future execution.
        example of Logic Rules:
            3COL:
                node(X) :- arc(X,_).
                node(Y) :- arc(_,Y).
                % schema(node(key(autoincrement), "name"))
                color(X,red) v color(X,green) v color(X,blue) :- node(X).
                badGraph :- arc(X,Y), color(X,Z), color(Y,Z).
                p :- badGraph, not p.
                not badGraph?
                % schema(color(key, "color"))

        :param logic_rules: Logic Rules for future execution
        :return: positive int identifier of Logic Rules
        """
        schemas = Utils.parseInputRules(logic_rules)
        valid_schemas = []
        if schemas is not None:
            for schema in schemas:
                if not Utils.isValidSchema(schema):
                    continue
                valid_schemas.append(schema)
        self.__id_logic_rules += 1
        self._logic_rules[self.__id_logic_rules] = logic_rules
        self._schemas_from_logic_rules[self.__id_logic_rules] = valid_schemas
        return self.__id_logic_rules

    def add_logic_rules_from_file(self, path: str) -> int:
        if os.path.exists(path):
            logic_rules = ""
            try:
                f = open(path, "r")
                logic_rules = f.read()
                f.close()
            except Exception:
                return -1
            return self.add_logic_rules(logic_rules)
        return -1

    def remove_logic_rules(self, identifier: int) -> bool:
        """
        Remove Logic Rules from identifier
        :param identifier: identifier of Logic Rules to remove
        :return: True if Logic Rules with identifier is removed, False otherwise
        """
        if identifier not in self._logic_rules:
            return False

        del self._logic_rules[identifier]
        del self._schemas_from_logic_rules[identifier]
        return True

    def remove_all_logic_rules(self):
        self.__id_logic_rules = 0
        self._logic_rules = {}
        self._schemas_from_logic_rules = {}

    def get_last_result(self, jsonOutput: bool = True):
        return Program.__map_dict_to_json(self._last_result) if jsonOutput else self._last_result

    def get_result(self, identifier: int, jsonOutput = True):
        if identifier not in self._results:
            return None
        return Program.__map_dict_to_json(self._results[identifier]) if jsonOutput else self._results[identifier]

    def get_all_results(self, jsonOutput: bool = True):
        results = []
        for identifier in self._results:
            results.append(self.get_result(identifier, jsonOutput))
        return results

    @staticmethod
    def __map_json_to_dict(value):
        try:
            if os.path.exists(value):
                f = open(value, "r")
                fContent = f.read()
                f.close()
                return json.loads(fContent)
            return json.loads(value)
        except Exception:
            pass
        return None

    @staticmethod
    def __map_dict_to_json(dict):
        try:
            return json.dumps(dict, indent=2)
        except Exception:
            pass
        return None

    def remove_result(self, identifier: int) -> bool:
        if identifier not in self._results:
            return False

        relative_result = self._results[identifier]
        if relative_result == self._last_result:
            self._last_result = None
        del self._results[identifier]
        return True

    def remove_results(self, identifiers: list) -> list[bool]:
        if not identifiers or not Utils.isList(identifiers):
            return None

        return [self.remove_result(idx) for idx in identifiers]

    def remove_all_results(self):
        self.__id_results = 0
        self._last_result = None
        self._results = {}

    def execute(self, param: str or Options) -> (int or None, str or None):
        """
        Execute Program
        :return: identifier of result if exists, None otherwise
        """
        try:
            options = Options(param) if Utils.isStr(param) else param
            if not isinstance(options, Options):
                return None, ["[-] Parameter must be a str path or an dlvpy.options.Options instance!"]

            if not os.path.exists(options.path):
                return None, ["[-] Invalid path!"]

            # Costruzione della lista dei parametri da passare all'eseguibile dlv
            parameters = [options.path] + options.get_options()

            # Lista dei file conteneti EDB (insieme dei fatti ottenuti input o da eventuali logiche aggiunte) e IDB (regole logiche aggiunte)
            input_files = []

            for identifier in self._entity_schema_components:
                input_files.append(Utils.write_temp_file(self.read_facts_of(identifier)))

            for id_rule in self._logic_rules:
                input_files.append(Utils.write_temp_file(self._logic_rules[id_rule]))

            parameters.extend(input_files)

            proc = subprocess.Popen(
                parameters,
                universal_newlines=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE,
            )

            # Esecuzione del processo sulla macchina con ottenimento dei risultati
            output, error = proc.communicate()

            for filename in input_files:
                Utils.remove_file(filename)

            if error is not None and error.strip() != "":
                errors = []
                if "syntax error" in error:
                    errors.append("[-] Syntax error! Check all input rules that you have added!")
                elif "Rule is not safe" in error:
                    errors.append("[-] Rule not safe! Check all input rules that you have added!")
                else:
                    errors.append(error)
                return None, errors

            # Fase di lexing e parsing dei risultati
            answer_sets, error = Utils.parseOutput(output)

            if error is not None:
                return None, [error]

            # Insieme degli schemi aggiunti al programma
            schemas_lists = list(map(lambda item: item[1], filter(lambda item: not item[1] is None, self._schemas_from_logic_rules.items())))
            schemas = []
            for schema_list in schemas_lists:
                schemas.extend(schema_list)

            # Aggiornamento dei risultati in funzione degli schemi aggiunti
            Utils.updateFinalResult(schemas, answer_sets)

            self.__id_results += 1
            self._last_result = answer_sets
            self._results[self.__id_results] = answer_sets
            return self.__id_results, None

        except RuntimeError as e:
            return None, [e]
        return None, None

    def read_schemas_of(self, identifier: int) -> str or None:
        """
        Build schema definition of Input with this identifier, if identifier is unknown return None
        :param identifier: id of Input added
        :return: string definition or None
        """
        if identifier not in self._entity_schema_components:
            return None
        visitor = SchemaComponentVisitor()
        try:
            result = self._entity_schema_components[identifier].accept(visitor)
        except RuntimeError as e:
            return None
        return result

    def read_facts_of(self, identifier: int) -> str or None:
        """
        Build facts of Input with this identifier, if identifier is unknown return None
        :param identifier: id of Input added
        :return: string definition or None
        """
        if identifier not in self._entity_schema_components:
            return None
        visitor = EntityComponentVisitor()
        try:
            result = self._entity_schema_components[identifier].accept(visitor)
        except RuntimeError as e:
            return None
        return result


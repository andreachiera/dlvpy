import re, tempfile, os
from enum import Enum

from antlr4 import InputStream, CommonTokenStream

from dlvpy.parsers.dlv.input.DLVLexerInput import DLVLexerInput
from dlvpy.parsers.dlv.input.DLVParserInput import DLVParserInput
from dlvpy.parsers.dlv.input.DLVParserInputVisitorImpl import DLVParserInputVisitorImpl
from dlvpy.parsers.dlv.output.DLVLexerOutput import DLVLexerOutput
from dlvpy.parsers.dlv.output.DLVParserOutput import DLVParserOutput
from dlvpy.parsers.dlv.output.DLVParserOutputVisitorImpl import DLVParserOutputVisitorImpl


class PythonDataType:
    NONETYPE = 'NoneType'
    STR = 'str'
    INT = 'int'
    FLOAT = 'float'
    COMPLEX = 'complex'
    LIST = 'list'
    TUPLE = 'tuple'
    RANGE = 'range'
    DICT = 'dict'
    SET = 'set'
    FROZENSET = 'frozenset'
    BOOL = 'bool'
    BYTES = 'bytes'
    BYTEARRAY = 'bytearray'
    MEMORYVIEW = 'memoryview'


SIMPLES = [
    PythonDataType.NONETYPE,
    PythonDataType.STR,
    PythonDataType.INT,
    PythonDataType.FLOAT,
    PythonDataType.COMPLEX,
    PythonDataType.BOOL
]

COMPLEX = [
    PythonDataType.DICT,
    PythonDataType.LIST,
]


class Type(Enum):
    SIMPLE = 0
    COMPLEX = 1


class Utils:
    # Serie di utility che verificano il tipo di un dato
    @staticmethod
    def isDict(value) -> bool:
        return isinstance(value, dict)

    @staticmethod
    def isList(value) -> bool:
        return isinstance(value, list)

    @staticmethod
    def isStr(value) -> bool:
        return isinstance(value, str)

    @staticmethod
    def isNone(value) -> bool:
        return value is None

    @staticmethod
    def isTuple(value) -> bool:
        return isinstance(value, tuple)

    @staticmethod
    def isSimple(value) -> bool:
        """
        Verifica se il dato è un tipo semplice o una lista di tipi semplici
        """
        return type(value).__name__ in SIMPLES or Utils.isListOfSimples(value)

    @staticmethod
    def isComplex(value) -> bool:
        """
        Verifica se il dato è un tipo complesso
        """
        return not Utils.isSimple(value) and type(value).__name__ in COMPLEX

    @staticmethod
    def isListOfSimples(value: list) -> bool:
        if not Utils.isList(value):
            return False

        for e in value:
            if not Utils.isSimple(e):
                return False
        return True

    @staticmethod
    def isListOfComplex(value: list) -> bool:
        if not Utils.isList(value):
            return False

        for e in value:
            if not Utils.isComplex(e):
                return False
        return True

    @staticmethod
    def removeKeyFromDict(value: dict, key: str) -> dict:
        """
        Rimuove una coppia chiave valore da un dizionario
        """
        if not Utils.isDict(value) or not Utils.isStr(key):
            Utils.raiseBadStructure()
        del value[key]
        return value

    # Alcuni metodi di utilità per lanciare eccezioni interne alla libreria
    @staticmethod
    def raiseNoNodeTypeException():
        raise Exception('Unknown Type exception!')

    @staticmethod
    def raiseBadStructure():
        raise Exception('Bad Structure!')

    @staticmethod
    def raiseBadConfigType(type: any):
        raise Exception('Type ' + type + ' isn\'t a valid type!')

    @staticmethod
    def raiseException(msg):
        raise Exception(str(msg))

    @staticmethod
    def print(msgs: list):
        print("\n".join(msgs))

    @staticmethod
    def valueType(value: any):
        """
        Return a Type mapping of a python data type or raise an Exception if it isn't a supported Type
        """
        if Utils.isSimple(value):
            return Type.SIMPLE
        if Utils.isComplex(value):
            return Type.COMPLEX
        Utils.raiseNoNodeTypeException()

    @staticmethod
    def valueOf(value: any):
        """
        Return same value if it is a SIMPLE, None if it is a COMPLEX, raise an Exception otherwise
        """
        _valueType = type(value).__name__
        if _valueType in SIMPLES or Utils.isListOfSimples(value):
            return value
        if _valueType in COMPLEX:
            return None
        Utils.raiseNoNodeTypeException()

    @staticmethod
    def get_properties_type(value: dict) -> dict:
        if not Utils.isDict(value):
            Utils.raiseBadStructure()
        return dict(map(lambda kv: (kv[0], Utils.valueType(kv[1])), value.items()))

    @staticmethod
    def checkAndGet(dictionary: dict, path: list, default: any) -> any:
        if not dictionary:
            return default
        lastDict = dictionary
        for key in path:
            if key in lastDict:
                lastDict = lastDict[key]
                continue
            return default
        if not lastDict:
            return default
        return lastDict

    @staticmethod
    def parseInputRules(rules) -> dict or None:
        if rules is None or (isinstance(rules, str) and len(rules.strip()) == 0):
            return None
        try:
            current_rules = rules.strip() + '\n'
            i_stream = InputStream(current_rules)
            lexer_input = DLVLexerInput(i_stream)
            tokens = CommonTokenStream(lexer_input)
            parser = DLVParserInput(tokens)
            visitor = DLVParserInputVisitorImpl()
            return visitor.visitCodeinput(parser.codeinput())
        except RuntimeError as e:
            Utils.print([str(e)])
        return None

    @staticmethod
    def isValidSchema(schema):
        is_valid_schema: bool = True
        errors = []
        if "ancestors_path" not in schema or schema["ancestors_path"] is None or len(schema["ancestors_path"]) == 0:
            if not Utils.checkIsValidName(schema["name"]):
                errors.append("[-] Root schema name \"" + schema["name"] + "\" isn't valid! It must match this pattern: " + Utils.NAME_PATTERN + "!")
                is_valid_schema = False
        else:
            if not Utils.checkIsValidFollowingProperty(schema["name"]):
                errors.append("[-] Schema name \"" + schema["name"] + "\" isn't valid! It must match this pattern: " + Utils.FOLLOWING_PROPERTY_PATTERN + "!")
                is_valid_schema = False
        if schema["key"] is not None:
            if "autoincrement" not in schema["key"] and "properties" not in schema["key"]:
                errors.append("[-] Invalid key definition! Key must container autoincrement or properties key!")
                is_valid_schema = False
            if "autoincrement" in schema["key"] and schema["key"]["autoincrement"]==False:
                errors.append("[-] Error on autoincrement!")
                is_valid_schema = False
        if len(errors) > 0:
            Utils.print(errors)
        return is_valid_schema


    @staticmethod
    def getOnlyValidSchemas(schemas):
        """
        Filtro degli schemi validi, ovvero o che sono root, oppure i cui ancestors_path sono validi e completamente attraversati
        """
        if schemas is None or len(schemas) == 0:
            return []
        schemas.sort(
            key=lambda schema: 0 if "ancestors_path" not in schema or schema["ancestors_path"] is None else len(
                schema["ancestors_path"]))
        schemas_tree = {}

        valid_schemas = []
        for schema in schemas:
            ancestors_path = [] if "ancestors_path" not in schema or schema["ancestors_path"] is None else schema["ancestors_path"]
            walked_all_path: bool = True
            current_schemas_tree = schemas_tree
            for ancestor in ancestors_path:
                if ancestor not in current_schemas_tree:
                    walked_all_path = False
                    break
                current_schemas_tree = current_schemas_tree[ancestor]
            if not walked_all_path:
                continue
            current_schemas_tree[schema["name"]] = {}
            valid_schemas.append(schema)
        return valid_schemas

    @staticmethod
    def getFinalResultFromSchemasAndModel(schemas, model: list):
        result = {
            "schema_results": [],
            "other_results": []
        }
        # mapping dentro schemas_dict del nome schema e relativa configurazione
        schemas_dict = dict(map(lambda inner_schema: (inner_schema["name"], inner_schema), schemas))
        # potenziali letterali da inserire dentro un alberatura risultante
        schema_literals = []

        # Sfoltimento dei letterali che non hanno un matching con uno schema e tipo/numero di proprietà dello schema
        for literal in model:
            name = literal["atom"]["name"]
            # Se il letterale non ha un atomo con nome predicato pari ad uno schema lo scartiamo dall'alberatura
            if name not in schemas_dict:
                result["other_results"].append(literal)
                continue

            schema = schemas_dict[name]

            terms = literal["atom"]["terms"]
            # Valuto il numero di ancestor nello schema relativo le cui key devono stare nei termini
            number_of_ancestors_keys = (
                0 if "ancestors_path" not in schema or schema["ancestors_path"] is None else len(
                    schema["ancestors_path"]))
            # Valuto il numero di proprietà che bisogna trovare, in questo caso numero di termini
            number_of_properties = (
                0 if "properties" not in schema or schema["properties"] is None else len(schema["properties"]))
            # Verifico che ci siano sufficienti termini per coprire l'esigenza dello schema
            # Se la key non è None, è calcolata dalla libreria come funzione di altri valori, altrimenti deve esserci il termine per la key
            if len(terms) != number_of_ancestors_keys + (0 if schema["key"] is not None else 1) + number_of_properties:
                result["other_results"].append(literal)
                continue

            # Verifico che le chiavi degli ancestor siano tutte stringhe
            cont: bool = False
            for i in range(number_of_ancestors_keys):
                if not isinstance(terms[i], str):
                    cont = True
                    break
            if cont:
                result["other_results"].append(literal)
                continue

            key = schema["key"]
            #Set la key è None, il termine corrispondente deve essere una stringa
            #if key is None and not isinstance(terms[number_of_ancestors_keys], str):
            #    result["other_results"].append(literal)
            #    continue


            if key is not None and "autoincrement" in key:
                if not key["autoincrement"]:
                    result["other_results"].append(literal)
                    continue
            #       cont = True
            #elif key is not None and "properties" in key:
            #    for prop in key["properties"]:
            #        idx = schema["properties"].index(prop)
            #        if isinstance(terms[idx], list):
            #            cont = True
            #            break

            #if cont:
            #    result["other_results"].append(literal)
            #    continue

            schema_literals.append(literal)

        # Creazione dell'alberatura ed esclusione letterali non facenti parte dell'alberatura che vanno in other_results
        schemas_result_without_config = {}

        schemas_name = list(map(lambda inner_schema: inner_schema["name"], schemas))
        literals_ordered = sorted(schema_literals,
                                  key=lambda inner_literal: schemas_name.index(inner_literal["atom"]["name"]))
        # Contiene informazione sugli schemi trovati che sono autoincrementali e il valore dell'ultima key inserita dentro lo schema
        schemas_autoincrement = {}
        # Per ogni letterale verifico l'inserimento nell'alberatura di uscita
        for literal in literals_ordered:
            name = literal["atom"]["name"]
            terms = literal["atom"]["terms"]
            schema = schemas_dict[name]
            # Prendo i valori delle chiavi ancestor per trovare la posizione nell'alberatura
            ancestor_keys = []
            if "ancestors_path" in schema and schema["ancestors_path"] is not None and len(schema["ancestors_path"]) > 0:
                ancestor_keys = terms[0:len(schema["ancestors_path"])]

            current_entity_component = schemas_result_without_config

            # Verifico che il cammino per arrivare alla entity corrente esista
            founded_all_match: bool = True
            for idx, ancestor_key in enumerate(schema["ancestors_path"]):
                if str(ancestor_key) not in current_entity_component or terms[idx] not in current_entity_component[str(ancestor_key)]:
                    founded_all_match = False
                    break
                current_entity_component = current_entity_component[str(ancestor_key)][str(ancestor_keys[idx])]

            # Se il cammino non esiste non salvo il literal nell'alberatura
            if not founded_all_match:
                result["other_results"].append(literal)
                continue

            # Se la proprietà in questione non c'è nella posizione di interimento, la aggiungo sottoforma di dizionario EntitiesContainer
            if schema["name"] not in current_entity_component:
                current_entity_component[schema["name"]] = {}

            number_of_ancestors_keys = 0 if "ancestors_path" not in schema or schema["ancestors_path"] is None else len(schema["ancestors_path"])

            # Prendo il valore della chiave, se None è in una determinata posizione, se dizionario e valore autoincremet costruisco un valore di chiave, altrimenti mi leggo le proprietà per la costruzione
            key = ""
            key_autoincrement = False
            if schema["key"] is None:
                key = str(terms[number_of_ancestors_keys])
            elif "autoincrement" in schema["key"]:
                key_autoincrement = True
            else:
                properties_index = [schema["properties"].index(prop) for prop in schema["key"]["properties"]]
                key_concat = "__" if "concat" not in schema["key"] or schema["key"]["concat"] is None else schema["key"]["concat"]
                key = key_concat.join(
                    [str(terms[number_of_ancestors_keys + prop_idx]) for prop_idx in properties_index])

            # Se esiste già un oggetto nella gerarchia in funzione delle chiavi inserite, il literal corrent viene scartato
            if key is not None and key in current_entity_component[schema["name"]]:
                result["other_results"].append(literal)
                continue

            sub_entity_component = {}
            # Se il letterale è negato secondo TRUE_NEGATION salvo questa informazione
            if "DLVPY_TRUE_NEGATION" in literal:
                sub_entity_component["DLVPY_TRUE_NEGATION"] = literal["DLVPY_TRUE_NEGATION"]

            for idx, prop in enumerate(schema["properties"]):
                value = terms[idx + number_of_ancestors_keys + (0 if schema["key"] is not None else 1)]
                sub_entity_component[prop] = value

            if key_autoincrement:
                inner_key = None if len(ancestor_keys) == 0 else "__".join(ancestor_keys)
                if schema["name"] not in schemas_autoincrement:
                    schemas_autoincrement[schema["name"]] = {
                        "__DLVPY__ROOT__": 0
                    }
                if inner_key is not None and inner_key not in schemas_autoincrement[schema["name"]]:
                    schemas_autoincrement[schema["name"]][inner_key] = 0

                key_int = 0
                if inner_key is not None:
                    schemas_autoincrement[schema["name"]][inner_key] += 1
                    key_int = schemas_autoincrement[schema["name"]][inner_key]
                else:
                    schemas_autoincrement[schema["name"]]["__DLVPY__ROOT__"] += 1
                    key_int = schemas_autoincrement[schema["name"]]["__DLVPY__ROOT__"]

                key = str(key_int)

            current_entity_component[schema["name"]][key] = sub_entity_component

        for schema_name in schemas_result_without_config:
            result["schema_results"].append([schemas_result_without_config[schema_name], {"schema": schema_name}])

        return result

    @staticmethod
    def updateFinalResult(schemas: list, answer_sets):
        if answer_sets is None:
            return None
        if len(answer_sets) == 0:
            return []

        # Filtering degli schemi validi
        schemas = Utils.getOnlyValidSchemas(schemas)

        # Mapping a seconda della tipologia di risultato dei relativi possibili modelli
        for answer_set in answer_sets:
            if "model" in answer_set:
                answer_set["model"] = Utils.getFinalResultFromSchemasAndModel(schemas, answer_set["model"])
            elif "query" in answer_set and "witness" in answer_set["query"]:
                answer_set["query"]["witness"] = Utils.getFinalResultFromSchemasAndModel(schemas, answer_set["query"]["witness"])
            elif "model_with_cost" in answer_set and "model" in answer_set["model_with_cost"]:
                answer_set["model_with_cost"]["model"] = Utils.getFinalResultFromSchemasAndModel(schemas, answer_set["model_with_cost"]["model"])

    NAME_PATTERN = "^[a-z][a-zA-Z0-9_]*$"
    __NAME_PATTERN_INSTANCE = re.compile(NAME_PATTERN)
    @staticmethod
    def checkIsValidName(value: str):
        """
        Verifica se il valore passato è un NAME DLV valido, ovvero inizia per una lettere minuscale e procede con lettere minuscole/maiuscole/numeri/underscore
        """
        if not isinstance(value, str):
            return False
        return Utils.__NAME_PATTERN_INSTANCE.match(value) is not None

    FOLLOWING_PROPERTY_PATTERN = "^[a-zA-Z0-9_]+$"
    __FOLLOWING_PROPERTY_PATTERN_INSTANCE = re.compile(FOLLOWING_PROPERTY_PATTERN)

    @staticmethod
    def checkIsValidFollowingProperty(value: str):
        """
        Analoga definizione al metodo @checkIsValidName a meno del controllo sulla lettera iniziale
        """
        if not isinstance(value, str):
            return False
        return Utils.__FOLLOWING_PROPERTY_PATTERN_INSTANCE.match(value) is not None

    @classmethod
    def parseOutput(cls, output: str):
        """
        Lecing e Parsing dell'output restituito da DLV
        """
        if output is None:
            return None, None
        try:
            current_output = output.strip() + '\n'
            i_stream = InputStream(current_output)
            lexer_input = DLVLexerOutput(i_stream) #Costruzione dei Token secondo i token definiti in DLVLexerOutput
            tokens = CommonTokenStream(lexer_input)
            parser = DLVParserOutput(tokens) #Costruzione albero di parsing a partire dai Token e dalle regole definite in DLVParserOutput
            visitor = DLVParserOutputVisitorImpl()
            return visitor.visitOutput(parser.output()), None # Generazione dei risultati in un'alberatura Custom a dizionari
        except RuntimeError as e:
            return None, e
        return None, None

    # Utility FILES per scrittura e rimozione
    @staticmethod
    def write_temp_file(text) -> str:
        fd, file_name = tempfile.mkstemp(suffix='.txt', text=True)
        os.close(fd)
        text = text if text is not None else ''
        fd = open(file_name, "w")
        fd.write(text)
        fd.close()
        return file_name

    @staticmethod
    def remove_file(filename):
        os.remove(filename)

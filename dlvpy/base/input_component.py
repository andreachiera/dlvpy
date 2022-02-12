import copy
from typing import Dict, List, Any

from dlvpy.utilities.utility import Utils


class InputComponent:
    TYPES_OF_ANALYSIS = ["key", "property"]
    DEFAULT_ANALYSIS_TYPE = TYPES_OF_ANALYSIS[0]
    CONFIG_TYPE_KEY = "type"
    CONFIG_PROPERTIES_KEY = "properties"
    CONFIG_PROPERTY_KEY = "key"
    CONFIG_PROPERTY_KEY_PROPERTIES = "properties"
    CONFIG_PROPERTY_KEY_CONCAT = "concat"
    CONFIG_PROPERTY_KEY_CONCAT_DEFAULT = "__"
    CONFIG_PROPERTY_KEY_AUTOINCREMENT = "autoincrement"
    CONFIG_SCHEMA_NAME_PREFIX_KEY = "schema"

    def __init__(self):
        self._data = None
        self._config = None

    @staticmethod
    def build(value):
        if value is None:
            return None

        result = InputComponent()
        if value is not None:
            # Se è un dizionario è solo il value, altrimenti abbiamo valore e configurazione
            if Utils.isTuple(value):
                if len(value) < 1:
                    return None
                result.data = value[0]
                result.config = {} if len(value) < 2 else value[1]
            else:
                result.data = value
                result.config = {}


        result.data = copy.deepcopy(result.data)
        result.config = copy.deepcopy(result.config)

        return result

    @property
    def data(self) -> Dict or List or Any:
        return self._data

    @data.setter
    def data(self, data: Dict or List or Any):
        self._data = data

    @property
    def config(self) -> Dict or None:
        return self._config

    @config.setter
    def config(self, config: Dict or None):
        self._config = config

    def get_analysis_type(self) -> str:
        if self.config and InputComponent.CONFIG_TYPE_KEY in self.config:
            if self.config[InputComponent.CONFIG_TYPE_KEY] not in InputComponent.TYPES_OF_ANALYSIS:
                # Se il type definito nel file di config non è un type valido, lanciamo un'errore
                Utils.raiseBadConfigType(self.config[InputComponent.CONFIG_TYPE_KEY])
            return self.config[InputComponent.CONFIG_TYPE_KEY]
        # Se non troviamo il tipo, utilizziamo l'analisi di default
        return InputComponent.DEFAULT_ANALYSIS_TYPE

    def sub_config_from_property(self, prop: str) -> dict:
        if InputComponent.CONFIG_PROPERTIES_KEY in self.config and prop in self.config[InputComponent.CONFIG_PROPERTIES_KEY]:
            return self.config[InputComponent.CONFIG_PROPERTIES_KEY][prop]
        return {}

    def check_analysis_type(self):
        analysis_type = self.get_analysis_type()
        # Se il tipo di analisi è key non ci aspettiamo nulla nel file di config
        if analysis_type == InputComponent.TYPES_OF_ANALYSIS[0]:
            return
        # Se non troviamo la chiave che definisce la proprietà, errore!
        if InputComponent.CONFIG_PROPERTY_KEY not in self.config:
            Utils.raiseException("[-] No key founded in config!")
        if Utils.isDict(self.config[InputComponent.CONFIG_PROPERTY_KEY]):
            if InputComponent.CONFIG_PROPERTY_KEY_AUTOINCREMENT in self.config[InputComponent.CONFIG_PROPERTY_KEY] and not self.config[InputComponent.CONFIG_PROPERTY_KEY][InputComponent.CONFIG_PROPERTY_KEY_AUTOINCREMENT]:
                Utils.raiseException("[-] Property " + InputComponent.CONFIG_PROPERTY_KEY_AUTOINCREMENT + " of " + InputComponent.CONFIG_PROPERTY_KEY + " in config must be True!")
            if InputComponent.CONFIG_PROPERTIES_KEY in self.config[InputComponent.CONFIG_PROPERTY_KEY] and len(self.config[InputComponent.CONFIG_PROPERTY_KEY][InputComponent.CONFIG_PROPERTIES_KEY]) == 0:
                Utils.raiseException("[-] Property " + InputComponent.CONFIG_PROPERTIES_KEY + " of " + InputComponent.CONFIG_PROPERTY_KEY + " in config without elements!")

    def check_property_analysis(self, entities_list: list):
        if not Utils.isList(entities_list):
            Utils.raiseException("[-] No entities list founded!")
        if InputComponent.CONFIG_PROPERTY_KEY not in self.config:
            Utils.raiseException("[-] No key founded in config file!")
        properties = []
        exist_other_configurations: bool = False
        if Utils.isStr(self.config[InputComponent.CONFIG_PROPERTY_KEY]):
            properties.append(self.config[InputComponent.CONFIG_PROPERTY_KEY])
        elif Utils.isDict(self.config[InputComponent.CONFIG_PROPERTY_KEY]):
            if InputComponent.CONFIG_PROPERTY_KEY_PROPERTIES in self.config[InputComponent.CONFIG_PROPERTY_KEY] and Utils.isListOfSimples(self.config[InputComponent.CONFIG_PROPERTY_KEY][InputComponent.CONFIG_PROPERTY_KEY_PROPERTIES]):
                properties = self.config[InputComponent.CONFIG_PROPERTY_KEY][InputComponent.CONFIG_PROPERTY_KEY_PROPERTIES]
            if InputComponent.CONFIG_PROPERTY_KEY_AUTOINCREMENT in self.config[InputComponent.CONFIG_PROPERTY_KEY] and self.config[InputComponent.CONFIG_PROPERTY_KEY][InputComponent.CONFIG_PROPERTY_KEY_AUTOINCREMENT] == True:
                exist_other_configurations = True

        if exist_other_configurations:
            return
        if len(properties) == 0:
            Utils.raiseException("[-] Invalid key definition in config file!")
        for entity in entities_list:
            if not Utils.isDict(entity):
                Utils.raiseException("[-] Entity " + str(entity) + " isn\'t a dictionary! ")
            for prop in properties:
                if (prop not in entity) or not Utils.isSimple(entity[prop]) or Utils.isListOfSimples(prop):
                    Utils.raiseException("[-] Invalid or not exist " + str(prop) + " in entity! ")


    def get_property_key(self):
        return self.config[InputComponent.CONFIG_PROPERTY_KEY]

    def get_schema_prefix(self):
        return Utils.checkAndGet(self.config, InputComponent.CONFIG_SCHEMA_NAME_PREFIX_KEY, None)

    @staticmethod
    def get_sub_config_from_property(config: any, property: str) -> dict:
        if config and InputComponent.CONFIG_PROPERTIES_KEY in config and property in config[InputComponent.CONFIG_PROPERTIES_KEY]:
            return config[InputComponent.CONFIG_PROPERTIES_KEY][property]
        return {}


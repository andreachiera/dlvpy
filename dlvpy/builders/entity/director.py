from abc import ABC
from dlvpy.base.input_component import InputComponent
from dlvpy.builders.entity.builder import EntityBuilder
from dlvpy.entity_schema.entity.entity_component import EntityComponent, EntitiesContainer, EntityValue, EntityContainer
import copy

from dlvpy.utilities.utility import Utils, Type


class Director(ABC):
    def __init__(self) -> None:
        self._entity_builder: EntityBuilder = None

    @property
    def entity_builder(self) -> EntityBuilder:
        return self._entity_builder

    @entity_builder.setter
    def entity_builder(self, entity_builder: EntityBuilder) -> None:
        self._entity_builder = entity_builder

    def build_entity_component(self, input_component: InputComponent) -> EntityComponent:
        """
        Metodo per la costruzione dell'alberatura delle entità
        """
        inner_input_componet = InputComponent()
        inner_input_componet.data = copy.deepcopy(input_component.data)
        inner_input_componet.config = copy.deepcopy(input_component.config)
        result = self.__build_entity_component(inner_input_componet)
        # Se il risultato non è un'instanza di EntitiesContainer, non riteniamo il risultato valido
        if not isinstance(result, EntitiesContainer):
            return None
        return result

    def __build_entity_component(self, input_component: InputComponent) -> EntityComponent:
        analysis_type: str = input_component.get_analysis_type() # Estrazione della tipologia di analisi (basata su chiave o basata sulle proprietà)
        return self.__build_entity_component_with_key_analysis(input_component) if analysis_type == InputComponent.TYPES_OF_ANALYSIS[0] else self.__build_entity_component_with_property_analysis(input_component)

    def __build_entity_component_with_key_analysis(self, input_component: InputComponent) -> EntityComponent:
        # Controlli di consistenza rispetto al tipo di analisi
        input_component.check_analysis_type()

        # Se il dato è un tipo semplice fermiamo l'analisi
        if Utils.isSimple(input_component.data):
            self.entity_builder.build_entity_value(None, input_component.data)
            return self.entity_builder.product

        self._entity_builder.build_entities_container(None, input_component.data, input_component.config)
        entities_container = self._entity_builder.product

        # Collezioniamo tutte le entità dentro un dizionario, la struttura dl json in ingresso può essere un singolo dizionario, oppure una lista con tanti dizionari
        dict_all_entities = {}
        if Utils.isDict(input_component.data):
            dict_all_entities.update(input_component.data)
        elif Utils.isList(input_component.data):
            for entities in input_component.data:
                dict_all_entities.update(entities)

        # Lista dove per ogni entità, abbiamo il valore della chiave, le proprietà con il relativo tipo (Semplice o Complesso) e l'entità grezza
        list_all_entities_with_key_properties_type_and_value = [(entity_key, Utils.get_properties_type(dict_all_entities[entity_key]), dict_all_entities[entity_key]) for entity_key in dict_all_entities]

        # Per ogni entità construisco in entity_container
        for entity_key_properties_type_and_value in list_all_entities_with_key_properties_type_and_value:
            self._entity_builder.build_entity_container(None, entity_key_properties_type_and_value[0])
            entity_container = self._entity_builder.product

            # Data ogni proprietà estendiamo l'alberatura
            for _property in entity_key_properties_type_and_value[1]:
                # Se un tipo semplice ci fermiamo
                if entity_key_properties_type_and_value[1][_property] == Type.SIMPLE:
                    self._entity_builder.build_entity_value(_property, entity_key_properties_type_and_value[2][_property])
                    entity_value = self._entity_builder.product
                    self._entity_builder.set_product(entity_container)
                    self._entity_builder.add_entity_component(entity_value)
                    continue

                # Costruiamo la sottoalberatura
                sub_input_component = InputComponent.build(
                    (entity_key_properties_type_and_value[2][_property], input_component.sub_config_from_property(_property))
                )

                # Avviamo la costruzione del sottoalbero
                sub_entities_container = self.__build_entity_component(sub_input_component)
                sub_entities_container.key = _property

                # Aggiunta del sotto albero nella gerarchia
                self._entity_builder.set_product(entity_container)
                self._entity_builder.add_entity_component(sub_entities_container)

            self._entity_builder.set_product(entities_container)
            self._entity_builder.add_entity_component(entity_container)

        return entities_container

    def __build_entity_component_with_property_analysis(self, input_component: InputComponent) -> EntityComponent:
        # Controlli di consistenza rispetto al tipo di analisi
        input_component.check_analysis_type()

        entities_list = [input_component.data] if Utils.isDict(input_component.data) else input_component.data if Utils.isList(input_component.data) else []

        # Ulteriori controlli di consistenza
        input_component.check_property_analysis(entities_list)

        self._entity_builder.build_entities_container(None, input_component.data, input_component.config)
        entities_container = self._entity_builder.product

        # Prendiamo la key, che può essere None, una stringa, oppure un oggetto con la definizione necessaria alla costruzione
        property_key: any = input_component.get_property_key()
        # Valore grezzo della proprietà usata come chiave oppure None
        property_key_key = property_key if isinstance(property_key, str) else None

        # Tupla con la key (in questo caso non valore la il nome della proprietà o la definizione per la costruzione), le proprietà con il relativo tipo (Semplice o Complesso) e l'entità grezza
        list_all_entities_with_key_properties_type_and_value = [(property_key, Utils.get_properties_type(entity), entity) for entity in entities_list]

        # Per ogni entità construisco in entity_container
        for idx, entity_key_properties_type_and_value in enumerate(list_all_entities_with_key_properties_type_and_value):
            # Valore della key dell'entità, presa o dalle proprietà oppure costruita dalla libreria, se autoincrement oppure definizione di proprietà da utilizzare
            if property_key_key is not None:
                property_key_value = entity_key_properties_type_and_value[2][property_key]
            else:
                if InputComponent.CONFIG_PROPERTY_KEY_AUTOINCREMENT in property_key and property_key[InputComponent.CONFIG_PROPERTY_KEY_AUTOINCREMENT] == True:
                    property_key_value = str(idx + 1)
                else:
                    property_key_value = ((InputComponent.CONFIG_PROPERTY_KEY_CONCAT_DEFAULT if InputComponent.CONFIG_PROPERTY_KEY_CONCAT not in property_key else property_key["concat"]).join([str(entity_key_properties_type_and_value[2][prop]) for prop in property_key[InputComponent.CONFIG_PROPERTY_KEY_PROPERTIES]]))
            self._entity_builder.build_entity_container(property_key_key, property_key_value)
            entity_container = self._entity_builder.product

            # Data ogni proprietà estendiamo l'alberatura
            for _property in entity_key_properties_type_and_value[1]:
                # Se la proprietà in questione è stata utilizzata come chiave la saltiamo
                if _property == property_key:
                    continue

                # Se un tipo semplice ci fermiamo
                if entity_key_properties_type_and_value[1][_property] == Type.SIMPLE:
                    self._entity_builder.build_entity_value(_property, entity_key_properties_type_and_value[2][_property])
                    entity_value = self._entity_builder.product
                    self._entity_builder.set_product(entity_container)
                    self._entity_builder.add_entity_component(entity_value)
                    continue

                # Costruiamo la sottoalberatura
                sub_input_component = InputComponent.build(
                    (entity_key_properties_type_and_value[2][_property], input_component.sub_config_from_property(_property))
                )

                # Aggiunta del sotto albero nella gerarchia
                sub_entities_container = self.__build_entity_component(sub_input_component)
                sub_entities_container.key = _property

                # Aggiunta del sotto albero nella gerarchia
                self._entity_builder.set_product(entity_container)
                self._entity_builder.add_entity_component(sub_entities_container)

            self._entity_builder.set_product(entities_container)
            self._entity_builder.add_entity_component(entity_container)

        return entities_container
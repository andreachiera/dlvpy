from __future__ import annotations
from abc import ABC, abstractmethod

from dlvpy.base.input_component import InputComponent
from dlvpy.entity_schema.schema.schema_component import SchemaComponent
from dlvpy.utilities.utility import Utils


class EntityComponent(ABC):

    def __init__(self):
        self._key = None
        self._value = None
        self._config = None
        self._parent = None

    @property
    def key(self) -> any:
        return self._key

    @key.setter
    def key(self, key: any):
        self._key = key

    @property
    def value(self) -> any:
        return self._value

    @value.setter
    def value(self, value: any):
        self._value = value

    @property
    def config(self) -> any:
        return self._config

    @config.setter
    def config(self, value: any):
        self._config = value

    @property
    def parent(self) -> EntityComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: EntityComponent):
        self._parent = parent

    def add(self, component: EntityComponent) -> None:
        pass

    def remove(self, component: EntityComponent) -> None:
        pass

    def getChildren(self) -> None:
        pass

    @abstractmethod
    def is_composite(self) -> bool:
        pass

    @abstractmethod
    def accept(self, visitor: EntityComponentVisitor) -> SchemaComponent:
        pass

    def __str__(self) -> str:
        result = "\"key\": {}, \"value\": {}".format(self._key, self._value)
        if self.getChildren() and Utils.isList(self.getChildren()) and len(self.getChildren()) > 0:
            result += ", childrens: [{}]".format(",".join([str(child) for child in self.getChildren()]))
        return "{" + result + "}"


class EntitiesContainer(EntityComponent):
    def __init__(self) -> None:
        self._entities: list[EntityComponent] = []

    def add(self, component: EntityComponent) -> None:
        self._entities.append(component)
        component.parent = self

    def remove(self, component: EntityComponent) -> None:
        self._entities.remove(component)
        component.parent = None

    def getChildren(self) -> list[EntityComponent]:
        return self._entities

    def is_composite(self) -> bool:
        return True

    def accept(self, visitor: EntityComponentVisitor) -> SchemaComponent:
        return visitor.visit_entities_container(self)


class EntityContainer(EntityComponent):
    def __init__(self) -> None:
        self._true_negation: bool = False
        self._properties: list[EntityComponent] = []

    @property
    def true_negation(self) -> bool:
        return self._true_negation

    @true_negation.setter
    def true_negation(self, true_negation: bool):
        self._true_negation = true_negation

    def add(self, component: EntityComponent) -> None:
        if component.key == "DLVPY_TRUE_NEGATION":
            self._true_negation = component.value
            return
        self._properties.append(component)
        component.parent = self

    def remove(self, component: EntityComponent) -> None:
        self._properties.remove(component)
        component.parent = None

    def getChildren(self) -> list[EntityComponent]:
        return self._properties

    def is_composite(self) -> bool:
        return True

    def accept(self, visitor: EntityComponentVisitor) -> SchemaComponent:
        visitor.visit_entity_container(self)


class EntityValue(EntityComponent):
    def is_composite(self) -> bool:
        return False

    def accept(self, visitor: EntityComponentVisitor) -> SchemaComponent:
        visitor.visit_entity_value(self)


class EntityComponentVisitor(ABC):
    @abstractmethod
    def visit_entities_container(self, entities_container: EntitiesContainer) -> None:
        pass

    @abstractmethod
    def visit_entity_container(self, entity_container: EntityContainer) -> None:
        pass

    @abstractmethod
    def visit_entity_value(self, entity_value: EntityValue) -> None:
        pass


class EntityComponentSchemaVisitor(EntityComponentVisitor):
    """
    EntityComponent Visitor used to obtain SchemaComponent
    """
    def visit_entities_container(self, entities_container: EntitiesContainer) -> SchemaComponent:
        return self.__visit_entities(entities_container.getChildren(), entities_container.config)

    def visit_entity_container(self, entity_container: EntityContainer) -> SchemaComponent:
        pass

    def visit_entity_value(self, entity_value: EntityValue) -> SchemaComponent:
        pass

    def __visit_entities(self, entities: list[EntityContainer], config: any) -> SchemaComponent:
        # Se non ci sono entities da analizzare, non abbiamo uno schema
        if not Utils.isList(entities) or len(entities) == 0:
            return None

        # Andiamo a cercare tutte le possibili proprietà presenti nelle entità
        all_properties_founded: list = []
        # Prendiamo come nome dello schema la chiave del primo EntityContainer, garantendo successivamente la presenza della stessa key in tutte le entità
        schema_key = entities[0].key
        for entity in entities:
            for entity_component in entity.getChildren():
                if entity_component.key in all_properties_founded:
                    continue
                all_properties_founded.append(entity_component.key)
            if entity.key != schema_key:
                Utils.raiseBadStructure()

        # Partiamo con la creazione dello schema, dentro cui salviamo il nome dello schema dentro la chiave e il file di configurazione corrente
        schema = SchemaComponent()
        schema.key = schema_key
        schema.config = config

        for _property in all_properties_founded:
            # Per ogni proprietà rieseguo la stessa analisi
            next_level_to_visit: list[EntityComponent] = []
            for entity in entities:
                next_level_to_visit.extend(list(filter(lambda _entity_component: _entity_component.key == _property, entity.getChildren())))

            # Se nel prossimo livello da analizzare sono tutte EntityValue vuol dire che devo fermami perché in realtà la proprietà in questione appartire a questo schema
            all_children_are_entity_value = True if len(list(filter(lambda _entity_component: not isinstance(_entity_component, EntityValue), next_level_to_visit))) == 0 else False
            if all_children_are_entity_value:
                schema.add_property(_property)
                continue

            # Altrimenti è necessario continuare verificando che tutti i componenti siano dei contenitori di entità
            all_children_are_entities_container = True if len(list(filter(lambda _entity_component: not isinstance(_entity_component, EntitiesContainer), next_level_to_visit))) == 0 else False
            if all_children_are_entities_container:
                sub_schema_component = self.__visit_entities([entity_component for entities_component in next_level_to_visit for entity_component in entities_component.getChildren()], InputComponent.get_sub_config_from_property(config, _property))
                sub_schema_component.schema_name = _property
                schema.add_sub_schema_component(sub_schema_component)
                continue

            # In questo caso c'è un errore in quando esiste incongruenza tra le proprietà degli entityContainer analizzati, devono essere o tutti valori semplici oppure valori complessi analizzabili, non sono accettati mix di entità
            Utils.raiseBadStructure()

        return schema




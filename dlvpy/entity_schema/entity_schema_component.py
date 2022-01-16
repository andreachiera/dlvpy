from abc import ABC, abstractmethod

from dlvpy.base.input_component import InputComponent
from dlvpy.builders.entity.builder import ConcreteEntityBuilder1
from dlvpy.builders.entity.director import Director
from dlvpy.entity_schema.entity.entity_component import EntityComponentSchemaVisitor, EntityComponent, EntityValue, \
    EntitiesContainer, EntityContainer
from dlvpy.entity_schema.schema.schema_component import SchemaComponent
from dlvpy.utilities.mapper import DLVMapper
from dlvpy.utilities.utility import Utils


class EntitySchemaComponentVisitor:
    pass


class EntitySchemaComponent(ABC):
    def __init__(self):
        self._input_component: InputComponent = None
        self._entity_component: EntityComponent = None
        self._schema_component: SchemaComponent = None

    @property
    def input_component(self) -> InputComponent:
        return self._input_component

    @input_component.setter
    def input_component(self, input_component: InputComponent):
        self._input_component = input_component

    @property
    def entity_component(self) -> EntityComponent:
        return self._entity_component

    @entity_component.setter
    def entity_component(self, entity_component: EntityComponent):
        self._entity_component = entity_component

    @property
    def schema_component(self) -> SchemaComponent:
        return self._schema_component

    @schema_component.setter
    def schema_component(self, schema_component: SchemaComponent):
        self._schema_component = schema_component

    def __reset(self):
        self._input_component = None
        self._entity_component = None
        self._schema_component = None

    @staticmethod
    def build(value):
        # Inizializziamo il risultato
        entity_schema_component = EntitySchemaComponent()
        try:
            # Mappiamo dati e configurazione in una classe interna InputComponent
            entity_schema_component.input_component = InputComponent.build(value)
            if entity_schema_component.input_component is None:
                return None, ["[-] Value is not valid!"]

            # Mappati gli input costruiamo l'alberatura delle entità
            director = Director()
            builder = ConcreteEntityBuilder1()
            director.entity_builder = builder
            director.build_entity_component(entity_schema_component.input_component)
            entity_schema_component.entity_component = builder.product

            # Se l'alberatura non è valida ritorniamo
            if entity_schema_component is None:
                return None, []

            # Verifica se l'alberatura è consistente
            is_entity_component_valid, errors = EntitySchemaComponent.isEntityComponentValid(entity_schema_component.entity_component)
            if not is_entity_component_valid:
                return None, errors

            # Estrapoliamo l'alberatura dello schema a partire dall'alberatura delle entità
            visitor = EntityComponentSchemaVisitor()
            entity_schema_component.schema_component = entity_schema_component.entity_component.accept(visitor)
        except Exception as e:
            return None, [str(e)]

        return entity_schema_component, None

    @staticmethod
    def isEntityComponentValid(entity_component):
        errors = []
        if not isinstance(entity_component, EntitiesContainer):
            return False, ["[-] First Entity Component must be an EntitiesContainer!"]

        if entity_component.config is not None and "schema" in entity_component.config:
            if not Utils.checkIsValidName(entity_component.config["schema"]):
                errors.append("[-] Property schema of config isn't valid! It must match this pattern: " + Utils.NAME_PATTERN + "!")

        not_visited = [entity_component]
        while len(not_visited) != 0:
            entity_component = not_visited.pop(0)
            if isinstance(entity_component, EntitiesContainer):
                if entity_component.key is not None and not Utils.checkIsValidFollowingProperty(entity_component.key):
                    errors.append("[-] Property " + entity_component.key + " isn't valid! It must match this pattern: " + Utils.FOLLOWING_PROPERTY_PATTERN + "!")
            childrens = entity_component.getChildren()
            if childrens is None:
                continue
            not_visited.extend(childrens)

        if len(errors) == 0:
            return True, None
        return False, errors


    def accept(self, visitor: EntitySchemaComponentVisitor) -> any:
        return visitor.visit(self)


class EntitySchemaComponentVisitor(ABC):
    @abstractmethod
    def visit(self, entity_schema_component: EntitySchemaComponent) -> any:
        pass


class SchemaComponentVisitor(ABC):
    def visit(self, entity_schema_component: EntitySchemaComponent) -> str:
        return self.__visit(entity_schema_component.schema_component)

    def __visit(self, schema_component: SchemaComponent) -> str:
        schema_prefix = schema_component.eval_complete_schema_name()
        keys = schema_component.eval_complete_keys()
        properties = schema_component.properties
        keys_properties = keys + DLVMapper.mapValuesToDLVFormat(properties)
        results: list[str] = ["schema(" + schema_prefix + "(" + ",".join(keys_properties) + "))"]

        for sub_schema_component in schema_component.sub_schema_components:
            results.append(self.__visit(sub_schema_component))

        return "\n".join(results)


class EntityComponentVisitor(ABC):
    def visit(self, entity_schema_component: EntitySchemaComponent) -> str:
        return self.__visit(entity_schema_component.schema_component, entity_schema_component.entity_component)

    def __visit(self, schema_component: SchemaComponent, entities_container: EntitiesContainer) -> str:
        schema_prefix = schema_component.eval_complete_schema_name()

        node_component = entities_container
        super_keys: list[str] = []
        while node_component is not None:
            if isinstance(node_component, EntityContainer):
                super_keys.insert(0, node_component.value)
            node_component = node_component.parent

        facts = []
        entity_container: EntityComponent
        for entity_container in entities_container.getChildren():
            true_negation = entity_container.true_negation if hasattr(entity_container, "true_negation") else False
            property_key_value = dict((e.key, e.value) for e in list(filter(lambda e: isinstance(e, EntityValue), entity_container.getChildren())))
            properties_value = [property_key_value[prop] if prop in property_key_value else None for prop in schema_component.properties]
            facts.append(("" if not true_negation else "-") + schema_prefix + "(" + ",".join(DLVMapper.mapValuesToDLVFormat(super_keys + [entity_container.value] + properties_value)) + ").")

        for entity_container in entities_container.getChildren():
            sub_entities_containers = list(filter(lambda e: isinstance(e, EntitiesContainer), entity_container.getChildren()))
            for sub_entities_container in sub_entities_containers:
                sub_schema_component = list(filter(lambda inner_sub_schema_component: inner_sub_schema_component.schema_name == sub_entities_container.key, schema_component.sub_schema_components))[0]
                facts.append(self.__visit(sub_schema_component, sub_entities_container))

        return "\n".join(facts)

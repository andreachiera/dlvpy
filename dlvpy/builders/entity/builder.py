from __future__ import annotations

from abc import ABC, abstractmethod
from dlvpy.entity_schema.entity.entity_component import EntityComponent, EntitiesContainer, EntityContainer, EntityValue


class EntityBuilder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_product(self) -> any or None:
        pass

    @abstractmethod
    def add_entity_component(self, entity_component: EntityComponent) -> bool:
        pass

    @abstractmethod
    def build_entities_container(self, key: str, value: any, config: any) -> None:
        pass

    @abstractmethod
    def build_entity_container(self, key: str, value: any) -> None:
        pass

    @abstractmethod
    def build_entity_value(self, key: str, value: any) -> None:
        pass


class ConcreteEntityBuilder1(EntityBuilder):

    def __init__(self) -> None:
        self._product = None

    def reset(self):
        self._product = None

    @property
    def product(self) -> EntityComponent:
        product = self._product
        self.reset()
        return product

    def set_product(self, product) -> any or None:
        result_product = self.product
        self.reset()
        self._product = product
        return result_product

    def add_entity_component(self, entity_component: EntityComponent) -> bool:
        if isinstance(self._product, EntityValue):
            return False
        if isinstance(self._product, EntitiesContainer) and isinstance(entity_component, EntitiesContainer):
            return False
        if isinstance(self._product, EntityContainer) and isinstance(entity_component, EntityContainer):
            return False
        self._product.add(entity_component)

    def build_entities_container(self, key: str, value: any, config: any) -> None:
        entities_container = EntitiesContainer()
        entities_container.key = key
        entities_container.value = value
        entities_container.config = config
        entities_container.parent = None
        self._product = entities_container

    def build_entity_container(self, key: str, value: any) -> None:
        entity_container = EntityContainer()
        entity_container.key = key
        entity_container.value = value
        entity_container.parent = None
        self._product = entity_container

    def build_entity_value(self, key: str, value: any) -> None:
        entity_value = EntityValue()
        entity_value.key = key
        entity_value.value = value
        entity_value.parent = None
        self._product = entity_value

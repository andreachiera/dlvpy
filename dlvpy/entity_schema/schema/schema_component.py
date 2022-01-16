from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from dlvpy.base.input_component import InputComponent
from dlvpy.utilities.utility import Utils


class SchemaComponent(ABC):
    DEFAULT_SCHEMA_NAME_PREFIX = "schema"
    DEFAULT_KEY = "key"
    DEFAULT_ANCESTOR_KEY = "ancestor_key"

    def __init__(self):
        self._schema_name: str = None
        self._config: any = None
        self._key: str = None
        self._properties: list[str] = []
        self._sub_schema_components: list[SchemaComponent] = []
        self._parent: SchemaComponent = None

    @property
    def schema_name(self) -> str:
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name: str):
        self._schema_name = schema_name

    @property
    def config(self) -> str:
        return self._config

    @config.setter
    def config(self, config: str):
        self._config = config

    @property
    def key(self) -> str:
        return self._key

    @key.setter
    def key(self, key: str):
        self._key = key

    @property
    def properties(self) -> list[str]:
        return self._properties

    @properties.setter
    def properties(self, properties: list[str]):
        self._properties = properties

    @property
    def sub_schema_components(self) -> list[SchemaComponent]:
        return self._sub_schema_components

    @sub_schema_components.setter
    def sub_schema_components(self, sub_schema_components: list[SchemaComponent]):
        self._sub_schema_components = sub_schema_components

    @property
    def parent(self) -> SchemaComponent:
        return self._parent

    @parent.setter
    def parent(self, parent: SchemaComponent):
        self._parent = parent

    def add_property(self, value: str) -> bool:
        if property in self._properties:
            return False
        self._properties.append(value)
        return True

    def remove_property(self, value: str) -> bool:
        len_properties = len(self._properties)
        self._properties.remove(value)
        return False if len(self._properties) == len_properties else True

    def add_sub_schema_component(self, sub_schema_component: SchemaComponent) -> bool:
        if sub_schema_component.schema_name in list(
                map(lambda sub_schema: sub_schema.schema_name, self._sub_schema_components)):
            return False
        self._sub_schema_components.append(sub_schema_component)
        sub_schema_component.parent = self
        return True

    def remove_sub_schema_component(self, sub_schema_component: SchemaComponent) -> bool:
        len_sub_schema_components = len(self._sub_schema_components)
        self._sub_schema_components = list(
            filter(lambda sub_schema: sub_schema.value != sub_schema_component.schema_name,
                   self._sub_schema_components))
        return False if len(self._sub_schema_components) == len_sub_schema_components else True

    def is_end_schema(self) -> bool:
        return len(self._sub_schema_components) == 0

    def eval_complete_schema_name(self) -> str:
        if self.schema_name is None or self.parent is None:
            schema_prefix: str or None = Utils.checkAndGet(self.config, [InputComponent.CONFIG_SCHEMA_NAME_PREFIX_KEY], None)
            if schema_prefix is None:
                schema_prefix = SchemaComponent.DEFAULT_SCHEMA_NAME_PREFIX
            return schema_prefix
        return "__".join([self.parent.eval_complete_schema_name(), self.schema_name])

    def __eval_complete_keys(self) -> list[str]:
        if self.parent is None:
            return [SchemaComponent.DEFAULT_ANCESTOR_KEY + "(" + self.eval_complete_schema_name() + ")"]
        return self.parent.__eval_complete_keys() + [SchemaComponent.DEFAULT_ANCESTOR_KEY + "(" + self.eval_complete_schema_name() + ")"]

    def eval_complete_keys(self) -> list[str]:
        if self.parent is None:
            return [SchemaComponent.DEFAULT_KEY]
        return self.parent.__eval_complete_keys() + [SchemaComponent.DEFAULT_KEY]

    @staticmethod
    def isSchemaValid(schema_component):
        if schema_component is None:
            return True, None

        return None, None

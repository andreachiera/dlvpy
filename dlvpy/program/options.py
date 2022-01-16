import copy
import os.path
from abc import ABC


class Options(ABC):
    def __init__(self, path: str = None):
        self.__id_options = 0
        self._path = os.path.abspath(path)
        self.options: dict = {}

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def add_option(self, option: str) -> int or None:
        if not isinstance(option, str):
            return None
        self.__id_options += 1
        self.options[self.__id_options] = option
        return self.__id_options

    def remove_option(self, identifier: int) -> bool:
        if not isinstance(identifier, int) or identifier not in self.options:
            return False
        del self.options[identifier]
        return True

    def add_options(self, options: list[str]) -> list[int or None]:
        identifiers: list[int or None] = []
        for option in options:
            identifiers.append(self.add_option(option))
        return identifiers

    def remove_options(self, identifiers: list[int]) -> list[bool]:
        removed: list[bool] = []
        for identifier in identifiers:
            removed.append(self.remove_option(identifier))
        return removed

    def get_options(self):
        return copy.deepcopy([option[1] for option in self.options.items()])
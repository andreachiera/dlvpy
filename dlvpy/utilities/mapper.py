from abc import ABC
import math


class DLVMapper(ABC):
    @staticmethod
    def mapValueToDLVFormat(value: any) -> str:
        if value is None:
            return "none"
        if isinstance(value, str):
            result = "\"" + DLVMapper.replaceAllBadCharacters(value) + "\""
            return result
        if isinstance(value, int) and value < 0:
            return "negative_integer(" + str(-1 * value) + ")"
        if isinstance(value, float):
            return ("negative_" if value<0 else "") + "float(" + str(value if value >= 0 else -1*value).replace(".", ",") + ")"
        if isinstance(value, complex):
            return "complex(" + DLVMapper.mapValueToDLVFormat(value.real) + "," + DLVMapper.mapValueToDLVFormat(value.imag) + ")"
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, list):
            return "[" + ",".join(DLVMapper.mapValuesToDLVFormat(value)) + "]"
        return str(value)

    @staticmethod
    def replaceAllBadCharacters(value: str):
        return DLVMapper.replacer(value, 0)

    BAD_CHARACTERS = ["\""]
    BAD_CHARACTERS_CODE = ["__DLVPY__34__"]
    @staticmethod
    def replacer(value: str, bad_char_position: int) -> str:
        if bad_char_position >= len(DLVMapper.BAD_CHARACTERS):
            return value
        return DLVMapper.replacer(value.replace(DLVMapper.BAD_CHARACTERS[bad_char_position], DLVMapper.BAD_CHARACTERS_CODE[bad_char_position]), bad_char_position+1)

    @staticmethod
    def charKey(char):
        return "__DLVPY__" + str(ord(char)) + "__"

    @staticmethod
    def mapValuesToDLVFormat(values: list[any]) -> list[str]:
        if values is None:
            return []
        return [DLVMapper.mapValueToDLVFormat(value) for value in values]

    @staticmethod
    def invReplacer(value: str, bad_char_position: int) -> str:
        if bad_char_position >= len(DLVMapper.BAD_CHARACTERS):
            return value
        return DLVMapper.invReplacer(value.replace(DLVMapper.BAD_CHARACTERS_CODE[bad_char_position], DLVMapper.BAD_CHARACTERS[bad_char_position]), bad_char_position + 1)

    @staticmethod
    def invReplaceAllBadCharacters(value: str):
        return DLVMapper.invReplacer(value, 0)

    @staticmethod
    def mapValueFromDLVFormat(value: any) -> any:
        if value is None:
            return None
        if value == "true":
            return True
        if value == "false":
            return False
        if isinstance(value, list):
            return DLVMapper.mapValuesFromDLVFormat(value)
        if isinstance(value, int) or isinstance(value, float):
            return value
        if isinstance(value, str):
            return DLVMapper.invReplaceAllBadCharacters(value)
        print("[-] No mapped value: " + value + "!")
        return None

    @staticmethod
    def mapValuesFromDLVFormat(values: list[any]) -> list[str]:
        if values is None:
            return []
        return [DLVMapper.mapValueToDLVFormat(value) for value in values]


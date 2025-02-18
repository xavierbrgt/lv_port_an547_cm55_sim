from PikaObj import *

class MemChecker:
    def max(self): ...
    def now(self): ...

    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def getMax(self) -> float: ...

    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def getNow(self) -> float: ...

    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def resetMax(self): ...


class SysObj:
    @staticmethod
    def type(arg: any) -> any: ...

    @staticmethod
    def int(arg: any) -> int: ...

    @staticmethod
    def float(arg: any) -> float: ...

    @staticmethod
    def str(arg: any) -> str: ...

    @staticmethod
    def iter(arg: any) -> any: ...

    @staticmethod
    def range(a1: int, a2: int) -> any: ...

    @staticmethod
    def print(*val): ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def printNoEnd(val: any): ...

    @staticmethod
    def __setitem__(obj: any, key: any, val: any) -> any: ...

    @staticmethod
    def __getitem__(obj: any, key: any) -> any: ...

    @staticmethod
    @PIKA_C_MACRO_IF("PIKA_BUILTIN_STRUCT_ENABLE")
    def __slice__(obj: any, start: any, end: any, step: int) -> any: ...

    @staticmethod
    def len(arg: any) -> int: ...

    @staticmethod
    @PIKA_C_MACRO_IF("PIKA_BUILTIN_STRUCT_ENABLE")
    def list() -> any: ...

    @staticmethod
    @PIKA_C_MACRO_IF("PIKA_BUILTIN_STRUCT_ENABLE")
    def dict() -> any: ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def hex(val: int) -> str: ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def ord(val: str) -> int: ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def chr(val: int) -> str: ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def bytes(val: any) -> bytes: ...

    @staticmethod
    @PIKA_C_MACRO_IF("PIKA_SYNTAX_FORMAT_ENABLE")
    def cformat(fmt: str, *var) -> str: ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def id(obj: any) -> int: ...

    @staticmethod
    @PIKA_C_MACRO_IF("PIKA_FILEIO_ENABLE")
    def open(path: str, mode: str) -> object: ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def dir(obj: object) -> list: ...

    @staticmethod
    @PIKA_C_MACRO_IF("PIKA_EXEC_ENABLE")
    def exec(code: str): ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def getattr(obj: object, name: str) -> any: ...

    @staticmethod
    @PIKA_C_MACRO_IF("!PIKA_NANO_ENABLE")
    def setattr(obj: object, name: str, val: any): ...


@PIKA_C_MACRO_IF("0")
class RangeObj:
    def __next__(self) -> any: ...


@PIKA_C_MACRO_IF("0")
class StringObj:
    def __next__(self) -> any: ...


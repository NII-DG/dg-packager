from enum import Enum
from dg_packager.error.error import EnumValueError


class SchemaType(Enum):
    BASE = "base"
    CAO = "cao"
    METI = "meti"
    AMED = "amed"
    GINFORK = "ginfork"

    @classmethod
    def value_of(cls, target_value):
        for e in SchemaType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in SchemaType Class.'.format(target_value))

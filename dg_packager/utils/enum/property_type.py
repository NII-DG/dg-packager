from enum import Enum
from dg_packager.error.error import EnumValueError


class PropertyType(Enum):
    ID = "@id"
    NAME = "name"
    EMAIL = "email"
    TELEPHONE = "telephone"
    CONTEXT = "@context"
    GRAPH = "@graph"
    TYPE = "@type"

    @classmethod
    def value_of(cls, target_value):
        for e in PropertyType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in PropertyType Class.'.format(target_value))

from enum import Enum
from dg_packager.error.error import EnumValueError

class IsAccessibleForFreeType(Enum):

    TRUE = 'True'
    FLASE = 'False'
    UNKNOWN = ''


    @classmethod
    def value_of(cls, target_value):
        for e in IsAccessibleForFreeType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in IsAccessibleForFreeType Class.'.format(target_value))
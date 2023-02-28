from enum import Enum
from dg_packager.error.error import EnumValueError

class ConfigType(Enum):
    GLOBAL = '--global'
    SYSTEM ='--system'
    LOCAL ='--local'

    @classmethod
    def value_of(cls, target_value):
        for e in ConfigType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in ConfigType Class.'.format(target_value))
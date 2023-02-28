from enum import Enum
from dg_packager.error.error import EnumValueError

class WayOfManageType(Enum):
    '''
    公開種別
    '''
    COMMISSIONED = "commissioned"
    SELF_MANAGED = "self-managed"
    EMPTY = ""


    @classmethod
    def value_of(cls, target_value):
        for e in WayOfManageType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in WayOfManageType Class.'.format(target_value))
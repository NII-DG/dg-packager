from enum import Enum
from dg_packager.error.error import EnumValueError

class ContentSizeType(Enum):
    '''
    ContentSizeType
    '''
    ONE_GB = "1GB"
    TEN_GB = "10GB"
    ONE_HUNDRED_GB = "100GB"
    OVER_ONE_HUNDRED_GB = "over100GB"
    EMPTY = ""


    @classmethod
    def value_of(cls, target_value):
        for e in ContentSizeType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in ContentSizeType Class.'.format(target_value))
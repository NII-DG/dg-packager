from enum import Enum
from dg_packager.error.error import EnumValueError

class GotInformedConsentType(Enum):

    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"
    EMPTY = ''


    @classmethod
    def value_of(cls, target_value):
        for e in GotInformedConsentType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in GotInformedConsentType Class.'.format(target_value))
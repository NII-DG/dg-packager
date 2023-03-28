from enum import Enum
from dg_packager.error.error import EnumValueError

class InformedConsentFormatType(Enum):

    AMED = "AMED"
    OTHER = "other"
    UNKNOWN = ""


    @classmethod
    def value_of(cls, target_value):
        for e in InformedConsentFormatType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in InformedConsentFormatType Class.'.format(target_value))
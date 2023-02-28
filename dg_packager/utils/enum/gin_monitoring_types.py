from enum import Enum
from dg_packager.error.error import EnumValueError


class DatasetStructureType(Enum):
    WITH_CODE = "with_code"
    FOR_PARAMETER = "for_parameter"
    UNKNOWN = ""

    @classmethod
    def value_of(cls, target_value):
        for e in DatasetStructureType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in DatasetStructureType Class.'.format(target_value))


class ContentSizeType(Enum):
    ONE_GB = "1GB"
    TEN_GB = "10GB"
    ONE_HUNDRED_GB = "100GB"
    ONE_TB = "1TB"
    TEN_PB = "1PB"
    UNKNOWN = ""

    @classmethod
    def value_of(cls, target_value):
        for e in ContentSizeType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in ContentSizeType Class.'.format(target_value))


class WorkflowIdentifierType(Enum):
    BASIC = "basic"
    BIO = "bio"
    NUERO = "nuero"
    UNKNOWN = ""

    @classmethod
    def value_of(cls, target_value):
        for e in WorkflowIdentifierType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in WorkflowIdentifierType Class.'.format(target_value))

from enum import Enum
from dg_packager.error.error import EnumValueError

class AccessRightsType(Enum):
    '''
    公開種別
    '''

    '''
    CAO and METI type
    '''
    OPEN_ACCESS = "open access"
    RESTRICED_ACCESS = "restricted access"
    EMBARGOED_ACCESS = "embargoed access"
    METADATA_ONLY_ACCESS = "metadata only access"

    '''
    Only AMED type
    '''
    UNSHARED = "Unshared"
    RESTRICTED_CLOSED_SHARING = "Restricted Closed Sharing"
    RESTRICTED_OPEN_SHARING = "Restricted Open Sharing"
    UNRESTRICTED_OPEN_SHARING = "Unrestricted Open Sharing"

    @classmethod
    def value_of(cls, target_value):
        for e in AccessRightsType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in AccessRightsType Class.'.format(target_value))

class CaoAndMetiAccessRightsType(Enum):
    '''
    公開種別
    '''

    '''
    CAO and METI type
    '''
    OPEN_ACCESS = "open access"
    RESTRICED_ACCESS = "restricted access"
    EMBARGOED_ACCESS = "embargoed access"
    METADATA_ONLY_ACCESS = "metadata only access"

    @classmethod
    def value_of(cls, target_value):
        for e in CaoAndMetiAccessRightsType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in CaoAndMetiAccessRightsType Class.'.format(target_value))

class AmedAccessRightsType(Enum):
    '''
    公開種別
    '''

    '''
    Only AMED type
    '''
    UNSHARED = "Unshared"
    RESTRICTED_CLOSED_SHARING = "Restricted Closed Sharing"
    RESTRICTED_OPEN_SHARING = "Restricted Open Sharing"
    UNRESTRICTED_OPEN_SHARING = "Unrestricted Open Sharing"

    @classmethod
    def value_of(cls, target_value):
        for e in AmedAccessRightsType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in AmedAccessRightsType Class.'.format(target_value))
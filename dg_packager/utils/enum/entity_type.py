from enum import Enum
from dg_packager.error.error import EnumValueError


class EntityType(Enum):
    DATASET = "Dataset"
    CREATIVE_WORK = "CreativeWork"
    FILE = "File"
    ORGANIZATION = "Organization"
    REPOSITORY_OBJECT = "RepositoryObject"
    PERSON = "Person"
    GIN_MONITORING = "GinMonitoring"
    DATA_DOWNLOAD = "DataDownload"
    HOSTING_INSTITUTION = "HostingInstitution"
    LICENSE = "License"
    DMP = "DMP"
    DMP_METADATA = "DMPMetadata"
    CONTACT_POINT = "ContactPoint"
    CLINICAL_RESEARCH_REGISTRATION = "ClinicalResearchRegistration"



    @classmethod
    def value_of(cls, target_value):
        for e in EntityType:
            if e.value == target_value:
                return e
        raise EnumValueError('{} is not defined in EntityType Class.'.format(target_value))
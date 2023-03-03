
from typing import Any
from dg_packager.error.error import EntityParameterError
from dg_packager.utils.enum.property_type import PropertyType
from dg_packager.utils.enum.access_rights_type import AccessRightsType
from dg_packager.utils.enum.got_Informed_consent_type import GotInformedConsentType
from dg_packager.utils.enum.imformed_consent_formata_type import InformedConsentFormatType
from dg_packager.utils.enum.is_accessible_for_free import IsAccessibleForFreeType

from nii_dg.entity import ContextualEntity
from nii_dg.schema.base import RepositoryObject, DataDownload, License, HostingInstitution, Organization, ContactPoint
from nii_dg.schema.cao import DMP as Cao_DMP
from nii_dg.schema.meti import DMP as Meti_DMP
from nii_dg.schema.amed import DMP as Amed_DMP, ClinicalResearchRegistration
from nii_dg.entity import Entity

class DMPEntity:
    '''
    DMPEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_amed(self,
                    common_props: dict[str, Any],
                    keyword: str,
                    gotInformedConsent: GotInformedConsentType,
                    identifier: list[ClinicalResearchRegistration],
                    informedConsentFormat: InformedConsentFormatType,
                    reasonForConcealment: str
                     ) -> Amed_DMP:
        '''
        amed の DMP インスタンスの生成メソッド
        '''
        props = common_props

        if keyword:
             props["keyword"] = keyword

        if GotInformedConsentType is not GotInformedConsentType.EMPTY:
            props["gotInformedConsent"] = gotInformedConsent.value

        if informedConsentFormat is not informedConsentFormat.UNKNOWN:
            props["informedConsentFormat"] = informedConsentFormat.value

        if len(identifier) > 0:
            identifier_list = list()
            for crr in identifier:
                crr_id = crr.data.get(PropertyType.ID.value)
                if crr_id:
                    identifier_list.append(crr)
                else:
                    raise EntityParameterError('Identifier Property of DMP Have Been Set Person that have no ID(Empty Value).')
            props["identifier"] = identifier_list

        if reasonForConcealment:
            props["reasonForConcealment"] = reasonForConcealment


        return Amed_DMP(id_=common_props['dataNumber'], props=props)

    def generate_meti(self,
                    common_props: dict[str, Any],
                    hostingInstitution: HostingInstitution,
                    wayOfManage: str,
                    creator: list[Organization],
                    isAccessibleForFree:IsAccessibleForFreeType,
                    license: License,
                    usageInfo: str,
                    reasonForConcealment: str,
                    measurementTechnique: str,
                    contactPoint: ContactPoint,
                     ) -> Meti_DMP:
        '''
        meti の DMP インスタンスの生成メソッド
        '''
        props = common_props

        hostingInstitution_id = hostingInstitution.data.get(PropertyType.ID.value)
        if hostingInstitution_id:
            props["hostingInstitution"] = hostingInstitution

        if wayOfManage:
            props["wayOfManage"] = wayOfManage

        if len(creator) > 0:
            creator_list = list()
            for p in creator:
                person_id = p.data.get(PropertyType.ID.value)
                if person_id:
                    creator_list.append(p)
                else:
                    raise EntityParameterError('Creator Property of DMP Have Been Set Person that have no ID(Empty Value).')
            props["creator"] = creator_list

        '''
        isAccessibleForFree
        '''
        if isAccessibleForFree is IsAccessibleForFreeType.TRUE:
            props["isAccessibleForFree"] = True
        elif isAccessibleForFree is IsAccessibleForFreeType.FLASE:
            props["isAccessibleForFree"] = False

        license_id = license.data.get(PropertyType.ID.value)
        if license_id:
            props["license"] = license

        if usageInfo:
            props["usageInfo"] = usageInfo

        if reasonForConcealment:
            props["reasonForConcealment"] = reasonForConcealment

        if measurementTechnique:
            props["measurementTechnique"] = measurementTechnique

        contactPoint_id = contactPoint.data.get(PropertyType.ID.value)
        if contactPoint_id:
            props["contactPoint"] = contactPoint

        return Meti_DMP(id_=common_props['dataNumber'], props=props)


    def generate_cao(self,
                     common_props: dict[str, Any],
                     hostingInstitution: HostingInstitution,
                     keyword: str,
                     creator: list[Entity],
                     dataManager: Entity,
                     isAccessibleForFree:IsAccessibleForFreeType,
                     license: License,
                     usageInfo: str,

                     ) -> Cao_DMP:
        '''
        cao の DMP インスタンスの生成メソッド
        '''
        props = common_props

        '''
        creator
        '''
        if len(creator) > 0:
            creator_list = list()
            for p in creator:
                person_id = p.data.get(PropertyType.ID.value)
                if person_id:
                    creator_list.append(p)
                else:
                    raise EntityParameterError('Creator Property of DMP Have Been Set Person that have no ID(Empty Value).')
            props["creator"] = creator_list

        '''
        dataManager
        '''
        dataManager_id = dataManager.data.get(PropertyType.ID.value)
        if dataManager_id:
            props["dataManager"] = dataManager

        '''
        isAccessibleForFree
        '''
        if isAccessibleForFree is IsAccessibleForFreeType.TRUE:
            props["isAccessibleForFree"] = True
        elif isAccessibleForFree is IsAccessibleForFreeType.FLASE:
            props["isAccessibleForFree"] = False

        '''
        license
        '''
        license_id = license.data.get(PropertyType.ID.value)
        if license_id:
            props["license"] = license

        '''
        usageInfo
        '''
        if usageInfo:
            props["usageInfo"] = usageInfo

        '''
        hostingInstitution
        '''
        hostingInstitution_id = hostingInstitution.data.get(PropertyType.ID.value)
        if hostingInstitution_id:
            props["hostingInstitution"] = hostingInstitution

        '''
        keyword
        '''
        if keyword:
             props["keyword"] = keyword

        return Cao_DMP(id_=common_props['dataNumber'], props=props)


    def creata_common_props(self,
                            dataNumber: int,
                            name: str,
                            description: str,
                            accessRights:str,
                            repository: RepositoryObject,
                            distribution: DataDownload,
                            contentSize: str,
                            availabilityStarts:  str,
                            ) -> dict[str, Any]:
        '''
        DMP の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()

        if dataNumber > 0:
            props["dataNumber"] = dataNumber

        if name:
            props["name"] = name

        if description:
            props["description"] = description

        if accessRights:
            props["accessRights"] = accessRights


        repository_id = repository.data.get(PropertyType.ID.value)
        if repository_id:
            props["repository"] = repository

        distribution_id = distribution.data.get(PropertyType.ID.value)
        if distribution_id:
            props["distribution"] = distribution

        if contentSize:
            props["contentSize"] = contentSize

        if availabilityStarts:
            props["availabilityStarts"] = availabilityStarts


        return props

    @staticmethod
    def is_open_access(dmp: ContextualEntity) -> bool:
        '''
        DMP accessRights property が "open access" or "Unrestricted Open Sharing" なら真
        それ以外なら偽
        '''
        is_open_access = False
        dmp_accessRights = dmp.data.get("accessRights")
        if dmp_accessRights == AccessRightsType.OPEN_ACCESS.value \
            or dmp_accessRights == AccessRightsType.UNRESTRICTED_OPEN_SHARING.value:

            is_open_access = True
        return is_open_access

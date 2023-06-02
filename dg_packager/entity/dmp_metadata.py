from typing import Any, List
from dg_packager.error.error import EntityParameterError
from nii_dg.schema.base import RepositoryObject, DataDownload, Person, HostingInstitution, Organization
from nii_dg.schema.cao import DMPMetadata as Cao_DMPMetadata, DMP as Cao_DMP
from nii_dg.schema.amed import DMPMetadata as Amed_DMPMetadata, DMP as Amed_DMP
from nii_dg.schema.meti import DMPMetadata as Meti_DMPMetadata, DMP as Meti_DMP
from dg_packager.utils.enum.property_type import PropertyType
from nii_dg.ro_crate import RootDataEntity
from nii_dg.entity import Entity


class DMPMetadataEntity:
    '''
    DMPMetadataEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_amed(self,
                    common_props: dict[str, Any],
                    funding: str,
                    chiefResearcher: Entity,
                    hostingInstitution: HostingInstitution,
                    dataManager: Entity,
                    hasPart: list[Amed_DMP],
                    creator: list[Entity],
                    )->Amed_DMPMetadata:
        '''
        Methods for creating DMPMetadata instances in amed
        '''
        props = common_props

        '''
        funding
        '''
        if funding:
            props["funding"] = funding

        '''
        chiefResearcher
        '''
        chiefResearcher_id = chiefResearcher.data.get(PropertyType.ID.value)
        if chiefResearcher_id:
            props["chiefResearcher"] = chiefResearcher

        '''
        hostingInstitution
        '''
        hostingInstitution_id = hostingInstitution.data.get(PropertyType.ID.value)
        if hostingInstitution_id:
            props["hostingInstitution"] = hostingInstitution

        '''
        dataManager
        '''
        dataManager_id = dataManager.data.get(PropertyType.ID.value)
        if dataManager_id:
            props["dataManager"] = dataManager

        '''
        hasPart
        '''
        if len(hasPart) > 0:
            data_list = list()
            for dmp in hasPart:
                dmp_id = dmp.data.get(PropertyType.ID.value)
                if dmp_id:
                    data_list.append(dmp)
                else:
                    EntityParameterError('HasPart Property of DMPMetadata(Amed) Must Not Be Empty ID of Amed.DMP.')
            props["hasPart"] = data_list

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
                    raise EntityParameterError('Creator Property of DMPMetadata Have Been Set Person that have no ID(Empty Value).')
            props["creator"] = creator_list

        return Amed_DMPMetadata(props=props)

    def generate_cao(self,
                    common_props: dict[str, Any],
                    keyword: str,
                    hasPart: list[Cao_DMP],
                    eradProjectId: str
                    )->Cao_DMPMetadata:
        '''
        Methods for creating DMPMetadata instances in cao
        '''
        props = common_props

        '''
        keyword
        '''
        if keyword:
            props["keyword"] = keyword

        '''
        hasPart
        '''
        if len(hasPart) > 0:
            data_list = list()
            for dmp in hasPart:
                dmp_id = dmp.data.get(PropertyType.ID.value)
                if dmp_id:
                    data_list.append(dmp)
                else:
                    EntityParameterError('HasPart Property of DMPMetadata(Cao) Must Not Be Empty ID of Cao.DMP.')
            props["hasPart"] = data_list

        '''
        eradProjectId
        '''
        if eradProjectId:
            props["eradProjectId"] = eradProjectId

        return Cao_DMPMetadata(props=props)

    def generate_meti(self,
                    common_props: dict[str, Any],
                    hasPart: list[Meti_DMP],
                    creator: list[Person],
                    )->Meti_DMPMetadata:
        '''
        Methods for creating DMPMetadata instances in meti
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
                    raise EntityParameterError('Creator Property of DMPMetadata Have Been Set Person that have no ID(Empty Value).')
            props["creator"] = creator_list

        '''
        hasPart
        '''
        if len(hasPart) > 0:
            data_list = list()
            for dmp in hasPart:
                dmp_id = dmp.data.get(PropertyType.ID.value)
                if dmp_id:
                    data_list.append(dmp)
                else:
                    EntityParameterError('HasPart Property of DMPMetadata(Meti) Must Not Be Empty ID of Meti.DMP.')
            props["hasPart"] = data_list

        return Meti_DMPMetadata(props=common_props)

    def creata_common_props(self,
                            about: RootDataEntity,
                            funder: Organization,
                            repository: RepositoryObject,
                            distribution: DataDownload,
                            ) -> dict[str, Any]:
        '''
        Method to get common properties of DMPMetadata in dict type
        '''
        props = dict[str, Any]()

        '''
        about
        '''
        about_id = about.data.get(PropertyType.ID.value)
        if about_id:
            props["about"] = about

        '''
        funder
        '''
        funder_id = funder.data.get(PropertyType.ID.value)
        if funder_id:
            props["funder"] = funder

        '''
        repository
        '''
        repository_id = repository.data.get(PropertyType.ID.value)
        if repository_id:
            props["repository"] = repository

        '''
        distribution
        '''
        distribution_id = distribution.data.get(PropertyType.ID.value)
        if distribution_id :
            props["distribution"] = distribution

        return props

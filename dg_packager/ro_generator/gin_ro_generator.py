
import json
import traceback
from typing import Any
from nii_dg.ro_crate import ROCrate
from dg_packager.error.error import JsonValidationError, RoPkgError
from dg_packager.entity.file import FileEntity
from dg_packager.entity.dataset import DatasetEntity
from dg_packager.entity.gin_monitoring import GinMonitoringEntity
from dg_packager.entity.dmp import DMPEntity
from dg_packager.entity.dmp_metadata import DMPMetadataEntity
from dg_packager.entity.person import PersonEntity
from dg_packager.entity.license import LicenseEntity
from dg_packager.entity.hosting_institution import HostingInstitutionEntity
from dg_packager.entity.data_download import DataDownloadEntity
from dg_packager.entity.repository_object import RepositoryObjectEntity
from dg_packager.entity.cinical_research_registration import ClinicalResearchRegistrationEntity
from dg_packager.utils.enum.got_Informed_consent_type import GotInformedConsentType
from dg_packager.utils.enum.imformed_consent_formata_type import InformedConsentFormatType
from dg_packager.utils.enum.is_accessible_for_free import IsAccessibleForFreeType
from dg_packager.utils.enum.schema_type import SchemaType
from dg_packager.entity.organization import OrganizationEntity
from dg_packager.entity.contact_point import ContactPointEntity
from nii_dg.schema.base import Organization, License, DataDownload, RepositoryObject, HostingInstitution, ContactPoint, Person as base_Person
from nii_dg.schema.cao import Person as cao_person, DMP as cao_DMP
from nii_dg.schema.meti import DMP as meti_DMP
from nii_dg.schema.amed import DMP as amed_DMP, ClinicalResearchRegistration
from nii_dg.entity import Entity
from nii_dg.error import CheckPropsError

from dg_packager.utils.ro_crate_util import RoCrateUtil


class GinRoGenerator():
    '''
    RoGenerator class for gin-fork
    '''

    def __init__(self, raw_metadata : dict[str, Any]):
        '''
        constructor

        Param
        -------------------------
        matadata : this param is mass of gin's metadata
        '''
        self.raw_metadata = raw_metadata

    @staticmethod
    def Generate(raw_metadata : dict[str, Any])->dict[str, Any]:
        ro_gnt = GinRoGenerator(raw_metadata)

        try:
            return ro_gnt.generate()
        except CheckPropsError as cpe :
            t = traceback.format_exception_only(type(cpe), cpe)
            raw_error_msg = t[0]
            forward_index = raw_error_msg.find("{")
            backward_index = raw_error_msg.rfind("}")
            shaped = raw_error_msg[forward_index:backward_index+1].replace('\'', '\"')
            data = json.loads(f'{{"results":[{shaped}]}}')
            raise RoPkgError(data)

    def generate(self) -> dict[str, Any]:
        '''
        RO-Crate生成メソッド
        '''
        self.check_key()

        raw_metadata = self.raw_metadata

        # ==========================================================
        # research_project data to RO-Crate(RootDataEntity)
        # ==========================================================
        research_project = raw_metadata["research_project"]

        ro_crate = ROCrate()
        ro_crate.root["name"] = research_project["name"]
        if len(research_project["description"]) > 0 :
            ro_crate.root["description"] = research_project["description"]

        # ==========================================================
        # funder_orgs data to RO-Crate(Organization)
        # ==========================================================
        org_gnt = OrganizationEntity()
        fund_dict = dict[str, Organization]()
        funder_list = list()
        for funder in raw_metadata["funder_orgs"]:
            funder_type = funder['type']
            common_props = org_gnt.creata_common_props(name=funder["name"], alias=funder["alias"], description=funder["description"])
            org_ent = org_gnt.generate_base(id=funder['@id'],common_props=common_props)
            ro_crate.add(org_ent)
            fund_dict[funder_type] = org_ent
            funder_list.append(org_ent)

        if len(funder_list)>0:
            ro_crate.root["funder"] = funder_list

        # ==========================================================
        # research_orgs data to RO-Crate(Organization)
        # ==========================================================
        research_org_dict = dict[str, Organization]()
        for research_org in raw_metadata["research_orgs"]:
            common_props = org_gnt.creata_common_props(name=research_org["name"], alias=research_org["alias"], description=research_org["description"])
            org_ent = org_gnt.generate_base(id=research_org['@id'],common_props=common_props)
            ro_crate.add(org_ent)
            research_org_dict[research_org['@id']] = org_ent

        # ==========================================================
        # licenses data to RO-Crate(License)
        # ==========================================================
        license_gnt = LicenseEntity()
        license_dict = dict[str, License]()
        for l in raw_metadata["licenses"]:
            common_props = license_gnt.creata_common_props(name=l['name'], description=l['description'])
            l_ent = license_gnt.generate_base(id=l['@id'], common_props=common_props)
            ro_crate.add(l_ent)
            license_dict[l['@id']] = l_ent

        # ==========================================================
        # data_downloads data to RO-Crate(DataDownload)
        # ==========================================================
        ddl_gnt = DataDownloadEntity()
        ddl_dict = dict[str, DataDownload]()
        for ddl in raw_metadata["data_downloads"]:
            common_props = ddl_gnt.creata_common_props(description=ddl['description'], sha256=ddl['sha256'],uploadDate=ddl['uploadDate'])
            ddl_ent = ddl_gnt.generate_base(id=ddl['@id'], common_props=common_props)
            ro_crate.add(ddl_ent)
            ddl_dict[ddl['@id']] = ddl_ent

        # ==========================================================
        # repository_objs data to RO-Crate(RepositoryObject)
        # ==========================================================
        repo_gnt = RepositoryObjectEntity()
        repo_dict = dict[str, RepositoryObject]()
        for repo in raw_metadata['repository_objs']:
            common_props = repo_gnt.creata_common_props(name=repo['name'], description=repo['description'])
            repo_ent = repo_gnt.generate_base(id=repo['@id'], common_props=common_props)
            ro_crate.add(repo_ent)
            repo_dict[repo['@id']] = repo_ent

        # ==========================================================
        # hosting_institutions data to RO-Crate(HostingInstitution)
        # ==========================================================
        host_inst_gnt = HostingInstitutionEntity()
        host_inst_dict = dict[str, HostingInstitution]()
        for host_inst in raw_metadata['hosting_institutions']:
            common_props = host_inst_gnt.creata_common_props(name=host_inst['name'], address=host_inst['address'], description=host_inst['description'])
            host_inst_ent = host_inst_gnt.generate_base(id=host_inst['@id'], common_props=common_props)
            ro_crate.add(host_inst_ent)
            host_inst_dict[host_inst['@id']] = host_inst_ent

        # ==========================================================
        # create person dict
        # ==========================================================
        p_gnt = PersonEntity()
        p_dict = dict[str, dict[str, Any]]()
        for p in raw_metadata['persons']:
            aff_ent = research_org_dict.get(p['affiliation'])
            if aff_ent == None:
                aff_ent = org_gnt.generate_empty_base()
            common_props = p_gnt.creata_common_props(name=p['name'], affiliation=aff_ent, email=p['email'], telephone=p['telephone'], alias=p['alias'])
            p_ent = p_gnt.generate_base(id=p['url'], common_props=common_props)
            ro_crate.add(p_ent)
            p_dict[p['id']] = p


        # ==========================================================
        # files data to RO-Crate(ginfork.File)
        # ==========================================================
        # Create ginfork.file
        file_gnt =  FileEntity()
        for file in raw_metadata["files"]:
            common_props = file_gnt.creata_common_props(name=file["name"], contentSize=file["contentSize"], sdDatePublished=file["sdDatePublished"],encodingFormat=file["encodingFormat"], sha256=file["sha256"], url=file["url"])

            file_ent = file_gnt.generate_ginfork(
                id=file["@id"],
                common_props=common_props,
                experimentPackageFlag=file["experimentPackageFlag"],
                )
            ro_crate.add(file_ent)

        # ==========================================================
        # datasets data to RO-Crate(Dataset)
        # ==========================================================
        # Create base.Dataset
        dataset_generator =DatasetEntity()
        for dataset in raw_metadata["datasets"]:
            common_props = dataset_generator.creata_common_props(
                name=dataset["name"],
                url=dataset["url"]
            )
            dataset_ent = dataset_generator.generate_base(
                id=dataset["@id"],
                common_props=common_props
            )
            ro_crate.add(dataset_ent)

        # ==========================================================
        # gin_monitoring data to RO-Crate(ginfork.GinMonitoring)
        # ==========================================================
        # Create ginfork.GinMnitoring
        gin_monitoring = raw_metadata["gin_monitoring"]
        gm_generator = GinMonitoringEntity()
        common_props = gm_generator.creata_common_props(
            about=ro_crate.root,
            contentSize=gin_monitoring["contentSize"],
            workflowIdentifier=gin_monitoring["workflowIdentifier"],
            datasetStructure=gin_monitoring["datasetStructure"],
            experimentPackageList=gin_monitoring["experimentPackageList"],
            parameterExperimentList=gin_monitoring["parameterExperimentList"]
            )
        gm_ent = gm_generator.generate_gifork(common_props=common_props)
        ro_crate.add(gm_ent)

        #==========================================================
        #                DMP data to RO-Crate
        #==========================================================

        # Create DMP
        dmps = raw_metadata["dmps"]
        dmp_meta_gnt = DMPMetadataEntity()
        dmp_gnt = DMPEntity()


        for dmp in dmps:
            funder_type = dmp['type']

            if funder_type == SchemaType.CAO.value:
                # Create cao.DMPMetadata
                # Create cao.DMP
                dmp_data = dmp['hasPart']
                dmp_data_list = list[cao_DMP]()
                cao_dmp_data_num = 0
                for data in dmp_data:
                    cao_dmp_data_num += 1
                    # Create cao.dmp.creator
                    creator_list = list()
                    for person_id in data['creator']:
                        p = p_dict.get(person_id)
                        if p == None:
                            raise Exception(f'creator(id: {person_id}) is not included in persons')
                        else:
                            ro_ent = RoCrateUtil.get_entity_by_entityname_id(ro_crate, cao_person, p['url'])
                            if ro_ent == None:
                                aff_ent = research_org_dict.get(p['affiliation'])
                                if aff_ent == None:
                                    aff_ent = org_gnt.generate_empty_base()
                                common_props = p_gnt.creata_common_props(name=p['name'], affiliation=aff_ent, email=p['email'], telephone=p['telephone'], alias=p['alias'])
                                p_ent = p_gnt.generate_cao(id=p['url'], common_props=common_props, eradResearcherNumber=p['eradResearcherNumber'])
                                ro_crate.add(p_ent)
                                creator_list.append(p_ent)
                            else:
                                creator_list.append(ro_ent)


                    # Create cao.dmp.dataManager
                    datamaneger_id = data.get('dataManager')
                    dm_ent:Entity
                    if datamaneger_id:
                        p = p_dict.get(datamaneger_id)
                        if p == None:
                            raise Exception(f'datamaneger(id: {datamaneger_id}) is not included in persons')
                        else:
                            ro_ent = RoCrateUtil.get_entity_by_entityname_id(ro_crate, cao_person, p['url'])
                            if ro_ent == None:
                                aff_ent = research_org_dict.get(p['affiliation'])
                                if aff_ent == None:
                                    aff_ent = org_gnt.generate_empty_base()
                                common_props = p_gnt.creata_common_props(name=p['name'], affiliation=aff_ent, email=p['email'], telephone=p['telephone'], alias=p['alias'])
                                p_ent = p_gnt.generate_cao(id=p['url'], common_props=common_props, eradResearcherNumber=p['eradResearcherNumber'])
                                ro_crate.add(p_ent)
                                dm_ent = p_ent
                            else:
                                dm_ent = ro_ent
                    else:
                        dm_ent = p_gnt.generate_empty_entity_cao()

                    repo_ent = self.get_ref_repo(data['repository'], repo_dict)
                    ddl_ent = self.get_ref_ddl(data['distribution'], ddl_dict)
                    host_inst_ent = self.get_ref_hostingInstitution(data['hostingInstitution'], host_inst_dict)
                    common_props = dmp_gnt.creata_common_props(
                                                dataNumber=cao_dmp_data_num,
                                                name=data['name'],
                                                description=data['description'],
                                                accessRights=data['accessRights'],
                                                repository=repo_ent,
                                                distribution=ddl_ent,
                                                contentSize=data['contentSize'],
                                                availabilityStarts=data['availabilityStarts']
                                                )
                    li_ent = license_dict.get(data['license'])
                    if li_ent == None:
                        li_ent = License("")
                    dmp_ent = dmp_gnt.generate_cao(common_props=common_props,
                                                   hostingInstitution=host_inst_ent,
                                                   keyword=data['keyword'],
                                                   creator=creator_list,
                                                   dataManager=dm_ent,
                                                   isAccessibleForFree=IsAccessibleForFreeType.value_of(data['isAccessibleForFree']),
                                                   license=li_ent,
                                                   usageInfo=data['usageInfo'])
                    ro_crate.add(dmp_ent)
                    dmp_data_list.append(dmp_ent)


                    # Create cao.File
                    for f in data['related_data']:
                        common_props = file_gnt.creata_common_props(
                            name=f['name'],
                            contentSize=f['contentSize'],
                            sdDatePublished=f['sdDatePublished'],
                            encodingFormat=f['encodingFormat'],
                            sha256=f['sha256'],
                            url=f['url']
                        )
                        f_ent = file_gnt.generate_cao(
                            id=f['@id'],
                            common_props=common_props,
                            dmpDataNumber=dmp_ent
                        )
                        ro_crate.add(f_ent)

                fd_ent = self.get_ref_funder(funder_type, fund_dict)

                repo_ent = self.get_ref_repo(dmp['repository'], repo_dict)

                ddl_ent = self.get_ref_ddl(dmp['distribution'], ddl_dict)

                common_props = dmp_meta_gnt.creata_common_props(
                    about=ro_crate.root,
                    funder=fd_ent,
                    repository=repo_ent,
                    distribution=ddl_ent,
                )
                dmp_metadata_ent = dmp_meta_gnt.generate_cao(
                                        common_props=common_props,
                                        keyword=dmp['keyword'],
                                        hasPart=dmp_data_list,
                                        eradProjectId=dmp['eradProjectId'])
                ro_crate.add(dmp_metadata_ent)
            elif funder_type == SchemaType.METI.value:
                # Create DMP of METI

                # Create cao.DMP
                dmp_data = dmp['hasPart']
                dmp_data_list = list[meti_DMP]()
                meti_dmp_data_num = 0
                for data in dmp_data:
                    meti_dmp_data_num += 1
                    repo_ent = self.get_ref_repo(data['repository'], repo_dict)
                    ddl_ent = self.get_ref_ddl(data['distribution'], ddl_dict)
                    host_inst_ent = self.get_ref_hostingInstitution(data['hostingInstitution'], host_inst_dict)
                    creator_list = list[Organization]()
                    for creator_org_id in data['creator']:
                        creator_list.append(self.get_ref_research_org(creator_org_id, research_org_dict))

                    l_ent = self.get_ref_license(data['license'], license_dict)

                    cp_gnt = ContactPointEntity()
                    raw_cp = data.get('contactPoint')
                    cp_ent = ContactPoint("")
                    if raw_cp is not None:
                        email = ''
                        telephone = ''
                        if raw_cp['email'] and raw_cp['telephone']:
                            email = raw_cp['email']
                        elif raw_cp['email'] and not raw_cp['telephone']:
                            email = raw_cp['email']
                        elif not raw_cp['email'] and raw_cp['telephone']:
                            telephone = raw_cp['telephone']
                        common_props = cp_gnt.creata_common_props(name=raw_cp['name'], email=email, telephone=telephone)
                        cp_ent = cp_gnt.generate_base(common_props=common_props)
                        if not self.is_has_duplication_contact_point(ro_crate=ro_crate, id=cp_ent.id):
                            ro_crate.add(cp_ent)


                    common_props = dmp_gnt.creata_common_props(
                        dataNumber=meti_dmp_data_num,
                        name=data['name'],
                        description=data['description'],
                        accessRights=data['accessRights'],
                        repository=repo_ent,
                        distribution=ddl_ent,
                        contentSize=data['contentSize'],
                        availabilityStarts=data['availabilityStarts']
                    )
                    dmp_ent = dmp_gnt.generate_meti(
                        common_props=common_props,
                        hostingInstitution=host_inst_ent,
                        wayOfManage=data['wayOfManage'],
                        creator=creator_list,
                        isAccessibleForFree=IsAccessibleForFreeType.value_of(data['isAccessibleForFree']),
                        license=l_ent,
                        usageInfo=data['usageInfo'],
                        reasonForConcealment=data['reasonForConcealment'],
                        measurementTechnique=data['measurementTechnique'],
                        contactPoint=cp_ent,
                    )
                    ro_crate.add(dmp_ent)
                    dmp_data_list.append(dmp_ent)


                    # Create meti.File
                    for f in data['related_data']:
                        common_props = file_gnt.creata_common_props(
                            name=f['name'],
                            contentSize=f['contentSize'],
                            sdDatePublished=f['sdDatePublished'],
                            encodingFormat=f['encodingFormat'],
                            sha256=f['sha256'],
                            url=f['url']
                        )
                        f_ent = file_gnt.generate_meti(
                            id=f['@id'],
                            common_props=common_props,
                            dmpDataNumber=dmp_ent
                        )
                        ro_crate.add(f_ent)

                fd_ent = self.get_ref_funder(funder_type, fund_dict)

                repo_ent = self.get_ref_repo(dmp['repository'], repo_dict)

                ddl_ent = self.get_ref_ddl(dmp['distribution'], ddl_dict)



                # Create meti.DMPMetadata.creator
                creator_list = list()
                for person_id in dmp['creator']:
                    p = p_dict.get(person_id)
                    if p == None:
                        raise Exception(f'creator(id: {person_id}) is not included in persons')
                    else:
                        ro_ent = RoCrateUtil.get_entity_by_entityname_id(ro_crate, base_Person, p['url'])
                        if ro_ent == None:
                            aff_ent = research_org_dict.get(p['affiliation'])
                            if aff_ent == None:
                                aff_ent = org_gnt.generate_empty_base()
                            common_props = p_gnt.creata_common_props(name=p['name'], affiliation=aff_ent, email=p['email'], telephone=p['telephone'], alias=p['alias'])
                            p_ent = p_gnt.generate_base(id=p['url'], common_props=common_props)
                            ro_crate.add(p_ent)
                            creator_list.append(p_ent)
                        else:
                            creator_list.append(ro_ent)


                common_props = dmp_meta_gnt.creata_common_props(
                    about=ro_crate.root,
                    funder=fd_ent,
                    repository=repo_ent,
                    distribution=ddl_ent,
                )
                dmp_metadata_ent = dmp_meta_gnt.generate_meti(
                    common_props=common_props,
                    hasPart=dmp_data_list,
                    creator=creator_list)
                ro_crate.add(dmp_metadata_ent)

            elif funder_type == SchemaType.AMED.value:
                # Create DMP of AMED
                dmp_data = dmp['hasPart']
                dmp_data_list = list[amed_DMP]()
                amed_dmp_data_num = 0
                for data in dmp_data:
                    amed_dmp_data_num += 1
                    repo_ent = self.get_ref_repo(data['repository'], repo_dict)
                    ddl_ent = self.get_ref_ddl(data['distribution'], ddl_dict)
                    crr_gnt = ClinicalResearchRegistrationEntity()
                    crr_list = list()
                    for crr in data['identifier']:
                        crr_id = crr['@id']
                        ro_ent = RoCrateUtil.get_entity_by_entityname_id(ro_crate, ClinicalResearchRegistration, crr_id)
                        if ro_ent != None:
                            crr_list.append(ro_ent)
                        else:
                            common_props = crr_gnt.creata_common_props(name=crr['name'], value=crr['value'])
                            crr_ent = crr_gnt.generate_amed(id=crr['@id'], common_props=common_props)
                            ro_crate.add(crr_ent)
                            crr_list.append(crr_ent)

                    common_props = dmp_gnt.creata_common_props(
                        dataNumber=amed_dmp_data_num,
                        name=data['name'],
                        description=data['description'],
                        accessRights=data['accessRights'],
                        repository=repo_ent,
                        distribution=ddl_ent,
                        contentSize=data['contentSize'],
                        availabilityStarts=data['availabilityStarts'])


                    dmp_ent = dmp_gnt.generate_amed(
                        common_props=common_props,
                        keyword=data['keyword'],
                        gotInformedConsent=GotInformedConsentType.value_of(data['gotInformedConsent']),
                        identifier=crr_list,
                        informedConsentFormat=InformedConsentFormatType.value_of(data['informedConsentFormat']),
                        reasonForConcealment=data['reasonForConcealment']
                    )
                    ro_crate.add(dmp_ent)
                    dmp_data_list.append(dmp_ent)

                    # Create amed.File
                    for f in data['related_data']:
                        common_props = file_gnt.creata_common_props(
                            name=f['name'],
                            contentSize=f['contentSize'],
                            sdDatePublished=f['sdDatePublished'],
                            encodingFormat=f['encodingFormat'],
                            sha256=f['sha256'],
                            url=f['url']
                        )
                        f_ent = file_gnt.generate_amed(
                            id=f['@id'],
                            common_props=common_props,
                            dmpDataNumber=dmp_ent
                        )
                        ro_crate.add(f_ent)

                fd_ent = self.get_ref_funder(funder_type, fund_dict)

                repo_ent = self.get_ref_repo(dmp['repository'], repo_dict)

                ddl_ent = self.get_ref_ddl(dmp['distribution'], ddl_dict)

                host_inst_ent = self.get_ref_hostingInstitution(dmp['hostingInstitution'], host_inst_dict)

                chiefResearcher_ent: Entity
                chiefResearcher_id = dmp.get('chiefResearcher')
                if chiefResearcher_id:
                    p = p_dict.get(chiefResearcher_id)
                    if p == None:
                        raise Exception(f'datamaneger(id: {chiefResearcher_id}) is not included in persons')
                    else:
                        ro_ent = RoCrateUtil.get_entity_by_entityname_id(ro_crate, base_Person, p['url'])
                        if ro_ent == None:
                            aff_ent = research_org_dict.get(p['affiliation'])
                            if aff_ent == None:
                                aff_ent = org_gnt.generate_empty_base()
                            common_props = p_gnt.creata_common_props(name=p['name'], affiliation=aff_ent, email=p['email'], telephone=p['telephone'], alias=p['alias'])
                            p_ent = p_gnt.generate_base(id=p['url'], common_props=common_props)
                            ro_crate.add(p_ent)
                            chiefResearcher_ent = p_ent
                        else:
                            chiefResearcher_ent = ro_ent
                else:
                    chiefResearcher_ent = p_gnt.generate_empty_entity_base()

                creator_list = list[Entity]()
                for person_id in dmp['creator']:
                    p = p_dict.get(person_id)
                    if p == None:
                        raise Exception(f'creator(id: {person_id}) is not included in persons')
                    else:
                        ro_ent = RoCrateUtil.get_entity_by_entityname_id(ro_crate, base_Person, p['url'])
                        if ro_ent == None:
                            aff_ent = research_org_dict.get(p['affiliation'])
                            if aff_ent == None:
                                aff_ent = org_gnt.generate_empty_base()
                            common_props = p_gnt.creata_common_props(name=p['name'], affiliation=aff_ent, email=p['email'], telephone=p['telephone'], alias=p['alias'])
                            p_ent = p_gnt.generate_base(id=p['url'], common_props=common_props)
                            ro_crate.add(p_ent)
                            creator_list.append(p_ent)
                        else:
                            creator_list.append(ro_ent)

                dataManager_ent: Entity
                datamaneger_id = dmp.get('dataManager')
                if datamaneger_id:
                    p = p_dict.get(datamaneger_id)
                    if p == None:
                        raise Exception(f'datamaneger(id: {datamaneger_id}) is not included in persons')
                    else:
                        ro_ent = RoCrateUtil.get_entity_by_entityname_id(ro_crate, base_Person, p['url'])
                        if ro_ent == None:
                            aff_ent = research_org_dict.get(p['affiliation'])
                            if aff_ent == None:
                                aff_ent = org_gnt.generate_empty_base()
                            common_props = p_gnt.creata_common_props(name=p['name'], affiliation=aff_ent, email=p['email'], telephone=p['telephone'], alias=p['alias'])
                            p_ent = p_gnt.generate_base(id=p['url'], common_props=common_props)
                            ro_crate.add(p_ent)
                            dataManager_ent = p_ent
                        else:
                            dataManager_ent = ro_ent
                else:
                    dataManager_ent = p_gnt.generate_empty_entity_base()

                common_props = dmp_meta_gnt.creata_common_props(
                    about=ro_crate.root,
                    funder=fd_ent,
                    repository=repo_ent,
                    distribution=ddl_ent,
                )
                dmp_metadata_ent = dmp_meta_gnt.generate_amed(
                    common_props=common_props,
                    funding=dmp['funding'],
                    chiefResearcher=chiefResearcher_ent,
                    hostingInstitution=host_inst_ent,
                    dataManager=dataManager_ent,
                    hasPart=dmp_data_list,
                    creator=creator_list
                )
                ro_crate.add(dmp_metadata_ent)

        return ro_crate.as_jsonld()

    def check_key(self):
        invalid_Msg = dict()
        absence_list = list[str]()
        invaid_type_list = list[str]()
        invalid_value_list = list[str]()
        data = self.raw_metadata
        absence_keys, invalid_type_keys = self.check_key_raw_metadata()
        absence_list.extend(absence_keys)
        invaid_type_list.extend(invalid_type_keys)

        if data.get('research_project') != None:
            absence_keys, invalid_type_keys = self.check_key_research_project()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('funder_orgs') != None:
            absence_keys, invalid_type_keys = self.check_key_funder_orgs()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('research_orgs') != None:
            absence_keys, invalid_type_keys = self.check_key_research_orgs()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('licenses') != None:
            absence_keys, invalid_type_keys = self.check_key_licenses()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('data_downloads') != None:
            absence_keys, invalid_type_keys = self.check_key_data_downloads()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('repository_objs') != None:
            absence_keys, invalid_type_keys = self.check_key_repository_objs()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('hosting_institutions') != None:
            absence_keys, invalid_type_keys = self.check_key_hosting_institutions()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('persons') != None:
            absence_keys, invalid_type_keys = self.check_key_persons()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('files') != None:
            absence_keys, invalid_type_keys =self.check_key_files()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('datasets') != None:
            absence_keys, invalid_type_keys = self.check_key_datasets()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('gin_monitoring') != None:
            absence_keys, invalid_type_keys = self.check_key_gin_monitoring()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
        if data.get('dmps') != None:
            absence_keys, invalid_type_keys, invalid_values= self.check_key_dmps()
            absence_list.extend(absence_keys)
            invaid_type_list.extend(invalid_type_keys)
            invalid_value_list.extend(invalid_values)

        if len(absence_list)>0 or len(invaid_type_list)>0 or len(invalid_value_list)>0:
            if len(absence_list)>0:
                invalid_Msg['required_key'] = absence_list
            if len(invaid_type_list)>0:
                invalid_Msg['invalid_value_type'] = invaid_type_list
            if len(invalid_value_list)>0:
                invalid_Msg['invalid_value'] = invalid_value_list
            raise JsonValidationError(invalid_Msg)




    def check_key_raw_metadata(self):
        data = self.raw_metadata
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        key_list = data.keys()
        targets = ['research_project', 'funder_orgs', 'research_orgs', 'licenses', 'data_downloads', 'repository_objs','hosting_institutions', 'persons', 'files', 'datasets', 'gin_monitoring', 'dmps']
        for target in targets:
            if target not in key_list:
                absence_list.append(f'{target}')
            else:
                value = data.get(target)
                if target == 'research_project' or target == 'gin_monitoring':
                    if type(value) is not dict:
                        invaid_type_list.append(f'{target} is not object')
                else:
                    if type(value) is not list:
                        invaid_type_list.append(f'{target} is not array')

        return absence_list, invaid_type_list

    def check_key_research_project(self):
        object_name = 'research_project'
        data = self.raw_metadata[object_name]
        absence_list = list[str]()
        invaid_type_list = list[str]()
        key_list = data.keys()
        targets = ['name', 'description']
        for target in targets:
            if target not in key_list:
                absence_list.append(f'{object_name}.{target}')
            else:
                value = data.get(target)
                if type(value) is not str:
                    invaid_type_list.append(f'{object_name}.{target} is not string')

        return absence_list, invaid_type_list

    def check_key_gin_monitoring(self):
        object_name = 'gin_monitoring'
        data = self.raw_metadata[object_name]
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        if type(data) is not dict:
            invaid_type_list.append(f'{object_name} is not object')
            return absence_list, invaid_type_list

        targets = ['contentSize', 'workflowIdentifier', 'datasetStructure', 'experimentPackageList', 'parameterExperimentList']
        key_list = data.keys()
        for target in targets:
            if target not in key_list:
                absence_list.append(f'{object_name}.{target}')
            elif target == 'experimentPackageList' or target == 'parameterExperimentList':
                value = data.get(target)
                if type(value) is not list:
                    invaid_type_list.append(f'{object_name}.{target} is not array')
                else:
                    for index in range(len(value)):
                        if type(value[index]) is not str:
                            invaid_type_list.append(f'{object_name}.{target}[{index}] is not string')

            else:
                value = data.get(target)
                if type(value) is not str:
                    invaid_type_list.append(f'{object_name}.{target} is not string')

        return absence_list, invaid_type_list

    def check_key_funder_orgs(self):
        object_name = 'funder_orgs'
        data = self.raw_metadata[object_name]
        absence_list = list[str]()
        invaid_type_list = list[str]()
        targets = ['type', '@id', 'name', 'alias', 'description']
        for index in range(len(data)):
            org = data[index]
            if type(org) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue

            key_list = org.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = org.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')

        return absence_list, invaid_type_list

    def check_key_research_orgs(self):
        object_name = 'research_orgs'
        data = self.raw_metadata[object_name]
        absence_list = list[str]()
        invaid_type_list = list[str]()
        targets = ['@id', 'name', 'alias', 'description']
        for index in range(len(data)):
            org = data[index]
            if type(org) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = org.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = org.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list

    def check_key_licenses(self):
        object_name = 'licenses'
        data = self.raw_metadata[object_name]
        absence_list = list[str]()
        invaid_type_list = list[str]()
        targets = ['@id', 'name', 'description']
        for index in range(len(data)):
            license = data[index]
            if type(license) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = license.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = license.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list

    def check_key_data_downloads(self):
        object_name = 'data_downloads'
        data = self.raw_metadata[object_name]
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        targets = ['@id', 'description', 'sha256', 'uploadDate']
        for index in range(len(data)):
            data_download = data[index]
            if type(data_download) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = data_download.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = data_download.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list

    def check_key_repository_objs(self):
        object_name = 'repository_objs'
        data = self.raw_metadata[object_name]
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        targets = ['@id', 'name', 'description']
        for index in range(len(data)):
            repo = data[index]
            if type(repo) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = repo.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = repo.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list

    def check_key_hosting_institutions(self):
        object_name = 'hosting_institutions'
        data = self.raw_metadata[object_name]
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        targets = ['@id', 'name', 'description', 'address']
        for index in range(len(data)):
            host_inst = data[index]
            if type(host_inst) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = host_inst.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = host_inst.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list

    def check_key_persons(self):
        object_name = 'persons'
        data = self.raw_metadata[object_name]
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        targets = ['id','url', 'name', 'alias', 'affiliation', 'email', 'telephone', 'eradResearcherNumber']
        for index in range(len(data)):
            person = data[index]
            if type(person) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = person.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = person.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list

    def check_key_files(self):
        object_name = 'files'
        data = self.raw_metadata[object_name]
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        targets = ['@id', 'name', 'contentSize', 'encodingFormat', 'sha256', 'url', 'sdDatePublished', 'experimentPackageFlag']
        for index in range(len(data)):
            file = data[index]
            if type(file) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = file.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    if target == 'experimentPackageFlag':
                        value = file.get(target)
                        if type(value) is not bool:
                            invaid_type_list.append(f'{object_name}[{index}].{target} is not boolean')
                    else:
                        value = file.get(target)
                        if type(value) is not str:
                            invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list

    def check_key_datasets(self):
        object_name = 'datasets'
        data = self.raw_metadata[object_name]
        absence_list : list[str] = list[str]()
        invaid_type_list = list[str]()
        targets = ['@id', 'name', 'url']
        for index in range(len(data)):
            dataset = data[index]
            if type(dataset) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = dataset.keys()
            for target in targets:
                if target not in key_list:
                    absence_list.append(f'{object_name}[{index}].{target}')
                else:
                    value = dataset.get(target)
                    if type(value) is not str:
                         invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
        return absence_list, invaid_type_list



    def check_key_dmps(self):
        object_name = 'dmps'
        data = self.raw_metadata[object_name]
        absence_list = list[str]()
        invalid_value_list = list[str]()
        invaid_type_list = list[str]()
        has_type_index_list = list()
        has_has_part_index_list = list()
        type_key = 'type'
        hasPart_key = 'hasPart'
        for index in range(len(data)):
            dmp = data[index]
            if type(dmp) is not dict:
                invaid_type_list.append(f'{object_name}[{index}] is not object')
                continue
            key_list = dmp.keys()
            if type_key not in key_list:
                absence_list.append(f'{object_name}[{index}].{type_key}')
            else:
                has_type_index_list.append(index)

            if hasPart_key not in key_list:
                absence_list.append(f'{object_name}[{index}].{hasPart_key}')
            else:
                if type(dmp.get(hasPart_key)) is not list:
                    invaid_type_list.append(f'{object_name}[{index}].{hasPart_key} is not array')
                    continue
                elif len(dmp[hasPart_key]) > 0:
                    has_has_part_index_list.append(index)



        for index in has_type_index_list:
            dmp = data[index]
            dmp_type = dmp[type_key]
            if type(dmp_type) is not str:
                invaid_type_list.append(f'{object_name}[{index}].{type_key} is not string')
            key_list = dmp.keys()
            if dmp_type == 'cao':
                targets = ['repository', 'distribution', 'keyword', 'eradProjectId']
                for target in targets:
                    if target not in key_list:
                        absence_list.append(f'{object_name}[{index}].{target}')
                    else:
                        value = dmp.get(target)
                        if type(value) is not str:
                            invaid_type_list.append(f'{object_name}[{index}].{target} is not string')

            elif dmp_type == 'meti':
                targets = ['creator', 'repository', 'distribution']
                for target in targets:
                    if target not in key_list:
                        absence_list.append(f'{object_name}[{index}].{target}')
                    else:
                        value = dmp.get(target)
                        if target == 'creator':
                            if type(value) is not list:
                                invaid_type_list.append(f'{object_name}[{index}].{target} is not array')
                            else:
                                for creator_index in range(len(value)):
                                        if type(value[creator_index]) is not str:
                                            invaid_type_list.append(f'{object_name}[{index}].{target}[{creator_index}] is not string')
                        else:
                            if type(value) is not str:
                                invaid_type_list.append(f'{object_name}[{index}].{target} is not string')

            elif dmp_type == 'amed':
                targets = ['funding', 'chiefResearcher', 'creator', 'hostingInstitution', 'dataManager', 'repository', 'distribution']
                for target in targets:
                    if target not in key_list:
                        absence_list.append(f'{object_name}[{index}].{target}')
                    else:
                        value = dmp.get(target)
                        if target == 'creator':
                            if type(value) is not list:
                                invaid_type_list.append(f'{object_name}[{index}].{target} is not array')
                            else:
                                for creator_index in range(len(value)):
                                        if type(value[creator_index]) is not str:
                                            invaid_type_list.append(f'{object_name}[{index}].{target}[{creator_index}] is not string')
                        else:
                            if type(value) is not str:
                                invaid_type_list.append(f'{object_name}[{index}].{target} is not string')
            else:
                invalid_value_list.append(f'{object_name}[{index}].{type_key} is invaid_value. only cao. meti, amed')


        # =====================================
        # Check Key for hasPart(DMP)
        # ====================================
        for index in has_has_part_index_list:
            dmp = data[index]
            dmp_type = dmp[type_key]
            hasPart = dmp[hasPart_key]

            if dmp_type == 'cao':
                targets = ['name', 'description', 'creator', 'keyword', 'accessRights', 'availabilityStarts', 'isAccessibleForFree', 'license', 'usageInfo', 'repository', 'distribution', 'contentSize', 'hostingInstitution', 'dataManager', 'related_data']

                for dmp_data_index in range(len(hasPart)):
                    dmp_data = hasPart[dmp_data_index]
                    if type(dmp_data) is not dict:
                        invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}] is not object')
                        continue
                    key_list = dmp_data.keys()
                    for target in targets:
                        if target not in key_list:
                            absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}')
                        else:
                            value = dmp_data.get(target)
                            if target == 'creator':
                                if type(value) is not list:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target} is not array')
                                else:
                                    for creator_index in range(len(value)):
                                        if type(value[creator_index]) is not str:
                                            invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}[{creator_index}] is not string')
                            elif target == 'related_data':
                                if type(value) is not list:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target} is not array')
                                else:
                                    for related_data_index in range(len(value)):
                                        related_data = value[related_data_index]
                                        if type(related_data) is not dict:
                                            invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}[{related_data_index}] is not object')
                                        else:
                                            key_list = related_data.keys()
                                            file_targets = ['@id', 'name', 'contentSize', 'encodingFormat', 'sha256', 'url', 'sdDatePublished']
                                            for file_target in file_targets:
                                                if file_target not in key_list:
                                                    absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].related_data[{related_data_index}].{file_target}')
                                                else:
                                                    related_data_value = related_data.get(file_target)
                                                    if type(related_data_value) is not str:
                                                        invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].related_data[{related_data_index}].{file_target} is not string')
                            else:
                                if type(value) is not str:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target} is not string')



            elif dmp_type == 'meti':
                targets = ['name', 'description', 'hostingInstitution', 'wayOfManage', 'accessRights', 'reasonForConcealment', 'availabilityStarts', 'creator', 'measurementTechnique', 'isAccessibleForFree', 'license', 'usageInfo', 'repository', 'contentSize', 'distribution', 'contactPoint', 'related_data']
                has_contactPoint_index_list = list()
                contactPoint_key = 'contactPoint'
                for dmp_data_index in range(len(hasPart)):
                    dmp_data = hasPart[dmp_data_index]
                    if type(dmp_data) is not dict:
                        invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}] is not object')
                        continue
                    key_list = dmp_data.keys()

                    for target in targets:
                        if contactPoint_key == target:
                            if target not in key_list:
                                absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}')
                            else:
                                value = dmp_data.get(contactPoint_key)
                                if type(value) is dict:
                                    has_contactPoint_index_list.append(dmp_data_index)
                                elif value is not None:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}]{target} is not object')
                        elif target not in key_list:
                            absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}')
                        else:
                            value = dmp_data.get(target)
                            if target == 'creator':
                                if type(value) is not list:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}]{target} is not array')
                                else:
                                    for creator_index in range(len(value)):
                                        if type(value[creator_index]) is not str:
                                            invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}]{target}[{creator_index}] is not string')

                            elif target == 'related_data':
                                if type(value) is not list:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}]{target} is not array')
                                else:
                                    for related_data_index in range(len(value)):
                                        related_data = value[related_data_index]
                                        if type(related_data) is not dict:
                                            invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}[{related_data_index}] is not object')
                                        else:
                                            key_list = related_data.keys()
                                            file_targets = ['@id', 'name', 'contentSize', 'encodingFormat', 'sha256', 'url', 'sdDatePublished']
                                            for file_target in file_targets:
                                                if file_target not in key_list:
                                                    absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].related_data[{related_data_index}].{file_target}')
                                                else:
                                                    related_data_value = related_data.get(file_target)
                                                    if type(related_data_value) is not str:
                                                        invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].related_data[{related_data_index}].{file_target} is not string')


                            else:
                                if type(value) is not str:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target} is not string')

                for dmp_data_index in has_contactPoint_index_list:
                    contactPoint = hasPart[dmp_data_index][contactPoint_key]

                    contactPoint_targets = ['name', 'email', 'telephone']
                    key_list = contactPoint.keys()
                    for contactPoint_target in contactPoint_targets:
                        if contactPoint_target not in key_list:
                            absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{contactPoint_key}.{contactPoint_target}')
                        else:
                            value = contactPoint.get(contactPoint_target)
                            if type(value) is not str:
                                invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{contactPoint_key}.{contactPoint_target} is not string')

            elif  dmp_type == 'amed':
                targets = ['name', 'description','keyword', 'accessRights', 'availabilityStarts', 'reasonForConcealment', 'repository', 'distribution', 'contentSize', 'gotInformedConsent', 'informedConsentFormat', 'identifier', 'related_data']
                identifier_key = 'identifier'
                for dmp_data_index in range(len(hasPart)):
                    dmp_data = hasPart[dmp_data_index]
                    if type(dmp_data) is not dict:
                        invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}] is not object')
                        continue
                    key_list = dmp_data.keys()
                    for target in targets:
                        if identifier_key == target:
                            if target not in key_list:
                                absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}')
                            else:
                                identifier_targets = ['@id', 'name', 'value']
                                identifier_list = dmp_data.get(identifier_key)
                                if type(identifier_list) is not list:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{identifier_key} is not array')
                                else:
                                    for identifier_index in range(len(identifier_list)):
                                        identifier = identifier_list[identifier_index]
                                        if type(identifier) is not dict:
                                            invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{identifier_key}[{identifier_index}] is not object')
                                        else:
                                            identifier_key_list = identifier.keys()
                                            for identifier_target in identifier_targets:
                                                if identifier_target not in identifier_key_list:
                                                    absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{identifier_key}[{identifier_index}].{identifier_target}')
                                                else:
                                                    value = identifier.get(identifier_target)
                                                    if type(value) is not str:
                                                        invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{identifier_key}[{identifier_index}].{identifier_target} is not string')
                        elif target not in key_list:
                            absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target}')
                        else:
                            value = dmp_data.get(target)
                            if target == 'related_data':
                                if type(value) is not list:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}]{target} is not array')
                                else:
                                     for related_data_index in range(len(value)):
                                        related_data = value[related_data_index]
                                        if type(related_data) is not dict:
                                            invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}]{target}[{related_data_index}] is not object')
                                        else:
                                            key_list = related_data.keys()
                                            file_targets = ['@id', 'name', 'contentSize', 'encodingFormat', 'sha256', 'url', 'sdDatePublished']
                                            for file_target in file_targets:
                                                if file_target not in key_list:
                                                    absence_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].related_data[{related_data_index}].{file_target}')
                                                else:
                                                    related_data_value = related_data.get(file_target)
                                                    if type(related_data_value) is not str:
                                                        invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].related_data[{related_data_index}].{file_target} is not string')
                            else:
                                if type(value) is not str:
                                    invaid_type_list.append(f'{object_name}[{index}].hasPart[{dmp_data_index}].{target} is not string')
        return absence_list, invaid_type_list, invalid_value_list


    def get_ref_repo(self, repo_id:str, repo_dict:dict):
        repo_ent: RepositoryObject
        if repo_id:
            repo = repo_dict.get(repo_id)
            if repo != None:
                repo_ent = repo
            else:
                raise Exception(f'repository (id : {repo_id}) is not included in repository_obj.')
        else:
            repo_ent = RepositoryObject('')

        return repo_ent

    def get_ref_ddl(self, ddl_id:str, ddl_dict:dict):
        ddl_ent : DataDownload

        if ddl_id:
            ddl = ddl_dict.get(ddl_id)
            if ddl != None:
                ddl_ent = ddl
            else:
                raise Exception(f'distribution (id : {ddl_id}) is not included in data_downloads.')
        else:
            ddl_ent = DataDownload('')

        return ddl_ent

    def get_ref_hostingInstitution(self, host_inst_id:str, host_inst_dict:dict):
        host_inst_ent : HostingInstitution
        if host_inst_id:
            hi = host_inst_dict.get(host_inst_id)
            if hi != None:
                host_inst_ent = hi
            else:
                raise Exception(f'hostingInstitution (id : {host_inst_id}) is not included in hosting_institution_list.')
        else:
            host_inst_ent = HostingInstitution('')

        return host_inst_ent

    def get_ref_funder(self, funder_type:str, funder_dict:dict):
        funder_ent : Organization
        funder = funder_dict.get(funder_type)
        if funder != None:
            funder_ent = funder
        else:
            raise Exception(f'funder (type : {funder_type}) is not included in root_data_entity.funder.')

        return funder_ent

    def get_ref_research_org(self, research_org_id:str, research_org_dict):
        research_org_ent : Organization
        research_org = research_org_dict.get(research_org_id)
        if research_org != None:
            research_org_ent = research_org
        else:
            raise Exception(f'Organization (id : {research_org_id}) is not included in hosting_institution_list.')

        return research_org_ent

    def get_ref_license(self, license_id:str, license_dict):
        l_ent : License
        l = license_dict.get(license_id)
        if l != None:
            l_ent = l
        else:
            raise Exception(f'License (id : {license_id}) is not included in licenses.')

        return l_ent

    def is_has_duplication_contact_point(self, ro_crate:ROCrate, id:str) -> bool:
        entity_list_by_id = ro_crate.get_by_id(id)
        for e in entity_list_by_id:
            if type(e) is ContactPoint:
                return True

        return False

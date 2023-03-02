
import os
from typing import Any, Type
from urllib.parse import urlparse
from dg_packager.error.error import ParameterError
from dg_packager.utils.enum.entity_type import EntityType

from dg_packager.utils.enum.property_type import PropertyType
from dg_packager.utils.enum.schema_type import SchemaType
from nii_dg.ro_crate import ROCrate
from nii_dg.entity import Entity
from nii_dg.schema.base import File as Base_File, Person as Base_Person
from nii_dg.schema.cao import File as Cao_File, DMPMetadata as Cao_DMPMetadata, DMP as Cao_DMP, Person as Cao_Person
from nii_dg.schema.meti import File as Meti_File, DMPMetadata as Meti_DMPMetadata, DMP as Meti_DMP
from nii_dg.schema.amed import File as Amed_File, DMPMetadata as Amed_DMPMetadata, DMP as Amed_DMP
from nii_dg.schema.ginfork import File as Ginfork_File


class RoCrateUtil:

    # ==================================================================
    # Operationg RO-Crate <JSON>
    # ==================================================================

    @staticmethod
    def get_all_entity_data_form_json(ro_crate_json: dict[str, Any]) -> list[dict[str, Any]]:
        '''
        RO-Crate(JSON) から 全ての Entity データを取得する。
        '''
        return ro_crate_json['@graph']

    @staticmethod
    def get_context_value_form_json(ro_crate_json: dict[str, Any]) -> str:
        '''
        RO-Crate(JSON) から 全ての @context の値を取得する。
        '''
        return str(ro_crate_json.get(PropertyType.CONTEXT.value))

    @staticmethod
    def get_entity_by_type_form_json(ro_crate_json: dict[str, Any], entity_type: EntityType) -> list[dict[str, Any]]:
        '''
        RO-Crate(JSON) から指定の Entity Type のentity dataを取得する。
        '''
        ro_entity_list = RoCrateUtil.get_all_entity_data_form_json(ro_crate_json)

        entity_list = list[dict[str, Any]]()

        for e in ro_entity_list:
            e_type = e.get(PropertyType.TYPE.value)
            if e_type == entity_type.value:
                entity_list.append(e)

        return entity_list

    @staticmethod
    def get_entity_by_schema_form_json(ro_crate_json: dict[str, Any], schema_type: SchemaType) -> list[dict[str, Any]]:
        '''
        RO-Crate(JSON) から指定の Schema Type のentity dataを取得する。
        '''
        ro_entity_list = RoCrateUtil.get_all_entity_data_form_json(ro_crate_json)

        entity_list = list[dict[str, Any]]()

        for e in ro_entity_list:
            schema_path = e.get(PropertyType.CONTEXT.value)
            schema_name = RoCrateUtil.get_schema_name_form_path(schema_path)
            if schema_name == schema_type.value:
                entity_list.append(e)

        return entity_list

    @staticmethod
    def get_entity_by_entity_and_schema_form_json(ro_crate_json: dict[str, Any], entity_type: EntityType,  schema_type: SchemaType) -> list[dict[str, Any]]:
        '''
        RO-Crate(JSON) から指定の Schema Type と Entity Type のentity dataを取得する。
        '''
        ro_entity_list = RoCrateUtil.get_all_entity_data_form_json(ro_crate_json)

        entity_list = list[dict[str, Any]]()

        for e in ro_entity_list:
            schema_path = e.get(PropertyType.CONTEXT.value)
            schema_name = RoCrateUtil.get_schema_name_form_path(schema_path)
            e_type = e.get(PropertyType.TYPE.value)
            if schema_name == schema_type.value and e_type == entity_type.value:
                entity_list.append(e)

        return entity_list

    @staticmethod
    def get_schema_name_form_path(url) -> str:
        path = urlparse(url).path
        split_path = os.path.split(path)
        split_path =os.path.split(split_path[0])
        return split_path[1]

    @staticmethod
    def get_entity_by_instance(ro_crate: ROCrate, entity_name: Type[Entity])-> list[Entity]:
        '''
        RO-Crate(instance) から指定の Entity(base.File, cao.File, meti.File, ..... cao.DMP など) のentityリストを取得する。
        '''
        return ro_crate.get_by_entity_type(entity=entity_name)

    # ==================================================================
    # Operationg RO-Crate <instance from nii_dg.ro_crate.ROCrat>
    # ==================================================================
    @staticmethod
    def get_file_by_instance(ro_crate: ROCrate, schema_type: SchemaType)-> list[Entity]:
        '''
        RO-Crate(instance) から指定の Schema Type の File entity リストを取得する。
        '''
        if schema_type == SchemaType.BASE:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Base_File)
        elif schema_type == SchemaType.CAO:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Cao_File)
        elif schema_type == SchemaType.AMED:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Amed_File)
        elif schema_type == SchemaType.METI:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Meti_File)
        else:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Ginfork_File)

    @staticmethod
    def get_dmp_metadata_by_instance(ro_crate: ROCrate, schema_type: SchemaType)-> list[Entity]:
        '''
        RO-Crate(instance) から指定の Schema Type の DMPMetadata entity リストを取得する。
        '''
        if schema_type == SchemaType.METI:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Meti_DMPMetadata)
        elif schema_type == SchemaType.CAO:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Cao_DMPMetadata)
        elif schema_type == SchemaType.AMED:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Amed_DMPMetadata)
        else:
            raise ParameterError('DMP Metadata Dose not have Base and Gindfork Schema')

    @staticmethod
    def get_dmp_by_instance(ro_crate: ROCrate, schema_type: SchemaType)-> list[Entity]:
        '''
        RO-Crate(instance) から指定の Schema Type の DMP entity リストを取得する。
        '''
        if schema_type == SchemaType.METI:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Meti_DMP)
        elif schema_type == SchemaType.CAO:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Cao_DMP)
        elif schema_type == SchemaType.AMED:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Amed_DMP)
        else:
            raise ParameterError('DMP Dose not have Base and Gindfork Schema')

    @staticmethod
    def get_person_by_instance(ro_crate: ROCrate, schema_type: SchemaType)-> list[Entity]:
        '''
        RO-Crate(instance) から指定の Schema Type の Person entity リストを取得する。
        '''
        if schema_type == SchemaType.BASE:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Base_Person)
        elif schema_type == SchemaType.CAO:
            return RoCrateUtil.get_entity_by_instance(ro_crate=ro_crate, entity_name=Cao_Person)
        else:
            raise ParameterError('DMP Dose not have Base, Meti, Amed amd Gindfork Schema')

    @staticmethod
    def get_entity_by_entityname_id(ro_crate: ROCrate, entity: Type[Entity], id:str):
        entity_list_by_id = ro_crate.get_by_id(id)
        ent = None
        for e in entity_list_by_id:
            if type(e) is entity:
                ent = e
                break

        return ent

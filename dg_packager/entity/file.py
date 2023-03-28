
from typing import Any

from dg_packager.utils.enum.property_type import PropertyType
from nii_dg.schema.base import File as Base_File
from nii_dg.schema.cao import File as Cao_File, DMP as Cao_DMP
from nii_dg.schema.amed import File as Amed_File, DMP as Amed_DMP
from nii_dg.schema.meti import File as Meti_File, DMP as Meti_DMP
from nii_dg.schema.ginfork import File as Ginfork_File


class FileEntity:
    '''
    FileEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_File:
        '''
        base の File インスタンスの生成メソッド
        '''
        return Base_File(id_=id, props=common_props)

    def generate_cao(self,
                     id: str,
                     common_props: dict[str, Any],
                     dmpDataNumber: Cao_DMP,
                     ) -> Cao_File:
        '''
        cao の File インスタンスの生成メソッド
        '''
        props = common_props

        dmpDataNumber_id = dmpDataNumber.data.get(PropertyType.ID.value)
        if dmpDataNumber_id:
            props["dmpDataNumber"] = dmpDataNumber

        return Cao_File(id_=id, props=props)

    def convert_to_cao(self, file: Base_File, dmpDataNumber: Cao_DMP,) -> Cao_File:
        common_props = self.get_common_props(file)

        return self.generate_cao(id=file.data[PropertyType.ID.value], common_props=common_props, dmpDataNumber=dmpDataNumber)

    def convert_to_multi_cao(self, entity_list: list[tuple[Base_File, Cao_DMP]]) -> list[Cao_File]:
        cao_file_list = list[Cao_File]()

        for entity in entity_list:
            file = entity[0]
            dmp = entity[1]
            cao_file = self.convert_to_cao(file=file, dmpDataNumber=dmp)
            cao_file_list.append(cao_file)

        return cao_file_list

    def generate_amed(self,
                      id: str,
                      common_props: dict[str, Any],
                      dmpDataNumber: Amed_DMP,
                      ) -> Amed_File:
        '''
        amed の File インスタンスの生成メソッド
        '''
        props = common_props

        dmpDataNumber_id = dmpDataNumber.data.get(PropertyType.ID.value)
        if dmpDataNumber_id:
            props["dmpDataNumber"] = dmpDataNumber

        return Amed_File(id_=id, props=props)

    def convert_to_amed(self, file: Base_File, dmpDataNumber: Amed_DMP) -> Amed_File:
        common_props = self.get_common_props(file)

        return self.generate_amed(id=file.data[PropertyType.ID.value], common_props=common_props, dmpDataNumber=dmpDataNumber)

    def convert_to_multi_amed(self, entity_list: list[tuple[Base_File, Amed_DMP]]) -> list[Amed_File]:
        amed_file_list = list[Amed_File]()

        for entity in entity_list:
            file = entity[0]
            dmp = entity[1]
            amed_file = self.convert_to_amed(file=file, dmpDataNumber=dmp)
            amed_file_list.append(amed_file)

        return amed_file_list

    def generate_meti(self,
                      id: str,
                      common_props: dict[str, Any],
                      dmpDataNumber: Meti_DMP
                      ) -> Meti_File:
        '''
        meti の File インスタンスの生成メソッド
        '''
        props = common_props

        dmpDataNumber_id = dmpDataNumber.data.get(PropertyType.ID.value)
        if dmpDataNumber_id:
            props["dmpDataNumber"] = dmpDataNumber

        return Meti_File(id_=id, props=props)

    def convert_to_meti(self, file: Base_File, dmpDataNumber: Meti_DMP) -> Meti_File:
        common_props = self.get_common_props(file)

        return self.generate_meti(id=file.data[PropertyType.ID.value], common_props=common_props, dmpDataNumber=dmpDataNumber)

    def convert_to_multi_meti(self, entity_list: list[tuple[Base_File, Meti_DMP]]) -> list[Meti_File]:
        meti_file_list = list[Meti_File]()

        for entity in entity_list:
            file = entity[0]
            dmp = entity[1]
            meti_file = self.convert_to_meti(file=file, dmpDataNumber=dmp)
            meti_file_list.append(meti_file)

        return meti_file_list

    def generate_ginfork(self,
                         id: str,
                         common_props: dict[str, Any],
                         experimentPackageFlag: bool
                         ) -> Ginfork_File:
        '''
        ginfork の File インスタンスの取得メソッド
        '''
        props = common_props
        props["experimentPackageFlag"] = experimentPackageFlag
        return Ginfork_File(id_=id, props=props)

    def convert_to_ginfork(self, file: Base_File, experimentPackageFlag: bool) -> Ginfork_File:
        common_props = self.get_common_props(file)

        return self.generate_ginfork(id=file.data[PropertyType.ID.value], common_props=common_props, experimentPackageFlag=experimentPackageFlag)

    def convert_to_multi_ginfork(self, entity_list: list[tuple[Base_File, bool]]) -> list[Ginfork_File]:
        ginfork_file_list = list[Ginfork_File]()

        for entity in entity_list:
            file = entity[0]
            experimentPackageFlag = entity[1]
            ginfork_file = self.convert_to_ginfork(file=file, experimentPackageFlag=experimentPackageFlag)
            ginfork_file_list.append(ginfork_file)

        return ginfork_file_list

    def creata_common_props(self,
                            name: str,
                            contentSize: str,
                            sdDatePublished: str,
                            encodingFormat: str,
                            sha256: str,
                            url: str,
                            ) -> dict[str, Any]:
        '''
        File の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()
        if name:
            props["name"] = name

        if contentSize:
            props["contentSize"] = contentSize + 'B'

        if sdDatePublished:
            props["sdDatePublished"] = sdDatePublished

        # mime-type で 'x-'が含まれる場合はencodingFormatの設定をしない。
        if encodingFormat and 'x-' not in encodingFormat:
            props["encodingFormat"] = encodingFormat

        if sha256:
            props["sha256"] = sha256

        if url:
            props["url"] = url


        return props

    def get_common_props(self, entity: Base_File) -> dict[str, Any]:
        common_props = dict[str, Any]()

        data = entity.data

        name = data["name"]
        common_props["name"] = name

        contentSize =data["contentSize"]
        common_props["contentSize"] = contentSize

        if "sdDatePublished" in data:
            common_props["sdDatePublished"] = data["sdDatePublished"]

        if "encodingFormat" in data:
            common_props["encodingFormat"] = data["encodingFormat"]

        if "sha256" in data:
            common_props["sha256"] = data["sha256"]

        if "url" in data:
            common_props["url"] = data["url"]

        return common_props

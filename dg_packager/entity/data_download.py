
from typing import Any
from nii_dg.schema.base import DataDownload as Base_DataDownload


class DataDownloadEntity:
    '''
    DataDownloadEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_DataDownload:
        '''
        base の DataDownload インスタンスの生成メソッド
        '''
        return Base_DataDownload(id_=id, props=common_props)

    def creata_common_props(self,
                            description: str,
                            sha256: str,
                            uploadDate: str,
                            ) -> dict[str, Any]:
        '''
        DataDownload の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()

        if description:
            props["description"] = description

        if sha256:
            props["sha256"] = sha256

        if uploadDate:
            props["uploadDate"] = uploadDate

        return props

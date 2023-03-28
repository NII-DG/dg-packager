from typing import Any
from nii_dg.schema.base import RepositoryObject as Base_RepositoryObject


class RepositoryObjectEntity:
    '''
    RepositoryObjectEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_RepositoryObject:
        '''
        base の RepositoryObject インスタンスの生成メソッド
        '''
        return Base_RepositoryObject(id_=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            description: str,
                            ) -> dict[str, Any]:
        '''
        RepositoryObject の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()
        if name:
            props["name"] = name

        if description:
            props["description"] = description

        return props

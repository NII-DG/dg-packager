from typing import Any
from nii_dg.schema.base import License as Base_License


class LicenseEntity:
    '''
    LicenseEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_License:
        '''
        base の License インスタンスの生成メソッド
        '''
        return Base_License(id=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            description: str,
                            ) -> dict[str, Any]:
        '''
        License の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()

        if name:
            props["name"] = name

        if description:
            props["description"] = description

        return props

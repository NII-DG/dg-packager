from typing import Any
from nii_dg.schema.base import Organization as Base_Organization


class OrganizationEntity:
    '''
    OrganizationEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_base(self, id: str, common_props: dict[str, Any]) -> Base_Organization:
        '''
        base の Organization インスタンスの生成メソッド
        '''
        return Base_Organization(id_=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            alias: str,
                            description: str
                            ) -> dict[str, Any]:
        '''
        Organization の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()
        if name:
            props["name"] = name

        if alias:
            props["alias"] = alias

        if description:
            props["description"] = description

        return props

    def generate_empty_base(self) -> Base_Organization:
        return Base_Organization("")

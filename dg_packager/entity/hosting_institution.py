from typing import Any
from nii_dg.schema.base import HostingInstitution as Base_HostingInstitution


class HostingInstitutionEntity:
    '''
    HostingInstitutionEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_HostingInstitution:
        '''
        base の HostingInstitution インスタンスの生成メソッド
        '''
        return Base_HostingInstitution(id=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            address: str,
                            description: str,
                            ) -> dict[str, Any]:
        '''
        HostingInstitution の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()

        if name :
            props["name"] = name

        if address:
            props["address"] = address

        if description:
            props["description"] = description

        return props

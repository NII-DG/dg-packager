from typing import Any
from nii_dg.schema.amed import ClinicalResearchRegistration as Amed_ClinicalResearchRegistration


class ClinicalResearchRegistrationEntity:
    '''
    ClinicalResearchRegistrationEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_amed(self,
                      id: str,
                      common_props: dict[str, Any],
                      ) -> Amed_ClinicalResearchRegistration:
        '''
        amed の ClinicalResearchRegistration インスタンスの生成メソッド
        '''
        props = common_props
        return Amed_ClinicalResearchRegistration(id=id, props=props)

    def creata_common_props(self,
                            name: str,
                            value: str,
                            ) -> dict[str, Any]:
        '''
        ClinicalResearchRegistration の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()
        if name:
            props["name"] = name

        if value:
            props["value"] = value

        return props

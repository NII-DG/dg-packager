from typing import Any
from dg_packager.utils.enum.property_type import PropertyType as pt
from dg_packager.error.error import EntityParameterError
from nii_dg.schema.base import ContactPoint as Base_ContactPoint


class ContactPointEntity:
    '''
    ContactPointEntity クラス
    '''

    def __init__(self):
        '''
        コンストラクタ
        '''

    def generate_base(self,
                      common_props: dict[str, Any]
                      ) -> Base_ContactPoint:
        '''
        base の DataDownload インスタンスの生成メソッド
        '''
        id = self.get_id(common_props=common_props)
        return Base_ContactPoint(id=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            email: str = "",
                            telephone: str = "",
                            ) -> dict[str, Any]:
        '''
        ContactPoint の共通プロパティをdict型で取得するメソッド
        '''
        props = dict[str, Any]()

        if name:
            props["name"] = name

        if email and not telephone:
            # email有り と telephone無しの場合
            props["email"] = email
        elif not email and telephone:
            # email無し と telephone有りの場合
            props["telephone"] = telephone
        elif email and telephone:
            # email と telephoneを両方ある場合
            raise EntityParameterError('ContactPoint Entirty has only a property, email or telephone.')
        else:
            # email と telephoneを両方ない場合
            raise EntityParameterError('ContactPoint Entity must a property, email or telephone.')

        return props

    def get_id(self, common_props: dict[str, Any]) -> str:

        if pt.EMAIL.value in common_props:
            id = self.get_id_for_email(common_props.get(pt.EMAIL.value))
        else:
            id = self.get_id_for_telephone(common_props.get(pt.TELEPHONE.value))
        return id


    def get_id_for_email(self, email) -> str:
        return "#mailto:{}".format(email)

    def get_id_for_telephone(self, telephone) -> str:
        return "#callto:{}".format(telephone)

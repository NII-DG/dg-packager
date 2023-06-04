from typing import Any
from nii_dg.schema.base import Organization as Base_Organization


class OrganizationEntity:
    '''
    OrganizationEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_base(self, id: str, common_props: dict[str, Any]) -> Base_Organization:
        '''
        Methods for creating Organization instances of base
        '''
        return Base_Organization(id_=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            alias: str,
                            description: str
                            ) -> dict[str, Any]:
        '''
        Method to obtain common properties of Organization in dict type
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

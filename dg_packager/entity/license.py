from typing import Any
from nii_dg.schema.base import License as Base_License


class LicenseEntity:
    '''
    LicenseEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_License:
        '''
        Methods for creating License instances of base
        '''
        return Base_License(id_=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            description: str,
                            ) -> dict[str, Any]:
        '''
        Method to get common properties of License with dict type
        '''
        props = dict[str, Any]()

        if name:
            props["name"] = name

        if description:
            props["description"] = description

        return props

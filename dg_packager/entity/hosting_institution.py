from typing import Any
from nii_dg.schema.base import HostingInstitution as Base_HostingInstitution


class HostingInstitutionEntity:
    '''
    HostingInstitutionEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_HostingInstitution:
        '''
        Methods for creating HostingInstitution instances of base
        '''
        return Base_HostingInstitution(id_=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            address: str,
                            description: str,
                            ) -> dict[str, Any]:
        '''
        Method to get common properties of HostingInstitution with dict type
        '''
        props = dict[str, Any]()

        if name :
            props["name"] = name

        if address:
            props["address"] = address

        if description:
            props["description"] = description

        return props

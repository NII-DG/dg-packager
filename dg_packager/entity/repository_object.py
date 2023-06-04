from typing import Any
from nii_dg.schema.base import RepositoryObject as Base_RepositoryObject


class RepositoryObjectEntity:
    '''
    RepositoryObjectEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_RepositoryObject:
        '''
        Methods for creating RepositoryObject instances of base
        '''
        return Base_RepositoryObject(id_=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            description: str,
                            ) -> dict[str, Any]:
        '''
        Method to get common properties of RepositoryObject with dict type
        '''
        props = dict[str, Any]()
        if name:
            props["name"] = name

        if description:
            props["description"] = description

        return props

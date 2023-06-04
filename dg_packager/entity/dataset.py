from typing import Any
from nii_dg.schema.base import Dataset as Base_Dataset


class DatasetEntity:
    '''
    DatasetEntityclass
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_base(self,
                    id: str,
                    common_props: dict[str, Any]
                    ) -> Base_Dataset:
        '''
        Methods for creating DatasetEntity instances of base
        '''
        return Base_Dataset(id_=id, props=common_props)

    def creata_common_props(self,
                            name: str,
                            url: str
                            ) -> dict[str, Any]:
        props = dict[str, Any]()

        if name:
            props["name"] = name

        if url:
            props["url"] = url

        return props

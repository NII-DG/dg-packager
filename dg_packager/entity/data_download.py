
from typing import Any
from nii_dg.schema.base import DataDownload as Base_DataDownload


class DataDownloadEntity:
    '''
    DataDownloadEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_DataDownload:
        '''
        Methods for creating DataDownload instances of base
        '''
        return Base_DataDownload(id_=id, props=common_props)

    def creata_common_props(self,
                            description: str,
                            sha256: str,
                            uploadDate: str,
                            ) -> dict[str, Any]:
        '''
        Method to get common properties of DataDownload in dict type
        '''
        props = dict[str, Any]()

        if description:
            props["description"] = description

        if sha256:
            props["sha256"] = sha256

        if uploadDate:
            props["uploadDate"] = uploadDate

        return props

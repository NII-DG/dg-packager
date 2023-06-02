from typing import Any
from nii_dg.schema.amed import ClinicalResearchRegistration as Amed_ClinicalResearchRegistration


class ClinicalResearchRegistrationEntity:
    '''
    ClinicalResearchRegistrationEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_amed(self,
                      id: str,
                      common_props: dict[str, Any],
                      ) -> Amed_ClinicalResearchRegistration:
        '''
        Methods for creating ClinicalResearchRegistration instances of amed
        '''
        props = common_props
        return Amed_ClinicalResearchRegistration(id_=id, props=props)

    def creata_common_props(self,
                            name: str,
                            value: str,
                            ) -> dict[str, Any]:
        '''
        Method to get common properties of ClinicalResearchRegistration in dict type
        '''
        props = dict[str, Any]()
        if name:
            props["name"] = name

        if value:
            props["value"] = value

        return props

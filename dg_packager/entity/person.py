from typing import Any
from nii_dg.schema.base import Person as Base_Person, Organization
from nii_dg.schema.cao import Person as Cao_Person
from dg_packager.utils.enum.property_type import PropertyType
from typing import Any


class PersonEntity:
    '''
    PersonEntity class
    '''

    def __init__(self):
        '''
        constructor
        '''

    def generate_base(self,
                      id: str,
                      common_props: dict[str, Any]
                      ) -> Base_Person:
        '''
        Methods for creating Person instances of base
        '''
        return Base_Person(id_=id, props=common_props)

    def generate_cao(self,
                    id: str,
                    common_props: dict[str, Any],
                    eradResearcherNumber: str
                    ) -> Cao_Person:
        '''
        Methods for creating Person instances in cao
        '''
        props = common_props
        if eradResearcherNumber:
            props["eradResearcherNumber"] = eradResearcherNumber

        return Cao_Person(id_=id, props=props)

    def creata_common_props(self,
                            name: str,
                            affiliation: Organization,
                            email: str,
                            telephone: str,
                            alias: str,
                            ) -> dict[str, Any]:
        '''
        Method to get common properties of Person with dict type
        '''
        props = dict[str, Any]()
        if name:
            props["name"] = name

        affiliation_id = affiliation.data.get(PropertyType.ID.value)
        if affiliation_id:
            props["affiliation"] = affiliation

        if email:
            props["email"] = email

        if telephone:
            props["telephone"] = telephone

        if alias:
            props["alias"] = alias

        return props

    def generate_empty_entity_cao(self):
        return Cao_Person('')

    def generate_empty_entity_base(self):
        return Base_Person('')
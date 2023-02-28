import json
from unittest import TestCase
from dg_packager.utils.enum.entity_type import EntityType
from dg_packager.utils.enum.schema_type import SchemaType
from dg_packager.utils.ro_crate_util import RoCrateUtil

class TestRoCrateUtil(TestCase):
    # test exec : python -m unittest tests.utils.test_ro_crate_util

    def test_get_all_entity_data(self):
        f = open('./tests/test_data/ro-crate-matadata.json', 'r')
        ro_crate = json.load(f)
        f.close()
        entity_list = RoCrateUtil.get_all_entity_data_form_json(ro_crate_json=ro_crate)
        self.assertEqual(37, len(entity_list))

    def test_get_context_value(self):
        predict_result = 'https://w3id.org/ro/crate/1.1/context'
        f = open('./tests/test_data/ro-crate-matadata.json', 'r')
        ro_crate = json.load(f)
        f.close()

        context = RoCrateUtil.get_context_value_form_json(ro_crate)
        self.assertEqual(predict_result, context)

    def test_get_entity_by_type(self):
        f = open('./tests/test_data/ro-crate-matadata.json', 'r')
        ro_crate = json.load(f)
        f.close()

        '''ClinicalResearchRegistration'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.CLINICAL_RESEARCH_REGISTRATION)
        self.assertEqual(1, len(entity_list))
        '''ContactPoint'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.CONTACT_POINT)
        self.assertEqual(1, len(entity_list))
        '''CreativeWork'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.CREATIVE_WORK)
        self.assertEqual(1, len(entity_list))
        '''DataDownload'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.DATA_DOWNLOAD)
        self.assertEqual(1, len(entity_list))
        '''Dataset'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.DATASET)
        self.assertEqual(5, len(entity_list))
        '''DMP'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.DMP)
        self.assertEqual(4, len(entity_list))
        '''DMPMetadata'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.DMP_METADATA)
        self.assertEqual(3, len(entity_list))
        '''File'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.FILE)
        self.assertEqual(8, len(entity_list))
        '''GinMonitoring'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.GIN_MONITORING)
        self.assertEqual(1, len(entity_list))
        '''HostingInstitution'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.HOSTING_INSTITUTION)
        self.assertEqual(1, len(entity_list))
        '''License'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.LICENSE)
        self.assertEqual(1, len(entity_list))
        '''Person'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.PERSON)
        self.assertEqual(6, len(entity_list))
        '''Organization'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.ORGANIZATION)
        self.assertEqual(3, len(entity_list))
        '''RepositoryObject'''
        entity_list = RoCrateUtil.get_entity_by_type_form_json(ro_crate_json=ro_crate, entity_type=EntityType.REPOSITORY_OBJECT)
        self.assertEqual(1, len(entity_list))

    def test_get_entity_by_schema(self):
        f = open('./tests/test_data/ro-crate-matadata.json', 'r')
        ro_crate = json.load(f)
        f.close()

        '''base'''
        entity_list = RoCrateUtil.get_entity_by_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.BASE)
        self.assertEqual(17, len(entity_list))

        '''cao'''
        entity_list = RoCrateUtil.get_entity_by_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.CAO)
        self.assertEqual(8, len(entity_list))


        '''meti'''
        entity_list = RoCrateUtil.get_entity_by_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.METI)
        self.assertEqual(3, len(entity_list))

        '''amed'''
        entity_list = RoCrateUtil.get_entity_by_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.AMED)
        self.assertEqual(4, len(entity_list))

        '''ginfork'''
        entity_list = RoCrateUtil.get_entity_by_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.GINFORK)
        self.assertEqual(4, len(entity_list))

    def test_get_entity_by_type_and_schema(self):
        f = open('./tests/test_data/ro-crate-matadata.json', 'r')
        ro_crate = json.load(f)
        f.close()

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.GINFORK, entity_type=EntityType.FILE)
        self.assertEqual(3, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.AMED, entity_type=EntityType.FILE)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.CAO, entity_type=EntityType.FILE)
        self.assertEqual(2, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.METI, entity_type=EntityType.FILE)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.BASE, entity_type=EntityType.FILE)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.BASE, entity_type=EntityType.DMP)
        self.assertEqual(0, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.CAO, entity_type=EntityType.DMP)
        self.assertEqual(2, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.METI, entity_type=EntityType.DMP)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.AMED, entity_type=EntityType.DMP)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.BASE, entity_type=EntityType.DMP_METADATA)
        self.assertEqual(0, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.CAO, entity_type=EntityType.DMP_METADATA)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.METI, entity_type=EntityType.DMP_METADATA)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.AMED, entity_type=EntityType.DMP_METADATA)
        self.assertEqual(1, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.BASE, entity_type=EntityType.DATASET)
        self.assertEqual(5, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.CAO, entity_type=EntityType.DATASET)
        self.assertEqual(0, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.BASE, entity_type=EntityType.PERSON)
        self.assertEqual(3, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.CAO, entity_type=EntityType.PERSON)
        self.assertEqual(3, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.METI, entity_type=EntityType.PERSON)
        self.assertEqual(0, len(entity_list))

        entity_list = RoCrateUtil.get_entity_by_entity_and_schema_form_json(ro_crate_json=ro_crate, schema_type=SchemaType.AMED, entity_type=EntityType.PERSON)
        self.assertEqual(0, len(entity_list))

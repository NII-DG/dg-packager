


from unittest import TestCase
import json
import logging
from dg_packager.error.error import ParameterError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from dg_packager.ro_generator.gin_ro_generator import RoGenerator


class TestRoGenerator(TestCase):
    # test exec : python -m unittest tests.ro_generator.test_gin_ro_generator
    def test_check_key_raw_metadata_with_key(self):
        test_data = {
            "research_project" : {},
            "funder_orgs": [],
            "research_orgs": [],
            "licenses": [],
            "data_downloads": [],
            "repository_objs": [],
            "hosting_institutions": [],
            "persons": [],
            "files": [],
            "datasets": [],
            "gin_monitorings": [],
            "dmps": []
        }

        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_raw_metadata()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_raw_metadata_without_key(self):
        test_data = dict()

        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_raw_metadata()
        self.assertEqual(12, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_raw_metadata_invaild_type_key(self):
        test_data = dict()
        test_data = {
            "research_project" : None,
            "funder_orgs": None,
            "research_orgs": None,
            "licenses": None,
            "data_downloads": None,
            "repository_objs": None,
            "hosting_institutions": None,
            "persons": None,
            "files": None,
            "datasets": None,
            "gin_monitorings": None,
            "dmps": None,
        }

        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_raw_metadata()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(12, len(invaid_type_list))

    def test_check_key_research_project_with_key(self):
        test_data = {
            "research_project" : {
                "name": "",
                "description": ""
            }
        }

        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_research_project()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_research_project_without_key(self):
        test_data = test_data = {
            "research_project" : dict()
        }

        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_research_project()

        self.assertEqual(2, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_research_project_invaild_type_key(self):
        test_data = test_data = {
            "research_project" : {
                "name": None,
                "description": None
            }
        }

        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_research_project()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(2, len(invaid_type_list))

    def test_check_key_funder_orgs_with_key(self):
        test_data = {
            "funder_orgs" : [
                {
                    "type": "",
                    "@id": "",
                    "name" : "",
                    "alias" : "",
                    "description" : "",
                },
                {
                    "type": "",
                    "@id": "",
                    "name" : "",
                    "alias" : "",
                    "description" : "",
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_funder_orgs()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_funder_orgs_without_key(self):

        test_data = {
            "funder_orgs" : [
                    dict(),
                    {
                        "type": None,
                        "@id": None,
                        "name" : None,
                        "alias" : None,
                        "description" : None
                    },
                    "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_funder_orgs()
        self.assertEqual(5, len(absence_list))
        self.assertEqual(6, len(invaid_type_list))

    def test_check_key_research_orgs_with_key(self):
        test_data = {
            "research_orgs" : [
                {
                    "@id": "",
                    "name" : "",
                    "alias" : "",
                    "description" : "",
                },
                {
                    "@id": "",
                    "name" : "",
                    "alias" : "",
                    "description" : ""
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_research_orgs()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_research_orgs_without_key(self):

        test_data = {
            "research_orgs" : [
                    dict(),
                    {
                        "@id": None,
                        "name" : None,
                        "alias" : None,
                        "description" : None
                    },
                    ""
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_research_orgs()
        self.assertEqual(4, len(absence_list))
        self.assertEqual(5, len(invaid_type_list))


    def test_check_key_licenses_with_key(self):
        test_data = {
            "licenses" : [
                {
                    "@id": "",
                    "name" : "",
                    "description" : "",
                },
                {
                    "@id": "",
                    "name" : "",
                    "description" : ""
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_licenses()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_licenses_without_key(self):

        test_data = {
            "licenses" : [
                    dict(),
                    {
                        "@id": None,
                        "name" : None,
                        "description" : None
                    },
                    "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_licenses()
        self.assertEqual(3, len(absence_list))
        self.assertEqual(4, len(invaid_type_list))

    def test_check_key_data_downloads_with_key(self):
        test_data = {
            "data_downloads" : [
                {
                    "@id": "",
                    "description" : "",
                    "sha256" : "",
                    "uploadDate" : "",
                },
                {
                    "@id": "",
                    "description" : "",
                    "sha256" : "",
                    "uploadDate" : "",
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_data_downloads()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_data_downloads_without_key(self):

        test_data = {
            "data_downloads" : [
                    dict(),
                    {
                    "@id": None,
                    "description" : None,
                    "sha256" : None,
                    "uploadDate" : None,
                },
                    "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_data_downloads()
        self.assertEqual(4, len(absence_list))
        self.assertEqual(5, len(invaid_type_list))

    def test_check_key_repository_objs_with_key(self):
        test_data = {
            "repository_objs" : [
                {
                    "@id": "",
                    "name" : "",
                    "description" : "",
                },
                {
                    "@id": "",
                    "name" : "",
                    "description" : ""
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_repository_objs()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_repository_objs_without_key(self):

        test_data = {
            "repository_objs" : [
                    dict(),
                    {
                        "@id": None,
                        "name" : None,
                        "description" : None
                    },
                    "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_repository_objs()

        self.assertEqual(3, len(absence_list))
        self.assertEqual(4, len(invaid_type_list))


    def test_check_key_hosting_institutions_with_key(self):
        test_data = {
            "hosting_institutions" : [
                {
                    "@id": "",
                    "name" :"",
                    "description" :"",
                    "address" : "",
                },
                {
                    "@id": "",
                    "name" : "",
                    "description" : "",
                    "address" : "",
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_hosting_institutions()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_hosting_institutions_without_key(self):

        test_data = {
            "hosting_institutions" : [
                    dict(),
                    {
                    "@id": None,
                    "name" : None,
                    "description" : None,
                    "address" : None,
                },
                    "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_hosting_institutions()

        self.assertEqual(4, len(absence_list))
        self.assertEqual(5, len(invaid_type_list))


    def test_check_key_persons_with_key(self):
        test_data = {
            "persons" : [
                {
                    "id": "",
                    "url": "",
                    "name": "",
                    "alias":"",
                    "affiliation": "",
                    "email":"",
                    "telephone": "",
                    "eradResearcherNumber": "",
                },
                {
                    "id":"",
                    "url": "",
                    "name": "",
                    "alias":"",
                    "affiliation":"",
                    "email": "",
                    "telephone": "",
                    "eradResearcherNumber":"",
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_persons()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_persons_without_key(self):

        test_data = {
            "persons" : [
                dict(),
                {
                    "id": None,
                    "url": None,
                    "name": None,
                    "alias":None,
                    "affiliation": None,
                    "email":None,
                    "telephone": None,
                    "eradResearcherNumber": None,
                },
                "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_persons()
        self.assertEqual(8, len(absence_list))
        self.assertEqual(9, len(invaid_type_list))


    def test_check_key_files_with_key(self):
        test_data = {
            "files" : [
                {
                    "@id": "",
                    "name":  "",
                    "contentSize":  "0",
                    "encodingFormat":  "",
                    "sha256":  "",
                    "url": "",
                    "sdDatePublished":  "",
                    "experimentPackageFlag":  False,
                },
                {
                    "@id": "",
                    "name": "",
                    "contentSize":  "0",
                    "encodingFormat":  "",
                    "sha256": "",
                    "url":"",
                    "sdDatePublished": "",
                    "experimentPackageFlag": True,
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_files()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))


    def test_check_key_files_without_key(self):

        test_data = {
            "files" : [
                dict(),
                {
                    "@id": None,
                    "name":  None,
                    "contentSize":  None,
                    "encodingFormat":  None,
                    "sha256":  None,
                    "url": None,
                    "sdDatePublished":  None,
                    "experimentPackageFlag":  None,
                },
                "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_files()

        self.assertEqual(8, len(absence_list))
        self.assertEqual(9, len(invaid_type_list))

    def test_check_key_datasets_with_key(self):
        test_data = {
            "datasets" : [
                {
                    "@id": "",
                    "name":  "",
                    "url": "",
                },
                {
                    "@id": "",
                    "name": "",
                    "url": "",
                },
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_datasets()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_datasets_without_key(self):

        test_data = {
            "datasets" : [
                dict(),
                {
                    "@id": None,
                    "name":  None,
                    "url": None,
                },
                "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_datasets()

        self.assertEqual(3, len(absence_list))
        self.assertEqual(4, len(invaid_type_list))

    def test_check_key_gin_monitorings_with_key(self):
        test_data = {
            "gin_monitorings" : [
                {
                    "contentSize":  "",
                    "workflowIdentifier": "",
                    "datasetStructure": "",
                },
                {
                    "contentSize": "",
                    "workflowIdentifier": "",
                    "datasetStructure": "",
                },
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_gin_monitorings()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))

    def test_check_key_gin_monitorings_without_key(self):

        test_data = {
            "gin_monitorings" : [
                dict(),
                {
                    "contentSize":  None,
                    "workflowIdentifier": None,
                    "datasetStructure": None,
                },
                "",
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list = ro_gnt.check_key_gin_monitorings()

        self.assertEqual(3, len(absence_list))
        self.assertEqual(4, len(invaid_type_list))


    def test_check_key_dmps_with_key_for_cao(self):
        test_data = {
            "dmps" : [
                {
                    "type": "cao",
                    "repository": "",
                    "distribution": "",
                    "keyword": "",
                    "eradProjectId": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "creator" : [
                                ""
                            ],
                            "keyword" : "",
                            "accessRights" : "",
                            "availabilityStarts" : "",
                            "isAccessibleForFree" : "",
                            "accessRights" : "",
                            "usageInfo" : "",
                            "license" : "",
                            "repository" : "",
                            "distribution" : "",
                            "contentSize" : "",
                            "hostingInstitution" : "",
                            "dataManager" : "",
                            "related_data" : [
                                {
                                    "@id": "",
                                    "name": "",
                                    "contentSize":  "0",
                                    "encodingFormat":  "",
                                    "sha256": "",
                                    "url":"",
                                    "sdDatePublished": "",
                                }
                            ],
                        }
                    ],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()


        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

    def test_check_key_dmps_invalid_for_cao(self):
        test_data = {
            "dmps" : [
                {
                    "type": None,
                    "repository": None,
                    "distribution": None,
                    "keyword": None,
                    "eradProjectId": None,
                    "hasPart": ""
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(2, len(invaid_type_list))
        self.assertEqual(1, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "cao",
                    "repository": None,
                    "distribution": None,
                    "keyword": None,
                    "eradProjectId": None,
                    "hasPart": []
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(4, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(2, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "cao",
                    "hasPart": []
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(4, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        # cao.dmps.hasPart
        test_data = {
            "dmps" : [
                {
                    "type": "cao",
                    "repository": "",
                    "distribution": "",
                    "keyword": "",
                    "eradProjectId": "",
                    "hasPart": [
                        {
                        }
                    ]
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(15, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "cao",
                    "repository": "",
                    "distribution": "",
                    "keyword": "",
                    "eradProjectId": "",
                    "hasPart": [
                        {
                            "name" : None,
                            "description" : None,
                            "creator" : None,
                            "keyword" : None,
                            "accessRights" : None,
                            "availabilityStarts" : None,
                            "isAccessibleForFree" : None,
                            "license" : None,
                            "usageInfo" : None,
                            "repository" : None,
                            "distribution" : None,
                            "contentSize" : None,
                            "hostingInstitution" : None,
                            "dataManager" : None,
                            "related_data" : None,
                        }
                    ]
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(15, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "cao",
                    "repository": "",
                    "distribution": "",
                    "keyword": "",
                    "eradProjectId": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "creator" : [0],
                            "keyword" : "",
                            "accessRights" : "",
                            "availabilityStarts" : "",
                            "isAccessibleForFree" : "",
                            "license" : "",
                            "usageInfo" : "",
                            "repository" : "",
                            "distribution" : "",
                            "contentSize" : "",
                            "hostingInstitution" : "",
                            "dataManager" : "",
                            "related_data" : [ ""
                            ]
                        }
                    ]
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(2, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "cao",
                    "repository": "",
                    "distribution": "",
                    "keyword": "",
                    "eradProjectId": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "creator" : [""],
                            "keyword" : "",
                            "accessRights" : "",
                            "availabilityStarts" : "",
                            "isAccessibleForFree" : "",
                            "license" : "",
                            "usageInfo" : "",
                            "repository" : "",
                            "distribution" : "",
                            "contentSize" : "",
                            "hostingInstitution" : "",
                            "dataManager" : "",
                            "related_data" : [
                                {

                                },
                                {
                                    "@id": None,
                                    "name": None,
                                    "contentSize":  None,
                                    "encodingFormat":  None,
                                    "sha256": None,
                                    "url":None,
                                    "sdDatePublished": None,
                                }
                            ]
                        }
                    ]
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(7, len(absence_list))
        self.assertEqual(7, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

    def test_check_key_dmps_with_key_for_meti(self):
        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "creator": [""],
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "hostingInstitution" : "",
                            "wayOfManage" : "",
                            "accessRights" : "",
                            "reasonForConcealment" : "",
                            "availabilityStarts" : "",
                            "accessRights" : "",
                            "creator" : [""],
                            "measurementTechnique" : "",
                            "isAccessibleForFree" : "",
                            "license" : "",
                            "usageInfo" : "",
                            "repository" : "",
                            "contentSize" : "",
                            "distribution" : "",
                            "contactPoint" : {
                                "name" : "",
                                "email" : "",
                                "telephone" : "",
                            },
                            "related_data" : [
                                {
                                    "@id": "",
                                    "name": "",
                                    "contentSize":  "0",
                                    "encodingFormat":  "",
                                    "sha256": "",
                                    "url":"",
                                    "sdDatePublished": "",
                                }
                            ],
                        }
                    ],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()


        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

    def test_check_key_dmps_invalid_for_meti(self):
        test_data = {
                "dmps" : [
                    {
                        "type": None,
                        "creator": "",
                        "repository": None,
                        "distribution": None,
                        "hasPart": "",
                    },

                ]
            }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()

        self.assertEqual(0, len(absence_list))
        self.assertEqual(2, len(invaid_type_list))
        self.assertEqual(1, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "creator": None,
                    "repository": None,
                    "distribution": None,
                    "hasPart": [],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()


        self.assertEqual(0, len(absence_list))
        self.assertEqual(3, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "hasPart": []
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()

        self.assertEqual(3, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "creator": [0],
                    "repository": "",
                    "distribution": "",
                    "hasPart": [""],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(2, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "creator": [""],
                    "repository": "",
                    "distribution": "",
                    "hasPart": [{}],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(17, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "creator": [""],
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                        {
                            "name" : None,
                            "description" : None,
                            "hostingInstitution" : None,
                            "wayOfManage" : None,
                            "accessRights" :None,
                            "reasonForConcealment" : None,
                            "availabilityStarts" : None,
                            "accessRights" : None,
                            "creator" : None,
                            "measurementTechnique" : None,
                            "isAccessibleForFree" : None,
                            "license" :None,
                            "usageInfo" : None,
                            "repository" : None,
                            "contentSize" : None,
                            "distribution" : None,
                            "contactPoint" : [],
                            "related_data" : None,
                        }
                    ],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(17, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "creator": [""],
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "hostingInstitution" : "",
                            "wayOfManage" : "",
                            "accessRights" :"",
                            "reasonForConcealment" : "",
                            "availabilityStarts" : "",
                            "accessRights" : "",
                            "creator" : [0],
                            "measurementTechnique" : "",
                            "isAccessibleForFree" : "",
                            "license" :"",
                            "usageInfo" : "",
                            "repository" : "",
                            "contentSize" : "",
                            "distribution" : "",
                            "contactPoint" : {
                                "name" :None,
                                "email" : None,
                                "telephone" :None,
                            },
                            "related_data" : [
                                "",
                                {

                                },
                                {
                                    "@id": None,
                                    "name": None,
                                    "contentSize":  None,
                                    "encodingFormat":  None,
                                    "sha256": None,
                                    "url":None,
                                    "sdDatePublished": None,
                                }
                            ]
                        }
                    ],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(7, len(absence_list))
        self.assertEqual(12, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "meti",
                    "creator": [""],
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "hostingInstitution" : "",
                            "wayOfManage" : "",
                            "accessRights" :"",
                            "reasonForConcealment" : "",
                            "availabilityStarts" : "",
                            "accessRights" : "",
                            "creator" : [""],
                            "measurementTechnique" : "",
                            "isAccessibleForFree" : "",
                            "license" :"",
                            "usageInfo" : "",
                            "repository" : "",
                            "contentSize" : "",
                            "distribution" : "",
                            "contactPoint" : {

                            },
                            "related_data" : [
                                {
                                    "@id": "",
                                    "name": "",
                                    "contentSize":  "0",
                                    "encodingFormat":  "",
                                    "sha256": "",
                                    "url":"",
                                    "sdDatePublished": "",
                                }
                            ],
                        }
                    ],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()

        self.assertEqual(3, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

    def test_check_key_dmps_with_key_for_amed(self):
        test_data = {
            "dmps" : [
                {
                    "type": "amed",
                    "funding": "",
                    "chiefResearcher": "",
                    "creator": [""],
                    "hostingInstitution": "",
                    "dataManager": "",
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "keyword" : "",
                            "accessRights" : "",
                            "availabilityStarts" : "",
                            "reasonForConcealment" : "",
                            "repository" : "",
                            "distribution" : "",
                            "contentSize" : "",
                            "gotInformedConsent" : "",
                            "informedConsentFormat" : "",
                            "identifier" : [
                                {
                                    "@id" : "",
                                    "name" : "",
                                    "value" : "",
                                }
                            ],
                            "related_data" : [
                                {
                                    "@id": "",
                                    "name": "",
                                    "contentSize":  "0",
                                    "encodingFormat":  "",
                                    "sha256": "",
                                    "url":"",
                                    "sdDatePublished": "",
                                }
                            ],
                        }
                    ],
                },

            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()

        for index in range(len(absence_list)):
            print(f'[{index}] : {[absence_list[index]]}')
        self.assertEqual(0, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

    def test_check_key_dmps_invalid_for_amed(self):
        test_data = {
            "dmps" : [
                {
                    "type": None,
                    "funding": None,
                    "chiefResearcher": None,
                    "creator": None,
                    "hostingInstitution": None,
                    "dataManager": None,
                    "repository": None,
                    "distribution": None,
                    "hasPart": None,
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(2, len(invaid_type_list))
        self.assertEqual(1, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "amed",
                    "funding": None,
                    "chiefResearcher": None,
                    "creator": None,
                    "hostingInstitution": None,
                    "dataManager": None,
                    "repository": None,
                    "distribution": None,
                    "hasPart": [],
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(7, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "amed",
                    "hasPart": [],
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(7, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "amed",
                    "funding": "",
                    "chiefResearcher": "",
                    "creator": [0],
                    "hostingInstitution": "",
                    "dataManager": "",
                    "repository": "",
                    "distribution": "",
                    "hasPart": [""],
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(2, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "amed",
                    "funding": "",
                    "chiefResearcher": "",
                    "creator": [""],
                    "hostingInstitution": "",
                    "dataManager": "",
                    "repository": "",
                    "distribution": "",
                    "hasPart": [{}],
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(13, len(absence_list))
        self.assertEqual(0, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "amed",
                    "funding": "",
                    "chiefResearcher": "",
                    "creator": [""],
                    "hostingInstitution": "",
                    "dataManager": "",
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                                                {
                            "name" : None,
                            "description" : None,
                            "keyword" : None,
                            "accessRights" : None,
                            "availabilityStarts" : None,
                            "reasonForConcealment" :None,
                            "repository" : None,
                            "distribution" :None,
                            "contentSize" : None,
                            "gotInformedConsent" : None,
                            "informedConsentFormat" : None,
                            "identifier" : None,
                            "related_data" :None,
                        }
                    ],
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(0, len(absence_list))
        self.assertEqual(13, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

        test_data = {
            "dmps" : [
                {
                    "type": "amed",
                    "funding": "",
                    "chiefResearcher": "",
                    "creator": [""],
                    "hostingInstitution": "",
                    "dataManager": "",
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                                                {
                            "name" : "",
                            "description" : "",
                            "keyword" : "",
                            "accessRights" : "",
                            "availabilityStarts" : "",
                            "reasonForConcealment" :"",
                            "repository" : "",
                            "distribution" :"",
                            "contentSize" : "",
                            "gotInformedConsent" : "",
                            "informedConsentFormat" : "",
                            "identifier" : [
                                "",
                                {},
                                {
                                    "@id" : None,
                                    "name" : None,
                                    "value" : None,
                                }
                            ],
                            "related_data" : [
                                "",
                                {

                                },
                                {
                                    "@id": None,
                                    "name": None,
                                    "contentSize":  None,
                                    "encodingFormat":  None,
                                    "sha256": None,
                                    "url":None,
                                    "sdDatePublished": None,
                                }
                            ],
                        }
                    ],
                }
            ]
        }
        ro_gnt = RoGenerator(raw_metadata=test_data)
        absence_list, invaid_type_list, invalid_value_list = ro_gnt.check_key_dmps()
        self.assertEqual(10, len(absence_list))
        self.assertEqual(12, len(invaid_type_list))
        self.assertEqual(0, len(invalid_value_list))

    def test_check_key_all(self):
        test_data = {
            "research_project" : {
                "name": "",
                "description": ""
            },
            "funder_orgs": [{
                    "type": "",
                    "@id": "",
                    "name" : "",
                    "alias" : "",
                    "description" : "",
                },],
            "research_orgs": [{
                    "@id": "",
                    "name" : "",
                    "alias" : "",
                    "description" : "",
                },],
            "licenses": [{
                    "@id": "",
                    "name" : "",
                    "description" : "",
                },],
            "data_downloads": [{
                    "@id": "",
                    "description" : "",
                    "sha256" : "",
                    "uploadDate" : "",
                },],
            "repository_objs": [{
                    "@id": "",
                    "name" : "",
                    "description" : "",
                },],
            "hosting_institutions": [{
                    "@id": "",
                    "name" :"",
                    "description" :"",
                    "address" : "",
                },],
            "persons": [{
                    "id": "",
                    "url": "",
                    "name": "",
                    "alias":"",
                    "affiliation": "",
                    "email":"",
                    "telephone": "",
                    "eradResearcherNumber": "",
                },],
            "files": [{
                    "@id": "",
                    "name":  "",
                    "contentSize":  "0",
                    "encodingFormat":  "",
                    "sha256":  "",
                    "url": "",
                    "sdDatePublished":  "",
                    "experimentPackageFlag":  False,
                },],
            "datasets": [{
                    "@id": "",
                    "name":  "",
                    "url": "",
                },],
            "gin_monitorings": [{
                    "contentSize":  "",
                    "workflowIdentifier": "",
                    "datasetStructure": "",
                },],
            "dmps": [
                {
                    "type": "cao",
                    "repository": "",
                    "distribution": "",
                    "keyword": "",
                    "eradProjectId": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "creator" : [
                                ""
                            ],
                            "keyword" : "",
                            "accessRights" : "",
                            "availabilityStarts" : "",
                            "isAccessibleForFree" : "",
                            "accessRights" : "",
                            "usageInfo" : "",
                            "license" : "",
                            "repository" : "",
                            "distribution" : "",
                            "contentSize" : "",
                            "hostingInstitution" : "",
                            "dataManager" : "",
                            "related_data" : [
                                {
                                    "@id": "",
                                    "name": "",
                                    "contentSize":  "0",
                                    "encodingFormat":  "",
                                    "sha256": "",
                                    "url":"",
                                    "sdDatePublished": "",
                                }
                            ],
                        }
                    ],
                },
                {
                    "type": "meti",
                    "creator": [""],
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "hostingInstitution" : "",
                            "wayOfManage" : "",
                            "accessRights" : "",
                            "reasonForConcealment" : "",
                            "availabilityStarts" : "",
                            "accessRights" : "",
                            "creator" : [""],
                            "measurementTechnique" : "",
                            "isAccessibleForFree" : "",
                            "license" : "",
                            "usageInfo" : "",
                            "repository" : "",
                            "contentSize" : "",
                            "distribution" : "",
                            "contactPoint" : {
                                "name" : "",
                                "email" : "",
                                "telephone" : "",
                            },
                            "related_data" : [
                                {
                                    "@id": "",
                                    "name": "",
                                    "contentSize":  "0",
                                    "encodingFormat":  "",
                                    "sha256": "",
                                    "url":"",
                                    "sdDatePublished": "",
                                }
                            ],
                        }
                    ],
                },
                {
                    "type": "amed",
                    "funding": "",
                    "chiefResearcher": "",
                    "creator": [""],
                    "hostingInstitution": "",
                    "dataManager": "",
                    "repository": "",
                    "distribution": "",
                    "hasPart": [
                        {
                            "name" : "",
                            "description" : "",
                            "keyword" : "",
                            "accessRights" : "",
                            "availabilityStarts" : "",
                            "reasonForConcealment" : "",
                            "repository" : "",
                            "distribution" : "",
                            "contentSize" : "",
                            "gotInformedConsent" : "",
                            "informedConsentFormat" : "",
                            "identifier" : [
                                {
                                    "@id" : "",
                                    "name" : "",
                                    "value" : "",
                                }
                            ],
                            "related_data" : [
                                {
                                    "@id": "",
                                    "name": "",
                                    "contentSize":  "0",
                                    "encodingFormat":  "",
                                    "sha256": "",
                                    "url":"",
                                    "sdDatePublished": "",
                                }
                            ],
                        }
                    ],
                },
            ]
        }

        try:
            ro_gnt = RoGenerator(raw_metadata=test_data)
            ro_gnt.check_key()
        except ParameterError as e:
            error_dict = e.get_msg_for_check_key()
            for key in error_dict.keys():
                print(f'{key} : {error_dict.get(key)}')
            self.fail()

    def test_check_key_empty(self):
        test_data = {
        }

        try:
            ro_gnt = RoGenerator(raw_metadata=test_data)
            ro_gnt.check_key()
        except ParameterError as e:
            error_dict = e.get_msg_for_check_key()
            error_list = error_dict['required_key']
            self.assertEqual(12, len(error_list))

    def test_check_key_all_invalid(self):
        test_data = {
            "research_project" : { # no_key 2 OK
            },
            "funder_orgs": [
                { # no_key 5 OK

                },
                { # invaid_type 5 OK
                    "type": None,
                    "@id": None,
                    "name" : None,
                    "alias" : None,
                    "description" : None,
                },
                "" # invaid_type 1 OK
            ],
            "research_orgs": [
                {}, # no_key 4 OK
                { # invaid_type 4 OK
                    "@id": None,
                    "name" : None,
                    "alias" : None,
                    "description" : None,
                },
                "" # invaid_type 1 OK
            ],
            "licenses": [
                {}, # no_key 3 OK
                { # invaid_type 3
                    "@id":  None,
                    "name" :  None,
                    "description" :  None,
                },
                "" # invaid_type 1
            ],
            "data_downloads": [
                {}, # no_key 4 OK
                { # invaid_type 4
                    "@id": None,
                    "description" : None,
                    "sha256" : None,
                    "uploadDate" : None,
                },
                "" # invaid_type 1
            ],
            "repository_objs": [
                {}, # no_key 3 OK
                { # invaid_type 3 OK
                    "@id": None,
                    "name" : None,
                    "description" : None,
                },
                "" # invaid_type 1 OK
            ],
            "hosting_institutions": [
                {}, # no_key 4 OK
                { # invaid_type 4 OK
                    "@id": None,
                    "name" :None,
                    "description" :None,
                    "address" : None,
                },
                "" # invaid_type 1 OK
            ],
            "persons": [
                {}, # no_key 8 OK
                { # invaid_type 8 OK
                    "id": None,
                    "url": None,
                    "name": None,
                    "alias":None,
                    "affiliation": None,
                    "email":None,
                    "telephone": None,
                    "eradResearcherNumber": None,
                },
                "" # invaid_type 1 OK
            ],
            "files": [
                {}, # no_key 8 OK
                { # invaid_type 8
                    "@id": None,
                    "name":  None,
                    "contentSize":  None,
                    "encodingFormat":  None,
                    "sha256":  None,
                    "url": None,
                    "sdDatePublished":  None,
                    "experimentPackageFlag":  None,
                },
                "" # invaid_type 1
            ],
            "datasets": [
                {}, # no_key 3 OK
                { # invaid_type 3 Ok
                    "@id": None,
                    "name":  None,
                    "url": None,
                },
                "" # invaid_type 1 OK
            ],
            "gin_monitorings": [
                {}, # no_key 3 OK
                { # invaid_type 3 OK
                    "contentSize":  None,
                    "workflowIdentifier": None,
                    "datasetStructure": None,
                },
                "" # invaid_type 1 OK
            ],
            "dmps": [
                "", # invaid_type 1 OK
                { # invaid_type 4 OK
                    "type": "cao",
                    "repository": None,
                    "distribution": None,
                    "keyword": None,
                    "eradProjectId": None,
                    "hasPart": [
                        { # invaid_type 14 OK
                            "name" : None,
                            "description" : None,
                            "creator" :  None,
                            "keyword" : None,
                            "accessRights" : None,
                            "availabilityStarts" : None,
                            "isAccessibleForFree" : None,
                            "usageInfo" : None,
                            "license" : None,
                            "repository" : None,
                            "distribution" : None,
                            "contentSize" : None,
                            "hostingInstitution" : None,
                            "dataManager" : None,
                            "related_data" : [
                                { # invaid_type 7 OK
                                    "@id": None,
                                    "name": None,
                                    "contentSize":  None,
                                    "encodingFormat":  None,
                                    "sha256": None,
                                    "url":None,
                                    "sdDatePublished": None,
                                },
                                {}, # no_key 7 OK
                                "", # invaid_type 1 OK
                            ],
                        },
                        {}, # no_key 15 OK
                        "" # invaid_type 1 OK
                    ],
                },
                { # invaid_type 3 OK
                    "type": "meti",
                    "creator": None,
                    "repository": None,
                    "distribution": None,
                    "hasPart": [
                        { # invaid_type 15 OK
                            "name" : None,
                            "description" : None,
                            "hostingInstitution" : None,
                            "wayOfManage" : None,
                            "accessRights" : None,
                            "reasonForConcealment" : None,
                            "availabilityStarts" : None,
                            "creator" : None,
                            "measurementTechnique" : None,
                            "isAccessibleForFree" : None,
                            "license" : None,
                            "usageInfo" : None,
                            "repository" : None,
                            "contentSize" : None,
                            "distribution" : None,
                            "contactPoint" : { # invaid_type 3 OK
                                "name" : None,
                                "email" : None,
                                "telephone" : None,
                            },
                            "related_data" : [
                                { # invaid_type 7 OK
                                    "@id": None,
                                    "name": None,
                                    "contentSize":  None,
                                    "encodingFormat":  None,
                                    "sha256": None,
                                    "url":None,
                                    "sdDatePublished": None,
                                },
                                {}, # no_key 7 OK
                                "",  # invaid_type 1
                            ],
                        },
                        {},# no_key 17 OK
                        "", # invaid_type 1 OK
                    ],
                },
                { # invaid_type 7 OK
                    "type": "amed",
                    "funding": None,
                    "chiefResearcher": None,
                    "creator": None,
                    "hostingInstitution": None,
                    "dataManager": None,
                    "repository": None,
                    "distribution": None,
                    "hasPart": [
                        { # invaid_type 11 OK
                            "name" : None,
                            "description" : None,
                            "keyword" : None,
                            "accessRights" : None,
                            "availabilityStarts" :None,
                            "reasonForConcealment" : None,
                            "repository" : None,
                            "distribution" : None,
                            "contentSize" :None,
                            "gotInformedConsent" :None,
                            "informedConsentFormat" : None,
                            "identifier" : [
                                { # invaid_type 3 OK
                                    "@id" : None,
                                    "name" : None,
                                    "value" : None,
                                },
                                {}, # no_key 3 OK
                                "" # invaid_type 1 OK
                            ],
                            "related_data" : [
                                { # invaid_type 7 OK
                                    "@id": None,
                                    "name": None,
                                    "contentSize": None,
                                    "encodingFormat":  None,
                                    "sha256": None,
                                    "url":None,
                                    "sdDatePublished": None,
                                },
                                {},# no_key 7 OK
                                "" # invaid_type 1 OK
                            ],
                        },
                        {}, # no_key 13 OK
                        "", # invaid_type 1 OK
                    ],
                },
                { # invaid_value 1
                    "type": "invaid",
                    "funding": "",
                    "chiefResearcher": "",
                    "creator": [],
                    "hostingInstitution": "",
                    "dataManager": "",
                    "repository": "",
                    "distribution": "",
                    "hasPart": []
                }
            ]
        }

        try:
            ro_gnt = RoGenerator(raw_metadata=test_data)
            ro_gnt.check_key()
        except ParameterError as e:
            error_dict = e.get_msg_for_check_key()
            required_key = error_dict['required_key']
            self.assertEqual(116, len(required_key))

            invalid_value_type = error_dict['invalid_value_type']
            self.assertEqual(144, len(invalid_value_type))
            invalid_value = error_dict['invalid_value']
            self.assertEqual(1, len(invalid_value))

    def test_generate(self):
        file_name = 'test_generate.json'
        dir_name = './tests/test_data/'
        json_file = dir_name + file_name
        json_open = open(json_file, 'r')
        json_load = json.load(json_open)
        json_open.close()
        ro_gnt = RoGenerator(raw_metadata=json_load)

        try:
            ro_crate = ro_gnt.generate()
            print(ro_crate)
        except ParameterError as e:
            error_dict = e.get_msg_for_check_key()
            for key in error_dict.keys():
                error_list = error_dict.get(key)
                for index in range(len(error_list)):
                    print(f'{key} ; [{index:05}] : {error_list[index]}')
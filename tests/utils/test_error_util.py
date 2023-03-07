from dg_packager.error.error import JsonValidationError, RoPkgError
from unittest import TestCase
from dg_packager.utils.error_util import ErrorUtil

class TestError(TestCase):
    # test exec : python -m unittest tests.utils.test_error_util

    def test_ExtractErrMsgToDict(self):
        Expected_Value = {"result": [{"key1": "val1", "key2": "val2"}, {"key3": "val3"}]}
        err = JsonValidationError(Expected_Value)

        data = ErrorUtil.ExtractErrMsgToDict(err)
        self.assertEqual(Expected_Value, data)


        Expected_Value = {'required_key': ['invalid_key_name1', 'invalid_key_name1'], 'invalid_value_type': ['error_msg1', 'error_msg2'], 'invalid_value' :['error_msg3', 'error_msg4']}
        err = JsonValidationError(Expected_Value)

        data = ErrorUtil.ExtractErrMsgToDict(err)
        self.assertEqual(Expected_Value, data)
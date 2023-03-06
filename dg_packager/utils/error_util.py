

import json
import traceback


class ErrorUtil():

    @staticmethod
    def ExtractErrMsgToDict(e : Exception):
        t = traceback.format_exception_only(type(Exception), e)
        raw_error_msg = t[0]
        forward_index = raw_error_msg.find("{")
        backward_index = raw_error_msg.rfind("}")
        shaped = raw_error_msg[forward_index:backward_index+1].replace('\'', '\"')
        return json.loads(shaped)
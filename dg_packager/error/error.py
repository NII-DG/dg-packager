#!/usr/bin/env python3
# coding: utf-8

import traceback
import json

class NotEnoughParameterError(Exception):
    pass


class ExcessParameterError(Exception):
    pass

class EmptyStringParameterError(Exception):
    pass


class EnumValueError(Exception):
    pass

class EntityParameterError(Exception):
    pass

class ParameterError(Exception):

    def get_msg(self):
        t = traceback.format_exception_only(type(self), self)
        return t

    def get_msg_for_check_key(self):
        t = traceback.format_exception_only(type(self), self)
        raw_error_msg = t[0]
        forward_index = raw_error_msg.find("{")
        backward_index = raw_error_msg.rfind("}")
        shaped = raw_error_msg[forward_index:backward_index+1]
        return json.loads(shaped.replace('\'', '\"'))


class GitError(Exception):
    pass

class CommandError(Exception):
    pass

class NotFoundError(Exception):
    pass

class ExistError(Exception):
    pass

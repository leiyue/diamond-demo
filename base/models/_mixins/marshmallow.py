# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 21:28
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals


class MarshmallowMixin(object):
    @classmethod
    def dump_all(cls):
        return cls.__schema__().dump(cls.query.all(), many=True).data

    @classmethod
    def load_all(cls, python_objects):
        return cls.__schema__().load(python_objects, many=True).data

    # dump
    def dump(self):
        return self.__schema__().dump(self).data

    def dumps(self):
        return self.__schema__().dumps(self).data

    def dumpf(self, file_handle):
        file_handle.write(self.dumps())

    # load
    @classmethod
    def load(cls, python_obj):
        return cls.__schema__().load(python_obj).data

    @classmethod
    def loads(cls, buf):
        return cls.__schema__().loads(buf)

    @classmethod
    def loadf(cls, file_handle):
        return cls.loads(file_handle.read())

    # dump_all
    @classmethod
    def dump_all(cls):
        return cls.__schema__().dump(cls.query.all(), many=True).data

    @classmethod
    def dumps_all(cls):
        return cls.__schema__().dumps(cls.query.all(), many=True).data

    @classmethod
    def dumpf_all(cls, file_handle):
        file_handle.write(cls.dumps_all())

    # load_all
    @classmethod
    def load_all(cls, python_objects):
        return cls.__schema__().load(python_objects, many=True)

    @classmethod
    def loads_all(cls, buf):
        return cls.__schema__().loads(buf, many=True)

    @classmethod
    def loadf_all(cls, file_handle):
        cls.loads_all(file_handle.read())

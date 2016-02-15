# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 21:28
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from ... import db


class MarshmallowMixin(object):
    # dump
    def dump(self):
        return self.__schema__().dump(self).data

    def dumps(self):
        return self.__shema__().dumps(self).data

    def dumpf(self, file_handle):
        file_handle.write(self.dumps())

    # load
    @classmethod
    def load(cls, python_obj):
        obj = cls.__schema__().load(python_obj)
        return cls.create(**obj.data)

    @classmethod
    def loads(cls, buf):
        obj = cls.__schema__().loads(buf)
        return cls.create(**obj.data)

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
        objs = cls.__schema__().load(python_objects, many=True)
        for obj in objs.data:
            cls.create(_commit=True, **obj)
        db.session.commit()
        db.session.flush()

    @classmethod
    def loads_all(cls, buf):
        objs = cls.__schema__().loads(buf, many=True)
        for obj in objs.data:
            cls.create(_commit=True, **obj)
        db.session.commit()
        db.session.flush()

    @classmethod
    def loadf_all(cls, file_handle):
        cls.loads_all(file_handle.read())

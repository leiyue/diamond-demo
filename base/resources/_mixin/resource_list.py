# -*- coding: utf-8 -*-
# @Date    : 2016-02-18 1:18
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from sqlite3 import IntegrityError

from flask.ext.restful import Resource as BaseResource, abort, marshal_with


class ResourceList(BaseResource):
    def __init__(self, model, marshal_fields, parser):
        self.model = model
        self.fields = marshal_fields
        self.parser = parser

    def get(self):
        return self.model.dump_all()

    @marshal_with(marshal_fields)
    def post(self):
        args = self.parser.parse_args()
        try:
            resource = self.model.create(**args)
        except IntegrityError:
            abort(400)
        return self.model.dump(resource)

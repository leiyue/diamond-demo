# -*- coding: utf-8 -*-
# -*- date: 2016-02-17 16:37 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.restful import Resource, abort
from flask.ext.security import auth_token_required, roles_required

from .decorators import load_with, dump_with
from ..models import Role, RoleSchema

_schema = RoleSchema()
_list_schema = RoleSchema(many=True)


class RoleListResource(Resource):
    method_decorators = [auth_token_required]

    model = Role

    @dump_with(_list_schema)
    def get(self):
        instances = self.model.query.all()
        return instances

    @roles_required('Admin')
    @load_with(_schema)
    @dump_with(_schema)
    def post(self, data):
        instance = self.model.find_one(name=data['name'])
        if instance:
            abort(409, message='Resource already exists')
        instance = self.model.create(**data)
        return instance


class RoleItemResource(Resource):
    method_decorators = [auth_token_required]

    model = Role

    @dump_with(_schema)
    def get(self, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        return instance

    @roles_required('Admin')
    def delete(self, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        return instance.delete() and '', 204

    @roles_required('Admin')
    @load_with(_schema)
    @dump_with(_schema)
    def put(self, data, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        instance = instance.update(**data)
        return instance

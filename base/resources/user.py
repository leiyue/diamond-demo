# -*- coding: utf-8 -*-
# @Date    : 2016-02-17 14:51
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.restful import Resource, abort
from flask.ext.security import auth_token_required, roles_required
from flask.ext.security.utils import encrypt_password

from .decorators import load_with, dump_with
from ..models import User, UserSchema

_schema = UserSchema()
_list_schema = UserSchema(many=True)


class UserListResource(Resource):
    # method_decorators = [auth_token_required]

    model = User

    @dump_with(_list_schema)
    def get(self):
        instances = self.model.query.all()
        return instances

    # @roles_required('Admin')
    @load_with(_schema)
    @dump_with(_schema)
    def post(self, data):
        instance = self.model.find_one(email=data['email'])
        if instance:
            abort(409, message='Resource already exists')
        instance = self.model.register(confirmed=True, roles=['User'], **data)
        return instance


class UserItemResource(Resource):
    # method_decorators = [auth_token_required]

    model = User

    @dump_with(_schema)
    def get(self, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        return instance

    def delete(self, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        return instance.delete() and '', 204

    @load_with(_schema)
    @dump_with(_schema)
    def put(self, data, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')

        original_password = data['password']
        data['password'] = encrypt_password(original_password)
        instance = instance.update(**data)
        return instance

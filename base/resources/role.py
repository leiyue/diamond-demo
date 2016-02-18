# -*- coding: utf-8 -*-
# @Date    : 2016-02-17 16:37
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.restful import Resource, fields, reqparse, marshal_with, abort
from sqlalchemy.exc import IntegrityError

from ..models import Role

_role_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String
}

_parser = reqparse.RequestParser()
_parser.add_argument('name', type=str, required=True, help='Role must has a name.')
_parser.add_argument('description', type=str)


class RoleList(Resource):
    def get(self):
        return Role.dumps_all()

    @marshal_with(_role_fields)
    def post(self):
        args = _parser.parse_args()
        try:
            # role = Role.create(**args)
            role = Role.load(args)
        except IntegrityError:
            abort(400)
        return Role.dump(role)


class RoleItem(Resource):
    def get(self, role_id):
        role = Role.get_by_id(role_id)
        if role:
            return Role.dump(role)
        else:
            abort(404)

    def delete(self, role_id):
        role = Role.get_by_id(role_id)
        if role:
            return role.delete() and '', 204
        else:
            abort(404)

    @marshal_with(_role_fields)
    def put(self, role_id):
        args = _parser.parse_args()
        role = Role.get_by_id(role_id)
        if role:
            role.update(**args)
            return Role.dump(role)
        else:
            abort(404)

# -*- coding: utf-8 -*-
# @Date    : 2016-02-15 11:49
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask import Blueprint
from flask.ext.restful import Api

_errors = {
    'ResourceAlreadyExistsError': {
        'message': "A resource already exists.",
        'status': 409,
    },
    'ResourceDoesNotExistError': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}

api = Api(errors=_errors)


def init_restful(self):
    from ..resources import UserList, UserItem
    from ..resources import RoleList, RoleItem

    # Todo: think about flask-restful usage
    api.add_resource(UserList, '/api/user')
    api.add_resource(UserItem, '/api/user/<int:user_id>')
    api.add_resource(RoleList, '/api/role')
    api.add_resource(RoleItem, '/api/role/<int:role_id>')

    # api_blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(self.app)
    # self.app.register_blueprint(api_blueprint)
    return api

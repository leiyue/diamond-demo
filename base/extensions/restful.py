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
    from ..resources import UserListResource, UserItemResource
    from ..resources import RoleListResource, RoleItemResource

    # Todo: think about flask-restful usage
    api.add_resource(UserListResource, '/api/user')
    api.add_resource(UserItemResource, '/api/user/<int:instance_id>')
    api.add_resource(RoleListResource, '/api/role')
    api.add_resource(RoleItemResource, '/api/role/<int:instance_id>')

    # api_blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(self.app)
    # self.app.register_blueprint(api_blueprint)
    return api

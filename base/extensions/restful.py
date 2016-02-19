# -*- coding: utf-8 -*-
# -*- date: 2016-02-15 11:49 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

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
    api.add_resource(UserListResource, '/user')
    api.add_resource(UserItemResource, '/user/<int:instance_id>')
    api.add_resource(RoleListResource, '/role')
    api.add_resource(RoleItemResource, '/role/<int:instance_id>')

    api.init_app(self.app)
    return api

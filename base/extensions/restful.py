# -*- coding: utf-8 -*-
# -*- date: 2016-02-15 11:49 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.restful import Api

__all__ = ['api', 'init_restful']

api = Api()


def init_restful(self):
    from ..resources import UserListResource, UserItemResource
    from ..resources import RoleListResource, RoleItemResource

    api.add_resource(UserListResource, '/api/user')
    api.add_resource(UserItemResource, '/api/user/<int:instance_id>')
    api.add_resource(RoleListResource, '/api/role')
    api.add_resource(RoleItemResource, '/api/role/<int:instance_id>')

    api.init_app(self.app)
    return api

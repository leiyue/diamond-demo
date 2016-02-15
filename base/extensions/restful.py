# -*- coding: utf-8 -*-
# @Date    : 2016-02-15 11:49
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.restful import Api

api = Api()


def init_restful(self):
    from ..views import HelloWorldResource

    # Todo: think about flask-restful usage
    api.add_resource(HelloWorldResource, '/api')
    api.init_app(self.app)
    return api

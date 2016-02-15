# -*- coding: utf-8 -*-
# @Date    : 2016-02-15 11:49
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.restful import Api

restful_api = Api()


def init_restful(self):
    from ..views import HelloWorldResource

    # Todo: think about flask-restful usage
    restful_api.add_resource(HelloWorldResource, '/api')
    restful_api.init_app(self.app)
    return restful_api

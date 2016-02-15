# -*- coding: utf-8 -*-
# @Date    : 2016-02-15 15:55
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.restful import Resource


class HelloWorldResource(Resource):
    def get(self):
        return dict(hello='world')

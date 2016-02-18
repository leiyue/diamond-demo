# -*- coding: utf-8 -*-
# @Date    : 2016-02-17 14:40
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.marshmallow import Marshmallow

marshmallow = Marshmallow()


def init_marshmallow(self):
    marshmallow.init_app(self.app)

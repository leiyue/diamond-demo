# -*- coding: utf-8 -*-
# @Date    : 2016-02-14 1:25
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.babelex import Babel

babel = Babel()


def init_babel(self):
    babel.init_app(self.app)

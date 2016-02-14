# -*- coding: utf-8 -*-
# @Date    : 2016-02-14 1:02
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals


def init_blueprints(self):
    from ..views import public_blueprint

    self.app.register_blueprint(public_blueprint)

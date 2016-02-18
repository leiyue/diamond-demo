# -*- coding: utf-8 -*-
# @Date    : 2016-02-14 0:35
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import flask
import flask.ext.security as security
from flask.ext.admin import BaseView
from flask.ext.admin.contrib.sqla import ModelView


class AuthUserMixin(object):
    def is_accessible(self):
        return security.current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(security.url_for_security('login'))


class AuthUserView(AuthUserMixin, BaseView):
    pass


class AuthUserModelView(AuthUserMixin, ModelView):
    pass

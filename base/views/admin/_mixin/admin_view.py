# -*- coding: utf-8 -*-
# -*- date: 2016-02-14 0:32 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

import flask
import flask.ext.security as security
from flask.ext.admin import BaseView
from flask.ext.admin.contrib.sqla import ModelView


class AdminUserMixin(object):
    def is_accessible(self):
        return security.current_user.has_role('Admin')

    def inaccessible_callback(self, name, **kwargs):
        return flask.redirect(security.url_for_security('login'))


class AdminUserView(AdminUserMixin, BaseView):
    pass


class AdminUserModelView(AdminUserMixin, ModelView):
    pass

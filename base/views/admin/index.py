# -*- coding: utf-8 -*-
# @Date    : 2016-02-14 2:07
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.admin import AdminIndexView, expose

from ._mixin import AdminUserMixin


class AdminIndex(AdminUserMixin, AdminIndexView):
    @expose()
    def index(self):
        return self.render('admin/extended_index.html')

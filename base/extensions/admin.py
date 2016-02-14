# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 23:50
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import flask
from flask.ext.admin import Admin, helpers as admin_helpers
from werkzeug.local import LocalProxy

_security = LocalProxy(lambda: flask.current_app.extensions['security'])


def init_admin(self, index_view=None, app_models=None):
    from .. import db
    from ..models import User, Role
    from ..views import AdminIndex, AdminUser, AdminRole

    admin = Admin(
        name=self.app.config['PROJECT_NAME'] or 'Admin',
        base_template='admin/extended_base.html',
        index_view=index_view or AdminIndex(url='/admin'),
        template_mode='bootstrap3'
    )

    admin.init_app(self.app)

    admin.add_view(AdminUser(User, db.session, name='用户管理', category='系统管理'))
    admin.add_view(AdminRole(Role, db.session, name='角色管理', category='系统管理'))

    with self.app.app_context():
        @_security.context_processor
        def security_context_processor():
            return dict(
                admin_base_template=admin.base_template,
                admin_view=admin.index_view,
                h=admin_helpers,
            )

    return admin
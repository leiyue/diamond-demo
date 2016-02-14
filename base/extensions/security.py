# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 17:18
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.security import Security, SQLAlchemyUserDatastore

security = Security()


def init_security(self, app_models=None):
    from .. import db
    if not app_models:
        from ..models import Role
        from ..models import User
    else:
        models = app_models

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(self.app, datastore=user_datastore)

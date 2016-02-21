# -*- coding: utf-8 -*-
# -*- date: 2016-02-13 17:18 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.security import Security, SQLAlchemyUserDatastore

__all__ = ['security', 'init_security']

security = Security()


def init_security(self):
    from .. import db
    from ..models import Role
    from ..models import User
    from ..forms import ExtendedLoginForm

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(self.app,
                      datastore=user_datastore,
                      login_form=ExtendedLoginForm, )

    try:
        from wtforms.fields import HiddenField
    except ImportError:
        def is_hidden_field_filter(field):
            raise RuntimeError('WTForms is not installed.')
    else:
        def is_hidden_field_filter(field):
            return isinstance(field, HiddenField)

    self.app.jinja_env.globals['is_hidden_field'] = is_hidden_field_filter

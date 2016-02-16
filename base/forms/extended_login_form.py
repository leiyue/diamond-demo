# -*- coding: utf-8 -*-
# @Date    : 2016-02-16 1:37
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import flask
import flask.ext.security as security
from werkzeug.local import LocalProxy
from wtforms import StringField, PasswordField, BooleanField, SubmitField

_datastore = LocalProxy(lambda: flask.current_app.extensions['security'].datastore)
_remember_default = LocalProxy(lambda: flask.current_app.config.get('SECURITY_DEFAULT_REMEMBER_ME', True))


class ExtendedLoginForm(security.forms.Form, security.forms.NextFormMixin):
    user = None
    login_name = StringField('用户名', validators=[security.forms.email_required])
    password = PasswordField('密码', validators=[security.forms.password_required])
    remember = BooleanField('自动登录', default='checked' if _remember_default else None)
    submit = SubmitField('登录')

    def validate(self):
        if not super(ExtendedLoginForm, self).validate():
            return False

        if self.login_name.data.strip() == '':
            self.login_name.errors.append(security.utils.get_message('EMAIL_NOT_PROVIDED')[0])
            return False

        if self.password.data.strip() == '':
            self.password.errors.append(security.utils.get_message('PASSWORD_NOT_PROVIDED')[0])
            return False

        self.user = _datastore.get_user(self.login_name.data)

        if self.user is None:
            self.login_name.errors.append(security.utils.get_message('USER_DOES_NOT_EXIST')[0])
            return False

        if not self.user.password:
            self.password.errors.append(security.utils.get_message('PASSWORD_NOT_SET')[0])
            return False

        if not security.utils.verify_and_update_password(self.password.data, self.user):
            self.password.errors.append(security.utils.get_message('INVALID_PASSWORD')[0])
            return False

        if not self.user.is_active:
            self.login_name.errors.append(security.utils.get_message('DISABLED_ACCOUNT')[0])
            return False

        return True

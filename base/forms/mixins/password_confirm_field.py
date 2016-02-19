# -*- coding: utf-8 -*-
# -*- date: 2016-02-16 1:33 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.security.forms import EqualTo
from wtforms import PasswordField

_confirm_password_equal = EqualTo('password', message='RETYPE_PASSWORD_MISMATCH')


class PasswordConfirmField(object):
    password_confirm = PasswordField('重复密码', validators=[_confirm_password_equal])

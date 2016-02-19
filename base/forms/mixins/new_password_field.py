# -*- coding: utf-8 -*-
# -*- date: 2016-02-16 1:31 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.security.forms import password_required, password_length
from wtforms import PasswordField


class NewPasswordField(object):
    password = PasswordField('密码', validators=[password_required, password_length])

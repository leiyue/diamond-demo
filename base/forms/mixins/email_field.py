# -*- coding: utf-8 -*-
# -*- date: 2016-02-16 1:24 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.security.forms import email_required, email_validator
from wtforms import StringField


class EmailField(object):
    email = StringField('邮件地址', validators=[email_required, email_validator])

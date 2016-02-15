# -*- coding: utf-8 -*-
# @Date    : 2016-02-16 1:28
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.security.forms import email_required, email_validator, unique_user_email
from wtforms import StringField


class UniqueEmailField(object):
    email = StringField('邮件地址', validators=[email_required, email_validator, unique_user_email])

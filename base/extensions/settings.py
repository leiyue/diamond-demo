# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 16:51
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import os


def init_settings(self):
    # BaseApp
    self.app.config['DEBUG'] = True
    self.app.config['PROJECT_NAME'] = 'DiamondDemo'
    self.app.config['APP_DIR'] = os.path.abspath(
        os.path.dirname(os.path.dirname(__file__)))
    self.app.config['PROJECT_ROOT'] = os.path.abspath(
        os.path.join(self.app.config['APP_DIR'], os.pardir))

    # logs
    self.app.config['LOG'] = 'var/log/dev.log'
    self.app.config['LOG_LEVEL'] = 'DEBUG'

    # database
    self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(
        os.path.join(self.app.config['PROJECT_ROOT'], r'var\db\dev.db'))
    self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # security
    self.app.config['SECRET_KEY'] = 'YouShouldNeverGuessItOut'
    self.app.config['SECURITY_REGISTERABLE'] = True
    self.app.config['SECURITY_CHANGEABLE'] = True
    self.app.config['SECURITY_LOGIN_URL'] = '/'
    self.app.config['SECURITY_UNAUTHORIZED_VIEW'] = None
    self.app.config['SECURITY_POST_LOGIN_VIEW'] = '/admin'
    self.app.config['SECURITY_LOGIN_USER_TEMPLATE'] = 'security/extended_login_user.html'

    # babel
    self.app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans_CN'

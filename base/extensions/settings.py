# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 16:51
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import os


def init_settings(self):
    self.app.config.from_yaml(
        os.path.join(self.app.root_path, os.path.pardir, 'etc', 'conf', 'settings.yaml'))

    # database
    self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(
        os.path.join(self.app.root_path, os.path.pardir, 'var', 'db', 'dev.db'))

    if os.environ.get('SETTINGS'):
        self.app.config.from_envvar('SETTINGS')

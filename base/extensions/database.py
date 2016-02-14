# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 17:10
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_database(self):
    db.app = self.app
    db.init_app(self.app)

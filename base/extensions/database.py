# -*- coding: utf-8 -*-
# -*- date: 2016-02-13 17:10 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.sqlalchemy import SQLAlchemy

__all__ = ['db', 'init_database']

db = SQLAlchemy()


def init_database(self):
    db.app = self.app
    db.init_app(self.app)

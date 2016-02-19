# -*- coding: utf-8 -*-
# -*- date: 2016-02-17 14:40 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.marshmallow import Marshmallow

ma = Marshmallow()


def init_marshmallow(self):
    ma.init_app(self.app)

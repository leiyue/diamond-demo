# -*- coding: utf-8 -*-
# -*- date: 2016-02-14 1:25 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.babelex import Babel

babel = Babel()


def init_babel(self):
    babel.init_app(self.app)

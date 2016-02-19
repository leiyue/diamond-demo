# -*- coding: utf-8 -*-
# -*- date: 2016-02-14 1:02 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)


def init_blueprints(self):
    from ..views import public_blueprint

    self.app.register_blueprint(public_blueprint)

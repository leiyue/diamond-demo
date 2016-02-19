# -*- coding: utf-8 -*-
# -*- date: 2016-02-14 0:54 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

import flask

public_blueprint = flask.Blueprint('public', __name__)

from .views import *  # noqa

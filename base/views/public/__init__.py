# -*- coding: utf-8 -*-
# -*- date: 2016-02-20 17:09 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import flask

__all__ = ['public_blueprint']

public_blueprint = flask.Blueprint('public', __name__)

# @public_blueprint.route('/')
# def index():
#     return 'hello world'

from .views import *  # noqa

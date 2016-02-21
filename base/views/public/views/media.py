# -*- coding: utf-8 -*-
# -*- date: 2016-02-20 17:10 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

import flask

from .. import public_blueprint

__all__ = ['media']


@public_blueprint.route('/media/<path:filename>')
def media(filename):
    return flask.send_from_directory(
        os.path.join(flask.current_app.root_path, 'media'), filename)
    # return flask.send_from_directory(flask.current_app.root_path, filename, as_attachment=True)

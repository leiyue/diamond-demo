# -*- coding: utf-8 -*-
# -*- date: 2016-02-16 1:11 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.assets import Environment, Bundle

assets = Environment()


def init_assets(self):
    css = Bundle(
        'libs/bootstrap/dist/css/bootstrap.css',
        'css/style.css',
        filters='cssmin',
        output='public/css/common.css'
    )
    js = Bundle(
        'libs/jquery/dist/jquery.js',
        'libs/bootstrap/dist/js/bootstrap.js',
        filters='jsmin',
        output='public/js/common.js'
    )

    assets.register('css_all', css)
    assets.register('js_all', js)
    assets.init_app(self.app)

# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 15:03
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import os

import yaml
from flask import Flask as BaseFlask, Config as BaseConfig

from .extensions import *

try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

app_instance = None


class Config(BaseConfig):
    def from_yaml(self, config_file):
        env = os.environ.get('FLASK_ENV', 'DEVELOPMENT')
        self['ENVIRONMENT'] = env.lower()

        with open(config_file) as f:
            c = yaml.load(f)

        c = c.get(env, c)

        for key in c.iterkeys():
            if key.isupper():
                self[key] = c[key]


class Flask(BaseFlask):
    def make_config(self, instance_relative=False):
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return Config(root_path, self.default_config)


class BaseApp(object):
    _extensions = [
        'settings',
        'logs',
        'database',
        'marshmallow',
        'security',
        'babel',
        'signals',
        'admin',
        'restful',
        'blueprints',
    ]

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, name=None, extensions=_extensions):
        if not name:
            name = __name__
        self.app = Flask(name)

        for extension_name in extensions:
            init_method = 'init_{0}'.format(extension_name)
            if not hasattr(self, init_method):
                method_to_call = globals()[init_method]
            else:
                method_to_call = getattr(self, init_method)
            setattr(self, init_method, method_to_call)

            try:
                result = method_to_call(self)
            except TypeError:
                result = method_to_call()

            self.app.logger.debug('initialized {0}'.format(extension_name))

        if hasattr(self.app, 'teardown_appcontext'):
            self.app.teardown_appcontext(self.teardown)
        else:
            self.app.teardown_request(self.teardown)

    def super(self, extension_name, **kwargs):
        init_method = 'init_{0}'.format(extension_name)
        # ensure the global version is called
        method_to_call = globals()[init_method]
        result = method_to_call(self, **kwargs)
        return result

    def teardown(self, exception):
        ctx = stack.top
        if hasattr(ctx, 'diamond'):
            pass

    @property
    def _app(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'app'):
                pass
            return ctx.app


def create_app():
    global app_instance
    if not app_instance:
        app_instance = BaseApp()
        app_instance.init_app()

    return app_instance.app

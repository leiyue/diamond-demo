# -*- coding: utf-8 -*-
# -*- date: 2016-02-19 20:31 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask import Blueprint

from base import BaseApp, db

app_instance = None


class BlogApp(BaseApp):
    def init_admin(self):
        from .models import Post
        from .views import AdminPost

        admin = self.super('admin')
        admin.add_view(AdminPost(Post, db.session, name='博客管理', category='内容管理'))

    def init_restful(self):
        from .resources import PostListResource, PostItemResource

        api = self.super('restful')
        api.add_resource(PostListResource, '/post')
        api.add_resource(PostItemResource, '/post/<int:instance_id>')

        api_blueprint = Blueprint('api', __name__, url_prefix='/api')
        api.init_app(api_blueprint)
        self.app.register_blueprint(api_blueprint)


def create_app():
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
    global app_instance
    if not app_instance:
        app_instance = BlogApp()
        app_instance.init_app(extensions=_extensions)

    return app_instance.app

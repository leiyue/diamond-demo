# -*- coding: utf-8 -*-
# -*- date: 2016-02-19 20:31 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import os

from flask.ext.admin.contrib.fileadmin import FileAdmin

from base import BaseApp, db, api

app_instance = None


class BlogApp(BaseApp):
    def init_admin(self):
        from .models import Post
        from .views import PostAdmin

        admin = self.super('admin')
        admin.add_view(PostAdmin(Post, db.session, name='博客管理', category='内容管理'))

        path = os.path.join(self.app.root_path, 'media')
        admin.add_view(FileAdmin(path, '/media/', name='文件管理', category='内容管理'))

    def init_restful(self):
        from base.resources import RoleListResource, RoleItemResource
        from base.resources import UserListResource, UserItemResource
        from .resources import PostListResource, PostItemResource

        api.add_resource(RoleListResource, '/api/role')
        api.add_resource(RoleItemResource, '/api/role/<int:instance_id>')
        api.add_resource(UserListResource, '/api/user')
        api.add_resource(UserItemResource, '/api/user/<int:instance_id>')
        api.add_resource(PostListResource, '/api/post')
        api.add_resource(PostItemResource, '/api/post/<int:instance_id>')

        api.init_app(self.app)


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

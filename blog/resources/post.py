# -*- coding: utf-8 -*-
# -*- date: 2016-02-19 21:56 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from flask.ext.restful import Resource, abort

from base.resources.decorators import load_with, dump_with
from ..models import Post, PostSchema

_schema = PostSchema()
_list_schema = PostSchema(many=True)


class PostListResource(Resource):
    # method_decorators = [auth_token_required]

    model = Post

    @dump_with(_list_schema)
    def get(self):
        instances = self.model.query.all()
        return instances

    @load_with(_schema)
    @dump_with(_schema)
    def post(self, data):
        instance = self.model.create(**data)
        return instance


class PostItemResource(Resource):
    # method_decorators = [auth_token_required]

    model = Post

    @dump_with(_schema)
    def get(self, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        return instance

    def delete(self, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        return instance.delete() and '', 204

    @load_with(_schema)
    @dump_with(_schema)
    def put(self, data, instance_id):
        instance = self.model.get_by_id(instance_id)
        if not instance:
            abort(404, message='Resource does not exists')
        instance = instance.update(**data)
        return instance

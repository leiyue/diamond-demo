# -*- coding: utf-8 -*-
# -*- date: 2016-02-19 20:58 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from base import db, ma
from base.models import CRUDMixin, TimestampMixin, UserExposeSchema


class Post(db.Model, CRUDMixin, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<{class_name}({title})>'.format(class_name=self.__class__.__name__, name=self.title)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class PostSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'title',
                  'content',
                  'author',
                  '_links')

    author = ma.Nested(UserExposeSchema)
    _links = ma.Hyperlinks({
        'self': ma.URLFor('postitemresource', instance_id='<id>'),
        'collection': ma.URLFor('postlistresource')
    })

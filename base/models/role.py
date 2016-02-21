# -*- coding: utf-8 -*-
# -*- date: 2016-02-13 17:23 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.security import RoleMixin

from ._mixins import CRUDMixin, TimestampMixin
from .. import db, ma

__all__ = ['Role', 'RoleSchema']


class Role(db.Model, RoleMixin, CRUDMixin, TimestampMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<{class_name}({name})>'.format(
            class_name=self.__class__.__name__, name=self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', '_links')

    _links = ma.Hyperlinks({
        'self': ma.URLFor('roleitemresource', instance_id='<id>'),
        'collection': ma.URLFor('rolelistresource')
    })

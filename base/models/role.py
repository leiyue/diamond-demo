# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 17:23
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from flask.ext.security import RoleMixin

from .mixins import CRUDMixin, MarshmallowMixin, TimestampMixin
from .. import db


class Role(db.Model, RoleMixin, CRUDMixin, MarshmallowMixin, TimestampMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<{class_name}({name})>'.format(class_name=self.__class__.__name__, name=self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

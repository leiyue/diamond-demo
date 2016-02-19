# -*- coding: utf-8 -*-
# -*- date: 2016-02-19 20:39 -*-

from base import db, ma
from base.models._mixins import CRUDMixin, TimestampMixin
from base.models import User, UserSchema  # noqa
from base.models import Role, RoleSchema  # noqa
from .post import Post, PostSchema

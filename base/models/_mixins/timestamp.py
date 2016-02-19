# -*- coding: utf-8 -*-
# -*- date: 2016-02-15 21:28 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

import datetime

from ... import db


class TimestampMixin(object):
    """Mixin that adds two Timestamp columns."""

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)

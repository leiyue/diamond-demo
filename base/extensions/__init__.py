# -*- coding: utf-8 -*-
# -*- date: 2016-02-13 16:44 -*-

from .settings import init_settings
from .logs import init_logs
from .database import db, init_database
from .marshmallow import ma, init_marshmallow
from .security import security, init_security
from .babel import babel, init_babel
from .blueprints import init_blueprints
from .signals import init_signals
from .admin import init_admin
from .restful import api, init_restful

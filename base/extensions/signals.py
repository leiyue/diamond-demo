# -*- coding: utf-8 -*-
# -*- date: 2016-02-13 23:17 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from flask.ext.security import user_registered


def init_signals(self):
    @user_registered.connect_via(self.app)
    def user_registered_signal_handler(sender, **extra):
        from .. import security

        user = extra['user']
        user_role = security.datastore.find_role('User')
        security.datastore.add_role_to_user(user, user_role)
        self.app.logger.info('added role <User> to {0}'.format(user))

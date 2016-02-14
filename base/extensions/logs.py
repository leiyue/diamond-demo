# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 16:49
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import logging


def init_logs(self):
    handler = logging.FileHandler(self.app.config.get('LOG', 'var/log/dev.log'))
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
    self.app.logger.addHandler(handler)
    _log_level = self.app.config.get('LOG_LEVEL')
    if _log_level == 'DEBUG':
        self.app.logger.setLevel(logging.DEBUG)
    elif _log_level == 'WARNING':
        self.app.logger.setLevel(logging.WARNING)
    else:
        self.app.logger.setLevel(logging.INFO)
    self.app.logger.info('Startup log with level: {0}'.format(_log_level))

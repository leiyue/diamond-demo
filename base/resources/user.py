# -*- coding: utf-8 -*-
# @Date    : 2016-02-17 14:51
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import flask
from flask.ext.restful import Resource

from ..models import User


class UserList(Resource):
    def get(self):
        data = User.dump_all()
        flask.current_app.logger.debug(data)
        return flask.jsonify(result=data)


class UserItem(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        result = User.dump(user)
        flask.current_app.logger.debug(user)
        return flask.jsonify(result)

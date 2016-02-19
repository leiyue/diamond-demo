# -*- coding: utf-8 -*-
# -*- date: 2016-02-18 1:18 -*-

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

from functools import wraps

from flask import request


def load_with(schema, force=False):
    def wrapper(f):
        f.__accept__ = {
            'schema': schema,
            'force': force,
        }

        @wraps(f)
        def wrapped(*args, **kwargs):
            from flask.ext.restful import abort

            data = request.get_json(force=force)
            result = schema.load(data)

            if result.errors:
                abort(412, message=result.errors)
            if result.data is None:
                abort(400, message='Wrong input data')
            return f(*args, data=result.data, **kwargs)

        return wrapped

    return wrapper


def dump_with(schema):
    def convert(data):
        data = schema.dump(data).data
        return data

    def wrapper(f):
        f.__export__ = {
            'schema': schema,
        }

        @wraps(f)
        def wrapped(*args, **kwargs):
            result = f(*args, **kwargs)

            if isinstance(result, tuple):
                (code, data) = result
                data = convert(data)

                result = (code, data)
            else:
                data = convert(result)

                result = data
            return result

        return wrapped

    return wrapper

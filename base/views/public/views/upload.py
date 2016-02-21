# -*- coding: utf-8 -*-
# -*- date: 2016-02-20 17:10 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import datetime
import os

import flask

from .. import public_blueprint

__all__ = ['upload']


@public_blueprint.route('/upload/', methods=['POST', 'OPTIONS'])
def upload():
    error = ''
    url = ''
    callback = flask.request.args.get("CKEditorFuncNum")

    if flask.request.method == 'POST' and 'upload' in flask.request.files:
        file_obj = flask.request.files['upload']
        file_name, file_ext = os.path.splitext(file_obj.filename)
        current_day = datetime.datetime.now().strftime('%Y%m%d')
        current_time = datetime.datetime.now().strftime('%H%M%S')
        unique_name = '{0}_{1}{2}'.format(file_name, current_time, file_ext)
        file_path = os.path.join(flask.current_app.root_path, 'media', current_day, unique_name)

        dir_name = os.path.dirname(file_path)
        if not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name)
            except:
                error = 'ERROR_CREATE_DIR'
        elif not os.access(dir_name, os.W_OK):
            error = 'ERROR_DIR_NOT_WRITEABLE'
        if not error:
            file_obj.save(file_path)
            url = flask.url_for('public.media', filename='{dir_name}/{filename}'
                                .format(dir_name=current_day, filename=unique_name))
    else:
        error = 'ERROR_UPLOAD_FAILURE'

    res = """<script type="text/javascript">
window.parent.CKEDITOR.tools.callFunction({0}, '{1}', '{2}');
</script>
""".format(callback, url, error)

    response = flask.make_response(res)
    response.headers["Content-Type"] = "text/html"
    return response

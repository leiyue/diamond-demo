# -*- coding: utf-8 -*-
# -*- date: 2016-02-20 22:04 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import datetime
import os

import flask
import flask.ext.security as security
from werkzeug.utils import secure_filename

from .. import public_blueprint

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps

THUMBNAIL_SIZE = (75, 75,)


def get_available_name(name):
    dir_name, file_name = os.path.split(name)
    file_root, file_ext = os.path.splitext(file_name)
    while os.path.exists(name):
        file_root += '_'
        name = os.path.join(dir_name, file_root, file_ext)
    return name


def get_thumb_filename(file_name):
    file_root, file_ext = os.path.splitext(file_name)
    return '{0}_thumb{1}'.format(file_root, file_ext)


def create_thumbnail(filename):
    image = Image.open(filename)

    if image.mode not in ('L', 'RGB'):
        image = image.convert('RGB')

    imagefit = ImageOps.fit(image, THUMBNAIL_SIZE, Image.ANTIALIAS)
    imagefit.save(get_thumb_filename(filename))


def get_media_url(path):
    relative_path = path.replace(os.path.join(
        flask.current_app.root_path, 'media'), '').replace('\\', '/')[1:]

    url = flask.url_for('public.media', filename='{path}'
                        .format(path=relative_path))
    return url


def get_upload_filename(upload_name):
    year, month, day = tuple(datetime.datetime.now().strftime('%Y/%m/%d').split('/'))
    upload_path = os.path.join(flask.current_app.root_path, 'media', year, month, day)
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    return get_available_name(os.path.join(upload_path, upload_name))


@public_blueprint.route('/ck_upload', methods=['POST', 'OPTIONS'])
def ck_upload():
    upload_file = flask.request.files['upload']
    filename = secure_filename(upload_file.filename)
    upload_filename = get_upload_filename(filename)

    upload_file.save(upload_filename)
    create_thumbnail(upload_filename)
    url = get_media_url(upload_filename)

    return flask.make_response("""
    <script type='text/javascript'>
        window.parent.CKEDITOR.tools.callFunction(%s, '%s');
    </script>""" % (flask.request.args.get('CKEditorFuncNum'), url))


def get_image_files(user=None):
    if user and not user.has_role('Admin'):
        user_path = user.email
    else:
        user_path = ''

    browse_path = os.path.join(flask.current_app.root_path, 'media', user_path)

    for root, dirs, files in os.walk(browse_path):
        for filename in [os.path.join(root, x) for x in files]:
            if os.path.splitext(filename)[0].endswith('_thumb'):
                continue
            yield filename


def get_image_browse_urls(user=None):
    images = []
    for filename in get_image_files(user=user):
        images.append(dict(
            thumb=get_media_url(get_thumb_filename(filename)),
            src=get_media_url(filename)
        ))

    return images


@public_blueprint.route('/ck_browse', methods=['GET', 'POST'])
def ck_browse():
    images = get_image_browse_urls(security.current_user)
    return flask.render_template('public/ckeditor_browse.html', **locals())

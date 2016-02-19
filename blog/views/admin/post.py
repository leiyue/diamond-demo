# -*- coding: utf-8 -*-
# -*- date: 2016-02-19 21:18 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from . import AdminUserModelView


class AdminPost(AdminUserModelView):
    page_size = 30
    can_create = True
    can_delete = False
    can_edit = True
    column_display_pk = False
    column_filters = ['title']
    column_exclude_list = ('created_at', 'updated_at',)
    column_default_sort = ('id', False)
    column_searchable_list = ('title', 'content',)
    column_labels = dict(
        id='ID',
        author='作者',
        title='标题',
        content='内容',
        created_at='创建时间',
        updated_at='更新时间')
    # form_columns = ('name', 'description', 'created_at', 'updated_at', 'users')
    #
    # column_descriptions = dict(
    #     name='推荐使用英文名称，兼容性更强',
    #     description='简要的描述角色的作用',
    #     users='默认角色User中包含所有用户，请等候……')

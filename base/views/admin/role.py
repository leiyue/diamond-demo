# -*- coding: utf-8 -*-
# @Date    : 2016-02-14 18:23
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

from ..core import AdminModelView


class AdminRole(AdminModelView):
    page_size = 30
    can_create = True
    can_delete = False
    can_edit = True
    column_display_pk = False
    column_filters = ['name']
    column_exclude_list = ('created_at', 'updated_at',)
    column_default_sort = ('id', False)
    column_searchable_list = ('name', 'description',)
    column_labels = dict(
        id='ID',
        name='角色名称',
        description='角色描述',
        created_at='创建时间',
        updated_at='更新时间',
        users='包含以下用户')
    form_columns = ('name', 'description', 'created_at', 'updated_at', 'users')

    column_descriptions = dict(
        name='推荐使用英文名称，兼容性更强',
        description='简要的描述角色的作用',
        users='默认角色User中包含所有用户，请等候……')

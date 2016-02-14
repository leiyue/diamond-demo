# -*- coding: utf-8 -*-
# @Date    : 2016-02-13 15:14
# @Author  : leiyue (mr.leiyue@gmail.com)
# @Link    : https://leiyue.wordpress.com/

from __future__ import absolute_import, division, print_function, with_statement, unicode_literals

import alembic
from flask.ext.migrate import Migrate, MigrateCommand, upgrade
from flask.ext.script import Manager, Shell, Server
from flask_script.commands import Clean, ShowUrls

from base import create_app, db, models

app = create_app()
migrate = Migrate(app, db, directory="var/migrations")


def _make_context():
    return dict(app=app, db=db, models=models)


manager = Manager(app)
manager.add_command('shell', Shell(make_context=_make_context))
manager.add_command('runserver', Server(port=app.config.get('PORT', 5000)))
manager.add_command('public', Server(port=app.config.get('PORT', 5000), host='0.0.0.0'))
manager.add_command('db', MigrateCommand)
manager.add_command('clean', Clean)
manager.add_command('urls', ShowUrls)


@manager.option('-m', '--migration', help='create database from migrations', action='store_true', default=None)
def init_db(migration):
    db.drop_all()

    if migration:
        # create database using migrations
        print('applying migration')
        upgrade()
    else:
        # create database from model schema directly
        db.create_all()
        db.session.commit()
        cfg = alembic.config.Config('var/migrations/alembic.ini')
        alembic.command.stamp(cfg, "head")


@manager.command
def populate_db():
    models.User.add_system_users()


if __name__ == '__main__':
    manager.run()

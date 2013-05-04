#!/usr/bin/env python
# -*- coding:utf-8 -*-

from apoc import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
    
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import Table, MetaData, Column
from sqlalchemy import Integer, Unicode, UnicodeText, Boolean, DateTime, Float, Text
from sqlalchemy.orm import mapper

from sqlalchemy import or_, and_

import uuid

Base = declarative_base()

def gen_uuid():
    return str(uuid.uuid1()).replace('-', '')

def get_session():
    connect_args = {
        'user': config.mysql.username,
        'passwd': config.mysql.password,
        'charset': 'utf8'
        }
    db_url = 'mysql://%s:%s/%s?charset=utf8&use_unicode=1' \
             % (config.mysql.host,
                config.mysql.port,
                config.mysql.database,
                )

    engine = create_engine(db_url,
                           connect_args = connect_args,
                           poolclass=NullPool,
                           echo=False)
    #some_engine = create_engine('postgresql://scott:tiger@localhost/')
    Session = scoped_session(
        sessionmaker(bind=engine, autocommit = True, autoflush=True)
    )

    return Session



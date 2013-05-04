#!/usr/bin/env python
# -*- coding:utf-8 -*-

from apoc.models.base import *

class User(Base):
    __tablename__ = 'users'

    id         = Column(Integer, primary_key = True)
    nickname   = Column(Unicode)
    email      = Column(Unicode)
    password   = Column(Unicode)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    @classmethod
    def get(cls, db_session, id):
        return db_session.query(cls).filter_by(id = id).first()

    @classmethod
    def gets_by_ids(cls, db_session, ids):
        return db_session.query(cls).filter(cls.id.in_(ids)).all()

    @classmethod
    def get_with_login(cls, db_session, email, password):
        return db_session.query(cls).filter_by(email = email, password = password).first()

    @classmethod
    def gets(cls, db_session):
        return db_session.query(cls).all()

    def hash(self, origin_password):
        return origin_password


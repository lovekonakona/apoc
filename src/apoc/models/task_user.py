#!/usr/bin/env python
# -*- coding:utf-8 -*-

from apoc.models.base import *

class TaskUser(Base):
    __tablename__ = 'task_user_mapping'

    task_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, primary_key = True)

    @classmethod
    def new(cls, db_session, task_id, user_id):
        task_user = TaskUser(task_id = task_id, user_id = user_id)
        
        with db_session.begin():
            db_session.add(task_user)
            db_session.flush()

        return task_user

    @classmethod
    def gets(cls, db_session, task_id = None, user_id = None):
        q = db_session.query(cls)
        
        if task_id:
            q = q.filter_by(task_id = task_id)

        if user_id:
            q = q.filter_by(user_id = user_id)

        return q.all()

    @classmethod
    def get(cls, db_session, task_id, user_id):
        return db_session.query(cls).filter_by(task_id = task_id, user_id = user_id).first()

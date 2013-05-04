#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

from apoc.models.base import *
from .status import Status
from .task_user import TaskUser
from .user import User


class Task(Base):
    __tablename__ = 'tasks'

    id             = Column(Integer, primary_key = True)
    title          = Column(Unicode)
    description    = Column(UnicodeText)
    creater_id     = Column(Integer)
    created_at     = Column(DateTime)
    updated_at     = Column(DateTime)
    estimated_hour = Column(Float)
    used_hour      = Column(Float)
    status         = Column(Integer)

    @classmethod
    def new(cls, db_session, title, description, creater_id, estimated_hour = 0):

        task = Task(title = title, description = description, creater_id = creater_id, estimated_hour = estimated_hour, used_hour = 0)
        task.created_at = task.updated_at = datetime.datetime.now()
        task.status = Status.OPEN

        with db_session.begin():
            db_session.add(task)
            db_session.flush()

        return task

    @classmethod
    def get(cls, db_session, id_):
        task = db_session.query(cls).filter_by(id = id_).first()
        if task:
            task_user_mapping = TaskUser.gets(db_session, task_id = task.id)
            user_ids = [tu.user_id for tu in task_user_mapping]
            task.users = User.gets_by_ids(db_session, user_ids) or []

        return task

    @classmethod
    def gets(cls, db_session):
        tasks = db_session.query(cls).all()
        for task in tasks:
            task_user_mapping = TaskUser.gets(db_session, task_id = task.id)
            user_ids = [tu.user_id for tu in task_user_mapping]
            task.users = User.gets_by_ids(db_session, user_ids) or []

        return tasks

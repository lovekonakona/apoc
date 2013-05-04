#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler
from apoc.models import Task, User, TaskUser
from apoc import utils

class TaskHandler(BaseHandler):
    def get(self):
        db_session = self.get_db_session()
        
        tasks = Task.gets(db_session)
        
        data = dict(
            tasks = tasks,
            user = utils.get_user(self, db_session)
            )

        self.render('task.tpl', **data)


class NewTaskHandler(BaseHandler):
    def get(self):
        db_session = self.get_db_session()
        user = utils.get_user(self, db_session)
        
        if not user:
            self.redirect('/login')

        data = dict(
            user = user,
            users = User.gets(db_session)
            )
        
        self.render('task_new.tpl', **data)
    def post(self):
        db_session = self.get_db_session()
        user = utils.get_user(self, db_session)
        
        if not user:
            return self.redirect('/login')

        users = User.gets(db_session)
        assign_list = []

        for u in users:
            try:
                name = 'assign_to_%s' % (str(u.id), )
                if self.get_argument(name):
                    assign_list.append(str(u.id))
            except:
                continue

        title = self.get_argument('title')
        description = self.get_argument('description')
        estimated_hour = self.get_argument('estimated_hour', default=0)

        print assign_list, title, description, estimated_hour

        if not title:
            return self.render('error.tpl', err_msg=u"title cannot be null")

        task = Task.new(db_session, title, description, user.id, estimated_hour)

        if assign_list and len(assign_list) > 0:
            for user_id in assign_list:
                TaskUser.new(db_session, task.id, user_id)

        self.redirect('/task')
            

class EditTaskHandler(BaseHandler):
    def get(self, task_id):
        db_session = self.get_db_session()
        task = Task.get(db_session, task_id)

        assign_ids = []
        for u in task.users:
            assign_ids.append(u.id)

        data = dict(
            task = task,
            user = utils.get_user(self, db_session),
            users = User.gets(db_session),
            assign_ids = assign_ids,
            )

        self.render('task_edit.tpl', **data)

    def post(self, task_id):
        db_session = self.get_db_session()
        user = utils.get_user(self, db_session)

        if not user:
            return self.redirect('/login')

        if not task_id:
            self.redirect('/task')

        title = self.get_argument('title')
        description = self.get_argument('description')
        estimated_hour = self.get_argument('estimated_hour', default = 0)
        status = self.get_argument('status', default = 1)

        if not title:
            return self.render('error.tpl', err_msg=u"title cannot be null")

        task = Task.get(db_session, task_id)

        task.title = title
        task.description = description
        task.estimated_hour = estimated_hour
        task.status = status

        users = User.gets(db_session)

        for u in users:
            try:
                name = 'assign_to_%s' % (str(u.id), )

                if self.get_argument(name):
                    task_user = TaskUser(task_id = task_id, user_id = u.id)
                    with db_session.begin():
                        db_session.merge(task_user)
            except:
                task_user = TaskUser.get(db_session, task_id, u.id)
                if task_user:
                    with db_session.begin():
                        db_session.delete(task_user)

        db_session.flush()

        self.redirect('/task')

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .index import IndexHandler
from .login import LoginHandler, SignUpHandler, LogoutHandler
from .task import TaskHandler, NewTaskHandler, EditTaskHandler
from .notfound import NotFoundHandler

def get_handlers(Session):
    return [
        (r"/", IndexHandler, { 'Session' : Session }),
        (r"/login", LoginHandler, { 'Session' : Session }),
        # (r"/signup", SignUpHandler, { 'Session' : Session }),
        (r"/logout", LogoutHandler, { 'Session' : Session }),
        (r"/task", TaskHandler, { 'Session' : Session }),
        (r"/task/new", NewTaskHandler, { 'Session' : Session }),
        (r"/task/edit/(\d+)", EditTaskHandler, { 'Session' : Session }),
        ]

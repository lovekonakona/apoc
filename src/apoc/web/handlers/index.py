#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler
from apoc import utils

class IndexHandler(BaseHandler):
    def get(self):
        db_session = self.get_db_session()

        user = utils.get_user(self, db_session)
        self.render('index.tpl', user = user)

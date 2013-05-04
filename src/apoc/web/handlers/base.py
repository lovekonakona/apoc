#!/usr/bin/env python
# -*- coding:utf-8 -*-

import traceback

from tornado.web import RequestHandler
from apoc import utils

class BaseHandler(RequestHandler):

    def initialize(self, Session):
        self.Session = Session
        self.db_session = None

    def get_db_session(self):
        if not self.db_session:
            self.db_session = self.Session()
            #self.db_session.begin()

        """
        #Remember to call session.remove() after using
        return self.Session()
        """
        return self.db_session

    def on_finish(self):
        if self.db_session:
            #self.db_session.commit()
            self.db_session.close()
            self.Session.remove()

    def write_error(self, status_code, **kwargs):
        db_session = self.get_db_session()
        
        exc_info = kwargs['exc_info']
        traceback.print_exception(*exc_info)
        
        err_msg = u"服务器开小差啦, 请稍后再试"

        if status_code == 404:
            err_msg = u"对不起, 您访问的页面不存在"
            
        data = dict(
            err_msg = err_msg,
            user    = utils.get_user(self, db_session)
            )
        
        self.render('error.tpl', **data)

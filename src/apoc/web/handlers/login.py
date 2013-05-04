#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler
from apoc.models import User
from apoc import utils

class LoginHandler(BaseHandler):
    def get(self):
        db_session = self.get_db_session()
        user = utils.get_user(self, db_session)

        if user:
            return self.redirect('/task')

        self.render('login.tpl', user = user)

    def post(self, **kvargs):
        db_session = self.get_db_session()

        email = self.get_argument('email', default = "")
        password = self.get_argument('password', default = "")
        # remember_me = bool(self.get_argument('rememberMe', default = False))

        user = User.get_with_login(db_session, email, utils.hash_password(password))

        if user:
            utils.seed_cookies(self, str(user.id))
            self.redirect('/task')
        else:
            self.render('error.tpl', err_msg = u"用户名或密码错误", user = user)

class SignUpHandler(BaseHandler):
    def get(self):
        db_session = self.get_db_session()
        user = utils.get_user(self, db_session)
        
        if user:
            return self.redirect('/task')

        db_session = self.get_db_session()

        self.render('signup.tpl', user = user)

    def post(self, **kvargs):
        
        nickname = self.get_argument('nickname', default = "")
        email = self.get_argument('email', default = "")
        password = self.get_argument('password', default = "")
        confirm_password = self.get_argument('confirmPassword', default = "")

class LogoutHandler(BaseHandler):
    def get(self):
        utils.logout(self)

        self.redirect('/')

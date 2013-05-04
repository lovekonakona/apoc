#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado.web import UIModule

class Topbar(UIModule):
    def render(self):
        user = 
        self.render('topbar.tpl', )

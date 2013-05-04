#!/usr/bin/env python
# -*- coding:utf-8 -*-

from base import BaseHandler

class NotFoundHandler(BaseHandler):
    
    def get(self):
        raise HTTPError(404)
    
    def post(self):
        raise HTTPError(404)

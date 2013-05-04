#!/usr/bin/env python
# -*- coding:utf-8 -*-

from apoc.web.handlers import indexHandler

def get_routes():
    return [
        (r"/", indexHandler),
        ]

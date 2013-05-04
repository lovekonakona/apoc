#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

import tornado.ioloop
import tornado.web

from tornado.options import define, options

from apoc.web import handlers as web_handlers

from apoc.models import base as models_base

if __name__ == "__main__":
    define("port", default=8888, help="run on the given port", type=int)
    define("running_dir", help="running dir", type=str)

    options.parse_command_line()

    print options.port, options.running_dir

    Session = models_base.get_session()
    
    handlers = web_handlers.get_handlers(Session)

    static_handler = (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "%s/src/static" % (options.running_dir)})
    handlers.append(static_handler)
    handlers.append((r".*", web_handlers.NotFoundHandler, { 'Session' : Session }))

    
    print handlers

    settings = dict(
        debug = True,
        template_path = "%s/src/tpls/" % (options.running_dir),
        )
    
    application = tornado.web.Application(handlers, **settings)

    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

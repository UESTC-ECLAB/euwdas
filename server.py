# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os.path
# from gevent.wsgi import WSGIServer
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from app import create_app
from app import scheduler
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

app = create_app()
if __name__ == '__main__':
    scheduler.start()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(80)
    IOLoop.instance().start()
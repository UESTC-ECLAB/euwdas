# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os.path
from gevent.wsgi import WSGIServer
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
    app.debug = True
    server = WSGIServer(("", 5000), app)
    server.serve_forever()

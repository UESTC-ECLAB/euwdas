from flask import Flask
from flask_apscheduler import APScheduler


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': '__main__:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 10
        },
        {
            'id': 'job2',
            'func': '__main__:job2',
            'args': (1, 3),
            'trigger': {
                'type':'cron',
                'second': '6,9,10'
            }
        },
        {
            'id': 'job3',
            'func': '__main__:job2',
            'args': (1, 3),
            'trigger': {
                'type':'cron',
                'hour': 6
            }
        }
    ]

    SCHEDULER_VIEWS_ENABLED = True


def job1(a, b):
    print(str(a) + ' ' + str(b))

def job2(a, b):
    print(str(a) + ' ' + str(b))

app = Flask(__name__)
app.config.from_object(Config())
app.debug = True

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

app.run()
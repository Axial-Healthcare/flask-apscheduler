from flask import Flask
from flask_apscheduler import APScheduler


class Config(object):
    APSCHEDULER_JOBS = [
        {
            'func': 'examples.jobs_list.job1',
            'trigger': 'cron',
            'second': 10,
            'args': (1, 2)
        }
    ]

    APSCHEDULER_HOSTS = ['localhost']


def job1(a, b):
    print(str(a) + ' ' + str(b))


app = Flask(__name__)
app.config.from_object(Config())

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

app.run()

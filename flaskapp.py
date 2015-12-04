from flask import Flask
from test import make_celery

# this needs to be run to kick off the worker:
# celery -A flaskapp.celery worker -l INFO

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='amqp://',
    CELERY_RESULT_BACKEND='amqp://',
    CELERY_TASK_SERIALIZER = 'json',
    CELERY_RESULT_SERIALIZER = 'json',
)

celery = make_celery(app)


@celery.task()
def add_together(a, b):
    return a + b


@celery.task()
def subtract(a, b):
    return a - b
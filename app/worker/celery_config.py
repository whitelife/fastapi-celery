class CeleryConfig:
    timezone = "Asia/Seoul"
    result_expires = 60 * 60 * 24
    task_track_started = True
    task_routes = {
        'app.worker.celery_worker.create_task': {'queue': 'task_queue'}
    }


backend = "redis://:ac1c24ef3149@localhost:6379/0"
broker = "amqp://admin:d418ae373cad@localhost:5672//"

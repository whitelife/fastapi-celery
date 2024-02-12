from ..app_config import get_app_config

class CeleryConfig:
    timezone = "Asia/Seoul"
    result_expires = 60 * 60 * 24
    task_track_started = True
    task_routes = {
        'app.worker.celery_worker.create_task': {'queue': 'task_queue'}
    }


app_config = get_app_config()
broker = app_config.celery_broker
backend = app_config.celery_backend

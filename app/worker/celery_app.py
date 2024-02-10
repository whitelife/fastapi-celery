from celery import Celery
from .celery_config import CeleryConfig, backend, broker

celery_app = Celery(
    "worker",
    backend=backend,
    broker=broker
)
celery_app.config_from_object(CeleryConfig)
celery_app.conf.update()

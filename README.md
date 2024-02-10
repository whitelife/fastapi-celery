# fastapi-celery

## Install

```
pip install -r requirements.txt
```

## Start FastAPI & Celery

* rabbitmq-management: http://localhost:15672
* flower: http://localhost:5555
* fastapi: http://localhost:8000

```
docker-compose -f ./docker-compose-local.yml up -d

celery -A app.worker.celery_worker worker -Q task_queue,celery -l DEBUG
celery -A app.worker.celery_worker flower --conf="./docker/flower/flower_config.py"

uvicorn app.main:app --reload
```

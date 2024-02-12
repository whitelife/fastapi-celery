# fastapi-celery

## Start FastAPI & Celery (Local)

* rabbitmq-management: http://localhost:15672
* flower: http://localhost:5555
* fastapi: http://localhost:8000

```
pip install -r requirements.txt
docker-compose -f ./docker-compose-local-services.yml up -d

celery -A app.worker.celery_worker worker -Q task_queue,celery -l DEBUG
celery -A app.worker.celery_worker flower --broker-api="http://admin:d418ae373cad@localhost:15672/api/" --logging="DEBUG"

uvicorn app.main:app --reload
```

## Start FastAPI & Celery (Docker-Compose)

* rabbitmq-management: http://localhost:15672
* flower: http://localhost:5555
* fastapi: http://localhost:8000

```
docker-compose -f ./docker-compose-local.yml up -d --build
docker-compose -f ./docker-compose-local.yml logs -f
```

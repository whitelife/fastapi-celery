from celery.result import AsyncResult
from fastapi import FastAPI, Body, Depends
from fastapi.responses import JSONResponse

from .worker.celery_worker import create_task, celery_app
from .app_config import get_app_config

from .dependencies import get_query_token, get_token_header
from .routers import items, users

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(items.router)


@app.get("/app_config")
def app_config():
    return get_app_config()


@app.get("/root")
def root():
    return {"message": "Hello"}


@app.post("/tasks", status_code=201)
def run_task(payload = Body(...)):
    task_type = payload["type"]

    task = create_task.apply_async(
        args=[int(task_type)],
        queue="task_queue"
    )

    return JSONResponse({"task_id": task.id})


@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id, app=celery_app)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)
import os
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    APP_ENV: str
    celery_broker: str
    celery_backend: str
    flower_broker_api: str
    flower_logging: str


class LocalConfig(BaseConfig):
    APP_ENV: str = "local"
    celery_broker: str = "amqp://admin:d418ae373cad@localhost:5672//"
    celery_backend: str = "redis://:ac1c24ef3149@localhost:6379/0"
    flower_broker_api: str = 'http://admin:d418ae373cad@localhost:15672/api/'
    flower_logging: str = 'DEBUG'


class LocalDockerConfig(BaseConfig):
    APP_ENV: str = "local-docker"
    celery_broker: str = "amqp://admin:d418ae373cad@rabbitmq:5672//"
    celery_backend: str = "redis://:ac1c24ef3149@redis:6379/0"
    flower_broker_api: str = 'http://admin:d418ae373cad@rabbitmq:15672/api/'
    flower_logging: str = 'DEBUG'


class DevConfig(BaseConfig):
    APP_ENV: str = "dev"
    celery_broker: str = "amqp://admin_dev:d418ae373cad@localhost:5672//"
    celery_backend: str = "redis://:ac1c24ef3149@localhost:6379/0"
    flower_broker_api: str = 'http://admin_dev:d418ae373cad@rabbitmq:15672/api/'
    flower_logging: str = 'DEBUG'


def get_app_config() -> BaseConfig:
    app_env = os.getenv("APP_ENV", "local")

    if app_env == "local":
        return LocalConfig()
    if app_env == "local_docker":
        return LocalDockerConfig()
    elif app_env == "dev":
        return DevConfig()

    return LocalConfig()

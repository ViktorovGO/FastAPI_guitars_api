from src.core.gunicorn.logger import GunicornLogger


def get_app_options(
    host: str,
    port: int,
    workers: int,
    timeout: int,
    log_level: str,
) -> dict:
    return {
        "accesslog": "-",
        "errorlog": "-",
        "loglevel": log_level,
        "logger_class": GunicornLogger,
        "bind": f"{host}:{port}",
        "workers": workers,
        "worker_class": "uvicorn.workers.UvicornWorker",
        "timeout": timeout,
    }

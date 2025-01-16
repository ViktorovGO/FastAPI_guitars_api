#!/usr/bin/env python

from src.core.gunicorn import Application, get_app_options
from src.main import app
from src.core import settings


def main():
    application = Application(
        app=app,
        options=get_app_options(
            host=settings.gunicorn.host,
            port=settings.gunicorn.port,
            workers=settings.gunicorn.workers,
            timeout=settings.gunicorn.timeout,
            log_level=settings.logging.log_level,
        ),
    )
    application.run()


if __name__ == "__main__":
    main()
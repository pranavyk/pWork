# flask-trials.py
import logging
import traceback

from app import app


def run_as_python_app():
    """"
    Called when the application is run as python webserver.py
    """
    try:
        if __name__ == "__main__":
            app.run(host="127.0.0.1", port=5000, debug=True)
    except Exception:
        message = F'Application failed due to ' \
                  F'an exception\n{traceback.format_exc()}'

        if 'logger' in globals():
            logging.error(message)
        else:
            print(F'ERROR: ' + message)

        exit(1)

    exit(0)


if __name__ == "__main__":
    run_as_python_app()
else:
    # Create app instance for gunicorn/other runner
    # app = get_web_app()
    pass

#!/bin/bash
source venv/bin/activate
#
# SIGTERM from Runit doesn't work if FLASK_DEBUG is set
#
#FLASK_DEBUG=1 FLASK_APP=app.py flask run --host=0.0.0.0 --port 5555
PYTHONUNBUFFERED=TRUE FLASK_APP=app.py flask run --host=0.0.0.0 --port 5555

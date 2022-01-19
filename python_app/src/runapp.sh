#!/bin/bash

# Collect static files
echo "Collect static files"
/opt/venv/bin/python3 manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
/opt/venv/bin/python3 manage.py migrate

# Start server
echo "Starting server"
/opt/venv/bin/python3 manage.py runserver 0.0.0.0:8000

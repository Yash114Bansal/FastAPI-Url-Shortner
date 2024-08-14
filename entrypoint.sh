#!/bin/sh

echo "Running DB migrations..."
alembic upgrade head


echo "Starting FastApiServer..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

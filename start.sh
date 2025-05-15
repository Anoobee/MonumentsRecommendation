#!/bin/bash

set -e

# Wait for MySQL
echo "⏳ Waiting for MySQL..."
until mysqladmin ping -h"$MYSQL_HOST" -P"$MYSQL_PORT" --silent; do
  sleep 1
done

# Run migrations
echo "🚀 Running Alembic migrations..."
alembic upgrade head

# Start FastAPI
echo "🌐 Starting FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

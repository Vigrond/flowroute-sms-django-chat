#!/bin/bash
#  Docker start script, called by docker-compose

# Check if database is ready

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" $POSTGRES_DB -c "\q"; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
echo "Postgres is ready.  Starting nginx+gunicorn..."

# ensure migrations
python3 flowchat/manage.py migrate

# start memcached
memcached -d -v -m 512 -u memcache

# Start our web server
nginx
gunicorn --pythonpath /code/flowchat --bind 0.0.0.0:8000  \
--log-config /code/docker/web/logging.conf \
--workers 8 --worker-class gthread --max-requests 5000 --max-requests-jitter 400 wsgi

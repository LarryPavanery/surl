#!/usr/bin/env bash

#up rethinkdb
rethinkdb --bind 0.0.0.0 --http-port 8080 &

#up application
gunicorn -k eventlet --worker-connections=2000 --backlog=1000 --paste etc/api-config.ini

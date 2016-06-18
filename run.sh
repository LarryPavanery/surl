#!/usr/bin/env bash

#up application
gunicorn -k eventlet --worker-connections=2000 --backlog=1000 --paste etc/api-config.ini

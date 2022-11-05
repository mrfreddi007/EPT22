#!/bin/bash
set -e

gunicorn --config gunicorn_config.py wsgi:app
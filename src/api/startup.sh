#!/bin/bash
gunicorn --chdir src/api app:app --bind 0.0.0.0:8000
#!/bin/bash
flask --app ./src/app/main.py:init_app run --debug -p 5005 --host 0.0.0.0

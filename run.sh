#!/bin/sh
SCRIPT_DIR=$(dirname "$(readlink -f "$0")")

python2 ${SCRIPT_DIR}/app.py

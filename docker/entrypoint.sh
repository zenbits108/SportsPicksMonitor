#!/bin/bash
set -e

# migrate DB if needed
python -m app.core.database --init

# start monitor
exec python -m app.main

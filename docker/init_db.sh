#!/bin/bash

# Database initialization script
python -c "from app.core.database import init_db; init_db()"
echo "Database initialized successfully"

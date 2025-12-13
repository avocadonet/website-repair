#!/bin/bash

echo "--- 1. Starting Docker Services (PostgreSQL + FastAPI) ---"
docker-compose up -d

echo ""
echo "Waiting 5 seconds for PostgreSQL and FastAPI containers to initialize..."
sleep 5

echo ""
echo "--- 2. Populating Database with Test Data ---"
docker-compose exec backend python populate_database.py

echo ""
echo "--- Backend Setup Complete ---"
echo "Backend services are running in the background (detached mode)."
echo "You can stop them with: docker-compose down"
#!/usr/bin/env bash

# Navigate to project root
cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Start Docker
echo "Starting Docker containers..."
docker compose up -d

# Start Flask in new terminal
gnome-terminal -- bash -c "cd backend && source ../venv/bin/activate && echo Starting Flask... && python app.py; exec bash" &

# Start Kafka Consumer in another terminal
gnome-terminal -- bash -c "cd backend && source ../venv/bin/activate && echo Starting Consumer... && python consumer.py; exec bash" &

echo "All services are starting..."
echo "Opening Webpage..."

xdg-open frontend/index.html
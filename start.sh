#!/bin/bash

echo "Starting DOcker services..."
docker compose up -d

echo "Activating virtual environment..."
source venv/bin/activate

echo "Starting Flask app..."
gnome-terminal -- bash -c "source venv/bin/activate && cd backend && python app.py"

echo "Starting Kafka consumer..."
gnome-terminal -- bash -c "source venv/bin/activate && cd backend && python consumer.py"
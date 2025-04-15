#!/usr/bin/env bash

echo "Stopping Webpage services..."

echo "Stopping Docker containers..."
docker compose down

echo "Stopping Flask and Consumer processes..."
pkill -f "python app.py"
pkill -f "python consumer.py"

echo "Shutdown complete. Please close the webpage if it's still open. See you next time!"

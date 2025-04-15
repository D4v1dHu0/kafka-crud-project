#!/usr/bin/env bash

# Activate virtual environment
source venv/bin/activate

# Start Docker containers
echo "Starting Docker containers..."
docker compose up -d

# Wait for Kafka to be ready
echo "Waiting for Kafka to be ready..."
KAFKA_READY=0
for i in {1..10}; do
  if nc -z localhost 9092; then
    KAFKA_READY=1
    break
  fi
  echo "Kafka not ready yet... waiting ($i/10)"
  sleep 2
done

if [ "$KAFKA_READY" -ne 1 ]; then
  echo "Kafka did not become ready in time. Exiting."
  exit 1
fi

echo "Kafka is ready!"

# Run consumer.py and app.py each in a new gnome-terminal window from the backend folder
gnome-terminal -- bash -c "cd backend && python3 consumer.py; exec bash" &
gnome-terminal -- bash -c "cd backend && python3 app.py; exec bash" &

# Open frontend in default browser
xdg-open frontend/index.html

echo "Startup complete!"
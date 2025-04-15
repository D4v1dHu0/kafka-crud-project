
# Kafka-CRUD-Project-Python

## Purpose

This project demonstrates skills developed during my internship, focusing on **Kafka**, **PostgreSQL**, and **Python**. It involves setting up a Kafka producer-consumer pipeline integrated with a PostgreSQL database and managing message CRUD operations through a REST API.

### Key Components
- **Python**: Main language used for scripting and interfacing with Kafka and PostgreSQL.
- **Kafka**: Manages the message queue with a producer-consumer model.
- **PostgreSQL**: Stores messages consumed from Kafka for persistent data storage.
- **Flask**: Used to create REST API endpoints for managing CRUD operations.

---

## Requirements

This project was developed on an Ubuntu virtual machine.

To run the project, ensure the following are installed:
- **Docker** (to containerize Kafka and PostgreSQL)
- **Python 3.11+**
- **Virtual Environment**

---

## Setup and Running the Project

### 1. Clone the Repository
```bash
git clone https://github.com/D4v1dHu0/kafka-crud-project.git
cd kafka-crud-project
```

### 2. Activate the Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Project
Use the provided script to simplify startup:
```bash
./start.sh
```
This script:
- Activates the virtual environment.
- Starts Docker Compose.
- Runs the Kafka consumer and Flask app in separate terminals.
- Opens the frontend in your default browser.

---

## Features
- **Message CRUD Operations**: Create, read, update, and delete messages through a simple web interface.
- **Real-Time Updates**: Messages update dynamically on the UI.
- **Kafka Integration**: Demonstrates a producer-consumer model for message handling.
- **Database Persistence**: Messages are stored in PostgreSQL for durability.

---

## Closing the Project
To shut down all running processes and clean up, close the webpage and use:
```bash
./stop.sh
```

This script:
- Stops the Kafka consumer and Flask app.
- Brings down Docker Compose containers.
- Deactivates the virtual environment.

---

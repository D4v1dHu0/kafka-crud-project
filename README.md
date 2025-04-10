# Kafka-CRUD-Project-Python

## Purpose

This project is designed to showcase skills learned in my internship, particularly working with **Kafka** and **PostgreSQL** in **Python**. THe project involves setting up a Kafka producer-consumer pipeline, integrating it with a POstgreSQL db, and managing msg CRUD operations using REST API.

Python - Main language used for scripting and to interact with Kafka, postgreSQL for simple CRUD.operation creation.
Kafka - Setting up a Kafka producer and consumer to handle msg queue.
PostgreSQL - Main db used to store msg from kafka.
REST API - Using FastAPI to create endpoints for CRUD operations on kafka msgs and db records.

## Requirements

This project is done on a vm with Ubuntu OS.

To run the project, you'll need:

Kafka
PostgreSQL
Python 3.11+
Virtual Environment

## Setup and RUnning the Project

1. Clone the repository:
 ***bash
 git clone https://github.com/D4v1dHu0/kafka-crud-project.git
cd kafka-crud-project
***

2. Activate Virtual Environment
 ***bash
python3 -m venv venv
source venv/bin/activate
***

3. Install required dependencies
***bash
pip install -r requirements.txt
***

4. Set up Kafka according to instructions locally.

5. Set up PostgresSQL and make sure db is up and running.

6. Create required PostgreSQL table for storing msgs
***sql
CREATE TABLE message(
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL
);
***

7. Run producer to send the message locally
***bash
python backend/producer.py
***

8. Run consumer to consume msg from producer and insert into PostgreSQL
***bash
python backend/consumer.py
***
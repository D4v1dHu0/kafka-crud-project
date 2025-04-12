from flask import Flask, request, jsonify
import sys
sys.path.insert(1,'../db')
import db

from flask_cors import CORS
from kafka import KafkaProducer
import json

app = Flask(__name__)
CORS(app)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', #check host name
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/produce', methods=['POST'])
def produce():
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    producer.send('messages', {'message': message})
    return jsonify({'status': 'Message sent to Kafka'})

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = db.get_all_messages()
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def add_messages():
    data = request.get_json()
    content = data.get('content')
    db.insert_message(content)
    return jsonify({'status': 'Message added'}), 201

@app.route('/messages<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    db.update_message(id, data['content'])
    return jsonify({'status' : 'Message updated'})

@app.route('/messages<int:id>', methods=['DELETE'])
def delete(id):
    db.delete_message(id)
    return jsonify({'status': 'Message deleted'})

if __name__ == '__main__':
    app.run(debug = True)
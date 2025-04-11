from flask import Flask, request, jsonify
import sys
sys.path.insert(1,'../db')
import db

app = flask(__name__)

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = db.get_all_messages()
    return jsonify(messages)

@app.route('/messages', methods=['POST'])
def add_messages():
    data = request.get_json
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
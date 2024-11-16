from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
import logging

app = Flask(__name__)
client = MongoClient(os.environ.get('MONGO_URI'))
db = client.chat_db
messages_collection = db.messages

def generate_chat_id(user1, user2):
    return ''.join(sorted([user1, user2]))

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    sender = data.get('sender')
    receiver = data.get('receiver')
    message = data.get('message')
    username = request.headers.get('x-logged-in-username')

    if username != sender:
        return jsonify({"message": "Unauthorized"}), 403

    chat_id = generate_chat_id(sender, receiver)

    messages_collection.insert_one({
        "chatId": chat_id,
        "sender": sender,
        "receiver": receiver,
        "message": message
    })
    return jsonify({"message": "Message sent successfully"}), 201

@app.route('/messages/<receiver>', methods=['GET'])
def get_messages(receiver):
    username = request.headers.get('x-logged-in-username')
    chat_id = generate_chat_id(username, receiver)
    messages = list(messages_collection.find({"chatId": chat_id}, {"_id": 0}))
    return jsonify(messages), 200

@app.route('/get-all-messages', methods=['GET'])
def get_all_messages():
    messages = list(messages_collection.find({}, {"_id": 0}))
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
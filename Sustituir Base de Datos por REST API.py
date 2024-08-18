from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_BASE_URL = 'https://api.example.com'

@app.route('/items', methods=['GET'])
def get_items():
    response = requests.get(f'{API_BASE_URL}/items')
    return jsonify(response.json())

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    response = requests.get(f'{API_BASE_URL}/items/{item_id}')
    return jsonify(response.json())

@app.route('/items', methods=['POST'])
def create_item():
    item_data = request.json
    response = requests.post(f'{API_BASE_URL}/items', json=item_data)
    return jsonify(response.json()), response.status_code

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item_data = request.json
    response = requests.put(f'{API_BASE_URL}/items/{item_id}', json=item_data)
    return jsonify(response.json()), response.status_code

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    response = requests.delete(f'{API_BASE_URL}/items/{item_id}')
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run()

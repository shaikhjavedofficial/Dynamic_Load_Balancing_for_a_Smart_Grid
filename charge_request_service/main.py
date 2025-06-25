from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
LOAD_BALANCER_URL = os.environ.get("LOAD_BALANCER_URL", "http://load_balancer:6000")

@app.route('/charge', methods=['POST'])
def charge():
    data = request.get_json()
    r = requests.post(f"{LOAD_BALANCER_URL}/route", json=data)
    return jsonify(r.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)

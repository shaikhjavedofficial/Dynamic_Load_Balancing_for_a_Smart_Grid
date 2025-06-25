from flask import Flask, request, jsonify
import threading
import os

app = Flask(__name__)
current_load = 0

@app.route('/charge', methods=['POST'])
def charge():
    global current_load
    current_load += 1
    # Simulate charging for 2 seconds
    threading.Timer(2, complete_charge).start()
    return jsonify({'status': 'charging', 'current_load': current_load})

def complete_charge():
    global current_load
    current_load -= 1

@app.route('/metrics', methods=['GET'])
def metrics():
    return f"current_load {current_load}\n"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8001))
    app.run(host='0.0.0.0', port=port)

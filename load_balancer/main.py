from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
SUBSTATION_URLS = os.environ.get("SUBSTATION_URLS", "http://substation1:8001,http://substation2:8002").split(',')

@app.route('/route', methods=['POST'])
def route():
    # Poll substations for their load
    loads = []
    for url in SUBSTATION_URLS:
        try:
            r = requests.get(f"{url}/metrics")
            load = int(r.text.split('current_load ')[1].split('\n')[0])
            loads.append(load)
        except:
            loads.append(9999)
    idx = loads.index(min(loads))
    # Forward the request to the least loaded substation
    r = requests.post(f"{SUBSTATION_URLS[idx]}/charge", json=request.get_json())
    return jsonify({'substation': idx+1, 'result': r.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

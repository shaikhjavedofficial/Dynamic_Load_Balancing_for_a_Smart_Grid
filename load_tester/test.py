import requests
import threading

def send_charge(i):
    r = requests.post("http://localhost:7000/charge", json={"vehicle_id": i})
    print(f"Request {i}: {r.json()}")

threads = []
for i in range(20):
    t = threading.Thread(target=send_charge, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

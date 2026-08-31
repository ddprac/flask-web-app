import socket
import time
from flask import Flask, jsonify

app = Flask(__name__)

is_ready = False
start_time = time.time()

@app.route('/')
def home():
    pod_name = socket.gethostname()
    # Ensure pod_name is a raw string, NOT wrapped in {}
    return {"status": "success", "served_by_pod": pod_name}

@app.route('/ready')
def ready():
    global is_ready
    if time.time() - start_time > 15:
        is_ready = True
        return jsonify({"status": "ready"}), 200
    else:
        return jsonify({"status": "starting up..."}), 503

@app.route('/live')
def live():
    # Crucial CKAD Fix: Standard string text, no extra curly braces!
    return jsonify({"status": "healthy"}), 200

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

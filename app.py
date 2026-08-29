import socket
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return{"status":"success", "message":"Hello, World! Flask is running"}
    
@app.route('/health')
def health():
    return{"Flask is running": True}

@app.route('/data')
def data():
    return{"This is the data route": True}

@app.route('/api')
def api():
    pod_name = socket.gethostname()
    return {
        "status": "success",
        "data": {
            "version": "1.0.0",
            "feature": "Ingress Testing API enabled"
        },
        "served_by_pod": pod_name
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
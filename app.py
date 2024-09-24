from flask import Flask, request, jsonify
import subprocess
import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="healthy")

@app.route('/date', methods=['GET'])
def current_date():
    return jsonify(date=datetime.datetime.now().isoformat())

@app.route('/print', methods=['POST'])
def print_request():
    return jsonify(request.json)

@app.route('/shell', methods=['POST'])
def kernel_version():
    kernel = subprocess.check_output(['uname', '-r']).decode('utf-8').strip()
    return jsonify(kernel_version=kernel)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


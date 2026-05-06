import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    return jsonify({"status": "pronto", "messaggio": "In attesa di specifiche"})

if __name__ == '__main__':
    # Render usa la variabile d'ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

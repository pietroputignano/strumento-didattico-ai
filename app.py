import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # Questa riga dice a Python di cercare il file templates/index.html
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_exercise():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    # Render ha bisogno che l'host sia 0.0.0.0
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

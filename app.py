import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate_exercise():
    data = request.json
    # Qui aggiungeremo la logica AI più avanti
    risposta_simulata = {
        "unite": "Unité 1",
        "titre_unite": "Le domino des objets",
        "titre_activite": "Le Domino",
        "livello_facile": {"consegna": "Associe", "elementi": ["lit", "table"]},
        "livello_difficile": {"consegna": "Lettres", "elementi": ["lit", "table"]}
    }
    return jsonify(risposta_simulata)

@app.route('/')
def home():
    return "Il server è attivo e pronto!"

if __name__ == '__main__':
    # IMPORTANTE: Render assegna una porta variabile, dobbiamo leggerla così:
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

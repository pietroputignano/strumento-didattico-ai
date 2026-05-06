from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Questo permette al frontend di comunicare con il backend

# Questa è la "mappa" di base di un esercizio. 
# Quando incollerai il testo dell'Unité 1, l'AI riempirà questi campi.
@app.route('/generate', methods=['POST'])
def generate_exercise():
    data = request.json
    testo_utente = data.get('testo')
    
    # Per ora simuliamo la risposta dell'AI per testare se tutto funziona.
    # In seguito collegheremo le API di OpenAI qui.
    risposta_simulata = {
        "unite": "Unité 1",
        "titre_unite": "Le domino des objets de la chambre",
        "titre_activite": "Le Domino",
        "livello_facile": {
            "consegna": "Lis et déplace les dominos.",
            "elementi": ["l'armoire", "la couette", "la fenêtre", "la lampe"]
        },
        "livello_difficile": {
            "consegna": "Regarde i dominos et mets les lettres dans le bon ordre.",
            "elementi": ["l'armoire", "la couette", "la fenêtre", "la lampe"]
        }
    }
    return jsonify(risposta_simulata)

@app.route('/')
def home():
    return "Il server è attivo! Pronto per generare esercizi."

if __name__ == '__main__':
    app.run(debug=True, port=5000)

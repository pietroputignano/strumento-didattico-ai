import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

# Inizializzazione sicura del client OpenAI
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_exercise():
    if not client:
        return jsonify({"error": "Chiave API non configurata su Render"}), 500
    
    try:
        data = request.json
        testo_utente = data.get('testo', '')

        prompt = f"""
        Sei un esperto di FLE. Analizza il testo e crea un JSON per un esercizio.
        Testo: {testo_utente}
        
        Rispondi ESCLUSIVAMENTE con un oggetto JSON strutturato così:
        {{
          "unite": "Titolo completo riga 1",
          "titre_activite": "Titolo riga 2",
          "items": ["parola 1", "parola 2"],
          "livello_facile": {{"consigne": "istruzione facile"}},
          "livello_difficile": {{"consigne": "istruzione difficile"}}
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Sei un assistente che genera solo JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

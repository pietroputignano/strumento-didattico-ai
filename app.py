import os
import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_exercise():
    try:
        testo_utente = request.json.get('testo', '')
        prompt = f"""
        Genera un JSON per un esercizio FLE. 
        Testo: {testo_utente}
        REGOLE:
        - unite: Titolo completo Unità (es. Unité 1 : ...)
        - titre_activite: Nome dell'attività
        - items: lista dei vocaboli
        - consigne_f: consegna facile
        - consigne_d: consegna difficile
        """
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "Rispondi SOLO in JSON."},
                      {"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        
        # Pulizia del risultato
        return response.choices[0].message.content
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

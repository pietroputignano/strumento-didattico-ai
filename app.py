import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI # Importiamo il cliente OpenAI

app = Flask(__name__)
CORS(app)

# Recuperiamo la chiave segreta in modo sicuro da Render
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_exercise():
    testo_utente = request.json.get('testo')
    
    prompt = f"""
    Sei un esperto sviluppatore di risorse didattiche FLE per Hachette.
    Analizza questo testo e trasforma tutto in un file JSON preciso.
    TESTO: {testo_utente}

    STRUTTURA JSON RICHIESTA (NON AGGIUNGERE ALTRO TESTO):
    {{
      "unite": "Testo completo della riga 1 (es: Unité 1 : Le domino...)",
      "titre_activite": "Titolo della riga 2",
      "items": ["parola1", "parola2", "parola3", "..."],
      "livello_facile": {{
          "consigne": "Testo della consegna facile",
          "tipo": "drag_and_drop"
      }},
      "livello_difficile": {{
          "consigne": "Testo della consegna difficile",
          "tipo": "anagramma"
      }}
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "Rispondi solo in formato JSON puro."},
                      {"role": "user", "content": prompt}],
            response_format={ "type": "json_object" } # Obbliga l'AI a dare JSON
        )
        return response.choices[0].message.content
    except Exception as e:
        return jsonify({"error": str(e)}), 500

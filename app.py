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
    
    # Questo è il "Prompt": l'istruzione che diamo all'AI
    prompt = f"""
    Trasforma il seguente testo in un esercizio interattivo per bambini (scuola primaria).
    Restituisci SOLO un file JSON con questa struttura:
    {{
      "unite": "numero unita",
      "titre_unite": "titolo",
      "titre_activite": "titolo attivita",
      "items": ["lista degli elementi"],
      "consigne_facile": "istruzione",
      "consigne_difficile": "istruzione"
    }}
    Testo: {testo_utente}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Il modello più avanzato
            messages=[{"role": "user", "content": prompt}]
        )
        # Qui l'AI ci risponde e noi mandiamo il risultato al tuo schermo
        return response.choices[0].message.content
    except Exception as e:
        return jsonify({{"error": str(e)}}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/parse_text', methods=['POST'])
def parse_text():
    try:
        testo_utente = request.json.get('testo', '')
        
        prompt = f"""
        Analizza questo testo didattico e compila i campi per un esercizio.
        TESTO: {testo_utente}
        
        RESTITUISCI SOLO JSON:
        {{
          "unite": "Numero e titolo unità",
          "consigne_f": "Consegna per il livello facile",
          "consigne_d": "Consegna per il livello difficile",
          "items": "lista parole separate da punto e virgola"
        }}
        """

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": "Sei un assistente che estrae dati didattici in JSON."},
                      {"role": "user", "content": prompt}],
            response_format={ "type": "json_object" }
        )
        return response.choices[0].message.content
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

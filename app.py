from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "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"

@app.route("/api", methods=["POST"])
def tutor():
    data = request.json
    message = data.get("message")

    if not message:
        return jsonify({"reply": "Please ask something."})

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful AI tutor."},
                    {"role": "user", "content": message}
                ]
            }
        )

        result = response.json()
        reply = result["choices"][0]["message"]["content"]

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
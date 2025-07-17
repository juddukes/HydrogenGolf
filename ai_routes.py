import os
import openai
from flask import Blueprint, request, jsonify

ai_bp = Blueprint("ai_bp", __name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@ai_bp.route("/api/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        print("Received data:", data)

        prompt = data.get("prompt", "").strip()
        if not prompt:
            print("Error: empty prompt")
            return jsonify({"error": "Prompt is empty"}), 400

        print("Sending prompt to OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message["content"]
        print("OpenAI response:", reply)

        return jsonify({"reply": reply})

    except Exception as e:
        print("🔥 Exception in /api/ask:", str(e))
        return jsonify({"error": str(e)}), 500

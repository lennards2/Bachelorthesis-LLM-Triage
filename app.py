import os
from flask import Flask, jsonify, render_template, request
import openai
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

OPENAI_API_KEY = os.environ["KEY"]

openai.api_key = OPENAI_API_KEY


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/session")
def session():
    print("Sending request to OpenAI API...", flush=True)
    url = "https://api.openai.com/v1/realtime/sessions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    json_data = {
        "model": "gpt-4o-realtime-preview-2024-12-17",
        "voice": "verse"
    }
    response = requests.post(url, headers=headers, json=json_data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)

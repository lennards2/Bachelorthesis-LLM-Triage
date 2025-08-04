import os
from flask import Flask, jsonify, render_template, request
import openai
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Retrieve OpenAI API key from environment variables
# This key is required for authenticating with OpenAI's Realtime API
OPENAI_API_KEY = os.environ["KEY"]

openai.api_key = OPENAI_API_KEY

#Serve the main application page
@app.route("/")
def index():
    return render_template("index.html")

#Create and return an ephemeral session token for OpenAI API
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
    # Return token to frontend
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, jsonify
import openai
import os
from google import genai
import requests 
from dotenv import load_dotenv

load_dotenv()

googleAi_api = os.getenv("GEMINI_API")

app = Flask(__name__)
client = genai.Client(api_key=googleAi_api)


    
@app.route('/<string:data>')
def index(data):
    if data == "f1" or data == "formula 1":        
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = "give me information related to formula 1"
        )
        return jsonify(response.to_json_dict()), 200
    else:
        return jsonify({'status': "err"}), 400
        

if __name__ == "__main__":
    app.run(port=3005, debug=True)
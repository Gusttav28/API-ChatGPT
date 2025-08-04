from flask import Flask, render_template, jsonify
import openai
import os
from google import genai
import requests 

googleAi_api = "AIzaSyAHna1iK7P0UM2xiytply01AslHoFoNUcg"

app = Flask(__name__)
client = genai.Client(api_key=googleAi_api)

openai.api_key = "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"


    
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
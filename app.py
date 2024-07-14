from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from flask_cors import CORS  
import json 
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


genai.configure(api_key=gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_palette', methods=['POST'])
def generate_palette():
    data = request.get_json(force=True)
    skin_color = data.get('skin_color', '#D6A77A')
    cool_undertone = data.get('cool_undertone', True)

    prompt = f"""
    I have a skin color with hex code {skin_color} and a cool undertone. Provide me with a personalized color palette that would look good on my skin. The output should be an array of hex codes, including primary colors, accent colors, and neutral colors suitable for clothing and accessories. Here are the requirements:
    1. Primary Colors: Include 5 colors that will be the main part of the outfit.
    2. Accent Colors: Include 5 colors that will add a pop of color to the outfit.
    3. Neutral Colors: Include 5 colors that will complement the outfit.
    Only output the result in the JSON format below:
    {{
        "primary": [
            "#hexcode1",
            "#hexcode2",
            "#hexcode3",
            "#hexcode4",
            "#hexcode5"
        ],
        "accent": [
            "#hexcode1",
            "#hexcode2",
            "#hexcode3",
            "#hexcode4",
            "#hexcode5"
        ],
        "neutral": [
            "#hexcode1",
            "#hexcode2",
            "#hexcode3",
            "#hexcode4",
            "#hexcode5"
        ]
    }}
    Do not include any other text or explanation, only the JSON.
    """

    response = model.generate_content(prompt)
    
   
    try:
        color_palette = response.text.strip()
      
        palette_json = json.loads(color_palette)
    except json.JSONDecodeError:
        palette_json = {"error": "Failed to parse the response as JSON"}
    
    return jsonify(palette_json)

@app.route('/measurements', methods=['POST'])
def receive_measurements():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    print("Received measurements:", data)

    return jsonify({"message": "Measurements received successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, jsonify, render_template
from dotenv import load_dotenv
import requests
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Retrieve API key from the environment variable
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')  # This will render a single-page HTML with JS to handle image display.

@app.route('/get-image')
def get_image():
    # Get the current day and format it
    current_day = datetime.now().strftime("%A, %B %d, %Y")

    # Set up the image prompt including the current day
    prompt = f"Perro salchicha gordo bachicha toma solcito a la orilla del mar tiene sombrero de marinero y en vez de traje se puso collar with text saying {current_day}"

    # Make the API call to OpenAI
    response = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json',
        },
        json={
            "model": "dall-e-3",
            "prompt": prompt,
            "size": "1024x1024",
            "quality": "standard",
            "n": 1
        }
    )
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        image_url = data['data'][0]['url']
        return jsonify({'image_url': image_url})
    else:
        return jsonify({'error': 'Could not fetch the image'}), 500

if __name__ == '__main__':
    app.run(debug=True)

# app.py

from flask import Flask, request, jsonify, render_template
import os
import openai

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_type = "azure"
openai.api_base = "https://test-onetwothree-openai.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.environ['OPENAI_API_KEY']
                            
@app.route("/", methods=["GET"])
def home():
    # Render the index.html template
    return render_template("index.html")

# Define a route for handling incoming chat messages
@app.route('/', methods=['POST'])
def index():
    # Get the message from the request body
    message = request.form['text']

    # Call the OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        engine="newturbs",
        prompt=message,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    # Extract the response text from the API response
    response = response.choices[0].text.strip()

    # Return the response as a JSON object
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
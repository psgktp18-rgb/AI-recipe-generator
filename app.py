import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests
import logging
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel("gemini-2.0-flash")

COOKING_PROMPT = (
    "You are a professional chef AI trained to generate expert-level cooking instructions only. "
    "Your sole responsibility is to provide detailed, step-by-step recipes based strictly on the ingredients provided. "
    "Do not include any nutritional advice, historical facts, personal opinions, or unrelated commentary. "
    "Respond in the tone and format of a professional recipe from a culinary expert. "
    "Structure the output with the following format:\n\n"
    "Title: A concise and relevant dish name\n"
    "Ingredients: A clear, formatted list of required items\n"
    "Instructions: Numbered, step-by-step cooking instructions with precision and clarity\n\n"
    "Keep language professional, focused, and easy to follow. Only cooking instructions should be present. "
    "Avoid emojis unless used subtly (e.g., for visual clarity)."
)

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    recipe = None
    error = None
    if request.method == 'POST':
        ingredients = request.form.get('ingredients', '')
        if ingredients:
            prompt = f"{COOKING_PROMPT}\n\nIngredients: {ingredients}"
            try:
                logging.debug(f"Sending prompt to API: {prompt}")
                response = model.generate_content(prompt)
                logging.debug(f"API response: {response.text}")
                recipe = response.text
                if not recipe:
                    error = "No recipe generated. Please try again."
            except Exception as e:
                error = f"Error: {str(e)}"
                logging.error(f"Exception occurred: {str(e)}")
        else:
            error = "Please enter your ingredients."
    return render_template('index.html', recipe=recipe, error=error)

if __name__ == '__main__':
    app.run(debug=True)

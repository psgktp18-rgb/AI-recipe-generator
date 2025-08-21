# AI Recipe Generator

This is a Flask-based web application that generates recipes based on user-provided ingredients using a lightweight Gemini model API.

## Features
- User-friendly interface to input ingredients.
- AI-generated recipes displayed in a structured Markdown format.
- Uses Flask for the backend and Bootstrap for styling.

## Requirements
- Python 3.12 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/psgktp18-rgb/AI-recipe-generator.git
   cd AI-recipe-generator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up the `.env` file:
   - Create a `.env` file in the root directory.
   - Add your Gemini API key:
     ```env
     GEMINI_API_KEY=your_api_key_here
     ```
6. Create new folder named `templates`
   - Move the index.html to templates folder
     
## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```





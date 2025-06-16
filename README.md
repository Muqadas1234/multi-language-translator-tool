#  Language Translator Web App

This is a simple web-based language translator built using **Flask (Python)** on the backend and **HTML/CSS** on the frontend. It utilizes **Microsoft Azure Translator Text API** to translate input text into multiple target languages.

---

##  Features

- Translate text into 9 languages including:
  - English, Spanish, French, German, Chinese (Simplified), Arabic, Hindi, Sindhi, Urdu
- Clean and responsive UI
- Built with Flask, HTML, and CSS
- Handles API errors gracefully

---

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Translation Service**: Microsoft Azure Cognitive Services (Translator Text API)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/language-translator-flask.git
cd language-translator-flask



2. Install Dependencies
pip install flask requests


3. Set Up Azure Translator API
Go to Azure Portal

Create a Translator resource
Copy your API key and endpoint
Replace them in app.py:

API_KEY = "your_api_key_here"
ENDPOINT = "https://api.cognitive.microsofttranslator.com/"
LOCATION = "your_region"  # e.g., eastus


4. Run the App
python app.py


from flask import Flask, render_template, request
import requests, uuid

app = Flask(__name__)

API_KEY = "FMUKkmI3xZrFQjc9REGiIS5kHd6t0dzjAnHeHjRnmPg8t2HPgCVlJQQJ99BEACYeBjFXJ3w3AAAbACOGS3gs"
ENDPOINT = "https://api.cognitive.microsofttranslator.com/"
LOCATION = "eastus"  # e.g., centralindia

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        to_lang = request.form["language"]

        path = '/translate?api-version=3.0'
        params = f"&to={to_lang}"
        constructed_url = ENDPOINT + path + params

        headers = {
            'Ocp-Apim-Subscription-Key': API_KEY,
            'Ocp-Apim-Subscription-Region': LOCATION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        body = [{'text': text}]

        try:
            response = requests.post(constructed_url, headers=headers, json=body)
            result = response.json()
            translated_text = result[0]["translations"][0]["text"]
        except Exception as e:
            translated_text = f"Error: {e}"

    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)

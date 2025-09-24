from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests  # to forward requests to backend

app = Flask(__name__, template_folder="templates")
CORS(app)  # enable cross-origin requests

# Backend URL (your backend running on port 5000)
BACKEND_URL = "http://127.0.0.1:5000/submittodoitem"

# Serve the frontend page
@app.route('/')
def index():
    return render_template("index.html")

# Handle form submission and send data to backend
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    
    

    
    response = requests.post(BACKEND_URL, data=form_data)
    return response.text
  

if __name__ == "__main__":
    app.run(port=3000, debug=True)

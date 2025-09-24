from flask import Flask, request
from dotenv import load_dotenv

from pymongo import MongoClient
import os

app = Flask(__name__)

load_dotenv()

client = MongoClient(os.getenv("uri"))
db = client.test
collection=db['flask_db']

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    form_data = dict(request.form)
    collection.insert_one(form_data)

    return "data submitted successfully to database from backend "

if __name__ == "__main__":
    app.run(port=5000, debug=True)

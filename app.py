from flask import Flask, request, jsonify, Response
import json
import db
from controller import get_data, create_data
app = Flask(__name__)

##############################


@app.route('/', methods=["POST"])
def create_user():
    return create_data()

##############################


@app.route('/', methods=["GET"])
def get_user():
    return get_data()

##############################


if __name__ == "__main__":
    app.run(debug=True, port=8000)

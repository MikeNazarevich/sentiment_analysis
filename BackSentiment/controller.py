from flask import request, abort, jsonify
from app import app
from service import get_sentiment

@app.route('/all', methods=['GET'])
def get_tasks():
    return 'kek'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_record', methods=['POST'])
def get_record():
    # if not request.json or not 'title' in request.json:
    #     abort(400)
    record = request.json("record")
    print(request.is_json)
    print(record)
    get_sentiment(record)
    return jsonify(record), 201

from flask import Flask
from flask_cors import CORS
from flask import request, abort, jsonify
import json
from service import get_sentiment

app = Flask(__name__)
cors = CORS(app)


@app.route('/all', methods=['GET'])
def get_tasks():
    return 'kek'

@app.route('/', methods=['GET'])
def hello_world():
    return 'helllo'

@app.route('/get_record', methods=['POST'])
def get_record():
    record = request.json["record"]
    lol = get_sentiment(record)
    print(lol)
    return jsonify(lol)


if __name__ == '__main__':
    app.run()




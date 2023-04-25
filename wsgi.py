import json
from flask import Flask, jsonify, request
from src.models.predict_model import predict

application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/predictions', methods=['POST'])
def create_prediction():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body))

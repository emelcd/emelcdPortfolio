from flask import Flask, render_template, jsonify
from os import environ
from uuid import uuid4
import json

api_key = environ.get('API_KEY')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(template_name_or_list='index.html')

@app.route('/msg')
def about():
    with open('msg.json', 'r') as f:
        msg = json.load(f)
    
    msg[str(uuid4())] = {
        'msg': 'Hello World!',
        'name': api_key
    }

    with open('msg.json', 'w') as f:
        json.dump(msg, f)

    return jsonify(msg)


if __name__ == '__main__':
    app.run(debug=True)
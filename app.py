from flask import Flask, jsonify

app = Flask(__name__)


app.config['SECRET_KEY'] = '1892434ad187b9bb4fd163fbaa6f0ec7'

@app.route('/')
def home():
    return jsonify('food APi')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
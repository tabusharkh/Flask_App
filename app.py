from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/')
def index():
    return "Hello World!"


@app.route('/api/get_data', methods=['GET'])
def get_output():
    object= {"output_text" : "some text",
             "output_type" : "text"}
    return jsonify(object)


@app.route('/api/request', methods=['POST'])
def get_request():
    return request.json


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/controller', methods=['POST'])
def controller():
    if request.method == 'POST':
        with open("move.json", "w") as outfile:
            json.dump(request.form, outfile)
        return 'Posted New Movement!', 204

@app.route('/nextmove', methods=['GET'])
def nextmove():
    if request.method == 'GET':
        return open('move.json', mode='r')

if __name__ == '__main__':
    app.run(
        host='localhost',
        port=5001,
    )
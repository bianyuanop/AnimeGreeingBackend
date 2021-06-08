from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=('POST',))
def upload():
    return json.dumps({'status': 200})

if __name__ == '__main__':
    app.run()
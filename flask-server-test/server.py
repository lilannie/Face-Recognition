from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/imgsave', methods = ['POST'])
def hii():
	print request.form['base64URL']
	return request.data

@app.route('/')
def hello_world():
    return app.send_static_file('flask_client.html')
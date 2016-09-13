from flask import Flask
from flask import request
import base64
app = Flask(__name__)

@app.route('/imgsave', methods = ['POST'])
def decode():
	imgdata = request.form['base64URL']
	print imgdata
	fh = open("imageToSave.png", "wb")
	print len(imgdata) % 4
	fh.write(base64.b64decode(imgdata + '=' * (4 - len(imgdata) % 4)))
	fh.close()

	return request.data

@app.route('/')
def hello_world():
    return app.send_static_file('flask_client.html')

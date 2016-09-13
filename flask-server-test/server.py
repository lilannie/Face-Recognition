from flask import Flask
from flask import request
import base64
app = Flask(__name__)

@app.route('/imgsave', methods = ['POST'])
def decode():
	imgdata = request.form['base64URL']
	imgdata = imgdata.replace("data:image/png;base64,", "")
	imgdata = base64.b64decode(imgdata)
	filename = 'face.jpg'
	with open(filename, 'wb') as f:
  			f.write(imgdata)

	return request.data

@app.route('/')
def hello_world():
    return app.send_static_file('flask_client.html')

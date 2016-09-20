from flask import Flask
from flask import request
import base64
import cv2, os
import numpy as np
from PIL import Image
app = Flask(__name__)

@app.route('/imgsave', methods = ['POST'])
def decode():
	imgdata = request.form['base64URL']
	imgdata = imgdata.replace("data:image/png;base64,", "")
	imgdata = base64.b64decode(imgdata)
	filename = './yalefaces/subject14.sad'
	with open(filename, 'wb') as f:
  			f.write(imgdata)
 	match_faces();

	return request.data

@app.route('/')
def hello_world():
    return app.send_static_file('flask_client.html')

def match_faces():
	# For face detection we will use the Haar Cascade provided by OpenCV.
	cascadePath = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascadePath)

	# For face recognition we will the the LBPH Face Recognizer 
	recognizer = cv2.createLBPHFaceRecognizer()

	images = None
	labels = None

	# Path to the Dataset
	path = './yalefaces'

	image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.sad')]
  	images = []
  	labels = []
  	for image_path in image_paths:
    # Read the image and convert to grayscale
  			image_pil = Image.open(image_path).convert('L')
    # Convert the image format into numpy array
	  		image = np.array(image_pil, 'uint8')
    # Get the label of the image
	  		nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
    # Detect the face in the image
	  		faces = faceCascade.detectMultiScale(image)
    # If face is detected, append the face to images and the label to labels
	  		for (x, y, w, h) in faces:
		      		images.append(image[y: y + h, x: x + w])
	      		labels.append(nbr)
	      		cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
	      		cv2.waitKey(20)

	print "training"
	# Call the get_images_and_labels function and get the face images and the 
	# corresponding labels
	# images, labels = get_images_and_labels(path)

	cv2.destroyAllWindows()

	# Perform the tranining
	recognizer.train(images, np.array(labels))
	print "trained"

	# Append the images with the extension .happy into image_paths
	image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]

	for image_path in image_paths:
	    predict_image_pil = Image.open(image_path).convert('L')
	    predict_image = np.array(predict_image_pil, 'uint8')
	    faces = faceCascade.detectMultiScale(predict_image)
	    for (x, y, w, h) in faces:
	        nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
	        nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
	        if nbr_actual == nbr_predicted:
	            print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
	        else:
	            print "{} is Incorrect Recognized as {}".format(nbr_actual, nbr_predicted)
	        cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
	        cv2.waitKey(1000)
# example of loading the keras facenet model
import tensorflow as tf
from tensorflow import keras
# load the model
model = tf.keras.models.load_model('facenet_keras.h5')
# summarize input and output shape
print(model.inputs)
print(model.outputs)

# # confirm mtcnn was installed correctly
# import mtcnn
# # print version
# print(mtcnn.__version__)

# # function for face detection with mtcnn
# from PIL import Image
# from numpy import asarray
# from mtcnn.mtcnn import MTCNN
 
# # extract a single face from a given photograph
# def extract_face(filename, required_size=(160, 160)):
# 	# load image from file
# 	image = Image.open(filename)
# 	# convert to RGB, if needed
# 	image = image.convert('RGB')
# 	# convert to array
# 	pixels = asarray(image)
# 	# create the detector, using default weights
# 	detector = MTCNN()
# 	# detect faces in the image
# 	results = detector.detect_faces(pixels)
# 	# extract the bounding box from the first face
# 	x1, y1, width, height = results[0]['box']
# 	# bug fix
# 	x1, y1 = abs(x1), abs(y1)
# 	x2, y2 = x1 + width, y1 + height
# 	# extract the face
# 	face = pixels[y1:y2, x1:x2]
# 	# resize pixels to the model size
# 	image = Image.fromarray(face)
# 	image = image.resize(required_size)
# 	face_array = asarray(image)
# 	return face_array
 
# # load the photo and extract the face
# pixels = extract_face("C:/Users/ASUSKIM/Desktop/AR/New folder/image/Lin Yi/300px-Lin_Yi.jpg")
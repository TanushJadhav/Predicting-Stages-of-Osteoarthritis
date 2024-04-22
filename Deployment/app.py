from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2

app = Flask(__name__)
CORS(app)

# Load the model
# model = tf.keras.models.load_model('path_to_your_model.h5')

# Compile the model
# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Preprocess the Input Image
def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    image=cv2.resize(gray,(224,224))
    return image

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    image_file = request.files['image']
    
    # Open the image using PIL
    image = Image.open(image_file)
    
    # Preprocess the image
    image = preprocess_image(image)
    
    # Make predictions using the model
    # predictions = model.predict(np.expand_dims(image, axis=0))
    
    # Get the predicted class
    # predicted_class = np.argmax(predictions)
    
    # Return the predicted class as JSON response
    # response = {'predicted_class': predicted_class}
    response = {'predicted_class': 2}
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import model_from_json
import  io

app = Flask(__name__)
CORS(app)

# Load the model
file = open("Model/model2.json", 'r')
loaded = file.read()

model = model_from_json(loaded)
model.load_weights("Model/model2.h5")

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Preprocess the Input Image
def preprocess_image(image):
    # img = load_img(image, target_size=(224, 224), color_mode="grayscale")
    img = load_img(io.BytesIO(image.read()), target_size=(224, 224), color_mode="grayscale")
    img_array = img_to_array(img)
    img =  img_array/255.0
    return img

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    image_file = request.files['image']
    
    # Preprocess the image
    image = preprocess_image(image_file)
    
    # Make predictions using the model
    predictions = model.predict(np.expand_dims(image, axis=0))
    print(predictions)
    # Get the predicted class
    predicted_class = np.argmax(predictions)
    predicted_class = int(predicted_class)

    # Return the predicted class as JSON response
    response = {'predicted_class': predicted_class}
    print(predicted_class)
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
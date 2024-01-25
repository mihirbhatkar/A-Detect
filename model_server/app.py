from flask import Flask, request, jsonify
from fastai.vision.all import *
from flask_cors import CORS

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
CORS(app)  

# Load the trained model
learn = load_learner('alzh-fastai.pkl')
pathlib.PosixPath = temp

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the request has a file in 'image' key
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']

    # Ensure the file has an allowed extension
    # if not image_file or not allowed_file(image_file.filename):
    #     return jsonify({'error': 'Invalid file format'})

    # Perform inference on the received image
    img = PILImage.create(image_file)
    prediction, _, _ = learn.predict(img)

    return jsonify({'prediction': str(prediction)})

# def allowed_file(filename):
#     # Define the allowed file extensions
#     allowed_extensions = {'png', 'jpg', 'jpeg'}
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

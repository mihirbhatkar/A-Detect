from flask import Flask, request, jsonify
from fastai.vision.all import *
from flask_cors import CORS

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)
CORS(app)

# Load the trained model
learn = load_learner('resnet50.pkl')
pathlib.PosixPath = temp

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']

    img = PILImage.create(image_file)
    prediction, idx, probs = learn.predict(img)
    
    class_probs = {learn.dls.vocab[i]: float(probs[i]) for i in range(len(probs))}
    print(class_probs)

    return jsonify({
        'prediction': str(prediction),
        'class_probabilities': class_probs
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
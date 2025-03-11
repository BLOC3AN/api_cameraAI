from flask import Flask, request, jsonify
import os
from predict import process_image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part in the request'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        image_path = os.path.join('./static', 'temp.png')
        file.save(image_path)
        predicted_text = process_image(image_path)
        return jsonify({'predicted_text': predicted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

#curl -X POST -F 'image=@/path/to/your/image.jpg' http://localhost:5000/predict
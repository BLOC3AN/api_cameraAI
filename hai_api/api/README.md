# Image Text API

This project is an API that accepts an image, processes it to extract text using a pre-trained model, and returns the predicted text as a response. It utilizes Flask for the web framework and EasyOCR for text extraction.

## Project Structure

```
image-text-api
├── src
│   ├── app.py                # Entry point of the API application
│   ├── predict.py            # Logic for processing images and extracting text
│   ├── models
│   │   └── wpod-net_update1.json  # Pre-trained model data for license plate detection
│   ├── static
│   │   └── temp.png          # Temporary storage for processed images
│   └── templates              # Directory for HTML templates (if needed)
├── requirements.txt           # List of dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd image-text-api
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the API:**
   Start the Flask application by running:
   ```
   python src/app.py
   ```
   The API will be available at `http://127.0.0.1:5000`.

## Usage

To use the API, send a POST request to the `/upload` endpoint with an image file. The API will process the image and return the extracted text.

### Example Request

```bash
curl -X POST -F "image=@path_to_your_image.jpg" http://127.0.0.1:5000/upload
```

### Example Response

```json
{
  "predicted_text": "Your extracted text here"
}
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

# curl -X POST -F 'image=@/home/hailt/project_STKENG/OCR_segmentation/MiAI_LP_Detection_2/test/xemay.jpg'  http://127.0.0.1:5000/upload

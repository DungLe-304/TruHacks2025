from flask import Flask, request, jsonify
import os
from pred_disease_name import predict_disease
from weather_to_disease import get_weather_and_predict_diseases


app = Flask(__name__)

# dir to save
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return 'this is a GET request.'


# use tomato image only
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # save file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "file_path": file_path})

# use tomato image only
@app.route('/predict_leaf_disease', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    # get client's image
    image = request.files['image']
    
    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # save image on server
    image_path = os.path.join("uploads", image.filename)
    os.makedirs("uploads", exist_ok=True)
    image.save(image_path)

    # predict & get advice
    predicted_disease, treatment, chemical = predict_disease(image_path)

    return jsonify({
        "predicted_disease": predicted_disease,
        "treatment": treatment,
        "chemical": chemical
    })

# tonny가 쓴거 integrate함. 체크할것
@app.route('/weather_disease', methods=['GET'])
def weather_disease():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')

    avg_temp, avg_humidity, total_precip, diseases = get_weather_and_predict_diseases(latitude, longitude)

    return jsonify({
        "avg_temp": avg_temp,
        "avg_humidity": avg_humidity,
        "total_precip": total_precip,
        "predicted_diseases": diseases
    })



if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)


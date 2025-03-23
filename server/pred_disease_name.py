import torch
from torchvision import transforms
from PIL import Image
import json

# load model & use cpu (colab has gpu)
device = torch.device('cpu')
model = torch.load('best_model.pth', map_location=device, weights_only=False)
model.eval()




# load class names
with open('class_names.json', 'r') as f:
    class_names = json.load(f)

# image transformations
transform = transforms.Compose([
    transforms.Resize(128),
    transforms.CenterCrop(128),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

])

# treatment recommendations
disease_treatments = {
    # apple
    'Apple___Apple_scab': 'Apply fungicides like captan or myclobutanil. Rake and destroy fallen leaves.',
    'Apple___Black_rot': 'Apply fungicides like captan or myclobutanil. Rake and destroy fallen leaves.',
    'Apple___Cedar_appe_rust': 'Apply fungicides like captan or myclobutanil. Rake and destroy fallen leaves.',
    'Apple___healthy': 'No treatment needed. Continue regular care.',
    # corn
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 'Use resistant varieties and apply fungicides if necessary.',
    'Corn_(maize)___Common_rust': 'Use resistant varieties and apply fungicides if necessary.',
    'Corn_(maize)___healthy': 'No treatment needed. Continue regular care.',
    'Corn_(maize)___Northern_Leaf_Blight': 'Use resistant varieties and apply fungicides if necessary.',
    # tomato
    "Tomato___Bacterial_Spot": "Apply copper-based bactericides. Remove and destroy infected plant debris. Practice crop rotation to reduce bacterial spread.",
    "Tomato___Early_Blight": "Apply fungicides like chlorothalonil or mancozeb. Prune affected leaves and practice good air circulation around plants.",
    "Tomato___Late_Blight": "Use fungicides like chlorothalonil or copper-based fungicides. Remove infected plants immediately and avoid overhead irrigation.",
    "Tomato___Leaf_Mold": "Apply fungicides containing chlorothalonil or copper. Prune and destroy affected leaves to improve air circulation.",
    "Tomato___Septoria_Leaf_Spot": "Apply fungicides such as mancozeb or chlorothalonil. Remove and destroy affected leaves. Ensure proper spacing between plants.",
    "Tomato___Spider_Mites_Two-Spotted_Spider_Mite": "Use miticides or insecticidal soaps. Prune affected areas and maintain good plant hygiene. Water plants regularly to prevent mites.",
    "Tomato___Target_Spot": "Apply fungicides like azoxystrobin or chlorothalonil. Remove infected leaves and avoid overhead watering.",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Remove and destroy infected plants immediately. Control whiteflies, the main vector for the virus, with insecticides or reflective mulches.",
    "Tomato___Tomato_Mosaic_Virus": "Remove and destroy infected plants. Control aphids, which can transmit the virus, by using insecticides or introducing natural predators.",
    "Tomato___Healthy": "Maintain a balanced watering schedule and regular soil health practices. Apply organic fertilizers and mulch to keep plants healthy."
}
recommended_chemicals = {
    # tomato  
    "Tomato___Bacterial_Spot": ["Copper-based bactericides"],
    "Tomato___Early_Blight": ["Chlorothalonil", "Mancozeb"],
    "Tomato___Late_Blight": ["Chlorothalonil", "Copper-based fungicides"],
    "Tomato___Leaf_Mold": ["Chlorothalonil", "Copper-based fungicides"],
    "Tomato___Septoria_Leaf_Spot": ["Mancozeb", "Chlorothalonil"],
    "Tomato___Spider_Mites_Two-Spotted_Spider_Mite": ["Avid", "Omite"],
    "Tomato___Target_Spot": ["Azoxystrobin", "Chlorothalonil"],
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": ["Imidacloprid", "Spinosad"],
    "Tomato___Tomato_Mosaic_Virus": ["Pyrethrins", "Insecticidal soap"],
    "Tomato___Healthy": ["Balanced organic fertilizer", "Compost"]
}


def predict_disease(image_path, model=model, transform=transform, class_names=class_names, disease_treatments=disease_treatments, recommended_chemicals=recommended_chemicals):
    
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)

    # make the prediction
    with torch.no_grad():
        outputs = model(image)
        _, preds = torch.max(outputs, 1)
        predicted_class = class_names[preds[0]]

        print(preds[0])

    treatment = disease_treatments.get(predicted_class, "No recommendation available.")
    chemical = recommended_chemicals.get(predicted_class, "No recommendation available.")

    return predicted_class, treatment, chemical


"""
# test

# image_path = 'test-images/cecospora1.png'
image_path = 'corns/test-images/common-rust3.png'
predicted_disease, treatment, chemical = predict_disease(image_path)
print(f"Predicted disease: {predicted_disease}")
print(f"Recommended treatment: {treatment}")
print(f"Recommended chemical: {chemical}")"
"""
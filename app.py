from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to call this API

def get_predicted_value(user_symptoms):
    # Your AI model logic (replace this with actual model prediction)
    return "Flu", "A viral infection", ["Rest", "Stay Hydrated"], ["Paracetamol"], ["Balanced Diet"], ["Light Exercise"]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    symptoms = data.get("symptoms", [])

    disease, desc, pre, med, diet, workout = get_predicted_value(symptoms)

    return jsonify({
        "disease": disease,
        "description": desc,
        "precautions": pre,
        "medications": med,
        "diet": diet,
        "workout": workout
    })

if __name__ == '__main__':
    app.run(debug=True)
 

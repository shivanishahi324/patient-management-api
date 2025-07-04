import pickle

# Load model and vectorizer
with open("disease_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Sample input
input_symptoms = "frequent urination and weight loss"

# Vectorize and predict
X_test = vectorizer.transform([input_symptoms])
prediction = model.predict(X_test)

print("Predicted Disease:", prediction[0])

# Patient Management System API — Built with FastAPI

Hello! I’m Shivani, and this is a backend project I developed while learning FastAPI.  
It is a simple RESTful API that manages patient records, automatically calculates BMI, and gives health verdicts based on standard BMI categories.

---

## Features

- View all patient records
- Get patient details by ID
- Add a new patient with auto-calculated BMI and verdict
- Edit or update existing patient data
- Delete a patient record
- Sort patients by height, weight, or BMI

---

---

##  New Feature: Disease Prediction using ML

The API now includes a machine learning model that predicts possible diseases based on symptoms input.

How It Works:

- Uses TF-IDF Vectorizer to process symptom text  
- Trained on a real-world medical dataset  
- Employs a Naive Bayes classifier for prediction  

Sample Request:

POST /predict

Request Body:
```json
{
  "text": "weight loss, frequent urination and thirst"
}
Response:

json
Copy code
{
  "prediction": "Diabetes"
}

Try the live API here:
https://patient-management-api-oljn.onrender.com/docs

```
## Tech Stack Used
```bash
- Python 3.10+
- FastAPI
- Pydantic
- JSON (used as local database)
- Uvicorn (ASGI server)

---md

## How to Run the Project

### Step 1: Create and activate a virtual environment

```bash
python -m venv myenv
.\myenv\Scripts\activate   # For Windows

```

### Step 2: Install the required packages

```bash
pip install -r requirements.txt

 If requirements.txt is not available, install manually:

```bash

pip install fastapi uvicorn pydantic

```
### Step 3: Start the FastAPI server
```bash
uvicorn main:app --reload
```

### Step 4: Open your browser to test the API
```bash
Visit:
http://127.0.0.1:8000/docs

This will open the Swagger UI where you can interact with the API.

```

### patient-management-api/

```bash
│
├── main.py              # FastAPI application
├── patients.json        # Mock database
├── requirements.txt     # Dependencies
└── README.md            # Documentation

```
### Future Improvements

```bash
Connect with real database (SQLite/PostgreSQL)

Add authentication (login/signup)

Add filtering and pagination

Deploy using Render or Heroku

Build a frontend using Streamlit or React
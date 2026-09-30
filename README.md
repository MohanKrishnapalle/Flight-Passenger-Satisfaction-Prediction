````
# Flight Passenger Satisfaction Prediction

A Machine Learning project that predicts whether a flight passenger is satisfied based on passenger and flight service information.

## Project Overview

This project uses a Machine Learning model to predict passenger satisfaction from various passenger and flight-related features.

The project includes a Streamlit web application where users can enter passenger details and receive a satisfaction prediction.

## Features

- Passenger satisfaction prediction
- Interactive Streamlit web interface
- Machine Learning pipeline
- Trained model included
- User-friendly input form
- Real-time prediction

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

## Machine Learning

The project uses a trained Machine Learning pipeline stored in:

```text
rf_pipeline.joblib
````

The target label encoder is stored in:

```text
label_encoder_target.joblib
```

## Project Structure

```
Flight-Passenger-Satisfaction-Prediction/
│
├── app.py
├── rf_pipeline.joblib
├── label_encoder_target.joblib
├── test.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Hiranya03/Flight-Passenger-Satisfaction-Prediction.git
```

### 2. Navigate to the project

```bash
cd Flight-Passenger-Satisfaction-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## Output

The application provides a prediction indicating whether the passenger is satisfied or dissatisfied based on the entered information.

````
import joblib

def load_model():
    """Load the pre-trained logistic regression model and scaler."""
    try:
        model = joblib.load('logreg_model.pkl')
        scaler = joblib.load('scaler.pkl')
        return model, scaler
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while loading the model: {e}")


def preprocess_input(input_data, scaler):
    if scaler is None:
        raise ValueError("Scaler is not loaded.")
    return scaler.transform(input_data)


def predict_diabetes(model, input_data):
    if model is None:
        raise ValueError("Model is not loaded.")
    return model.predict(input_data)[0]
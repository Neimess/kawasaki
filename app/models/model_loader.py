from tensorflow.keras.models import load_model


def load_model_from_path(path):
    try:
        return load_model(path)
    except Exception as e:
        raise ValueError(f"Failed to load model from {path}: {str(e)}")

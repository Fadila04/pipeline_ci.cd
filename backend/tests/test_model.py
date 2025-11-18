import os
import joblib

def test_model_exists():
    """Vérifie que le fichier .pkl du modéle existe"""
    model_path = os.path.join("model", "model.pkl")
    assert os.path.exists(model_path), "Le fichier model.pkl n'existe pas"


def test_model_loaded():
    """ Vérifie si le modéle est chargé"""
    model_path = os.path.join("model", "model.pkl")
    model = joblib.load(model_path)
    assert model is not None


def test_model_prediction():
    """Test pour voir si les prédictions retourne un entier"""
    model_path = os.path.join("model", "model.pkl")
    model = joblib.load(model_path)

    sample = [5.1, 3.5, 1.4, 0.2]  # Le point du dataset Iris
    pred = model.predict([sample])[0]

    assert pred == 0




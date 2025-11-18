import os
import logging
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Configuration logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Le chemin vers le dossier model/
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model")
MODEL_PATH = os.path.join(MODEL_DIR, "model.pkl")

def train_model():
    logger.info("Début de l'entrainement du modéle")

    # Chargement des données (Iris Datasets)
    data = load_iris()
    X, y = data.data, data.target

    logger.info("Chargement des données OK")

    X_train, X_test, y_train, y_test = train_test_split( 
        X,y, test_size=0.2, random_state=42)
    
    # Démrage du Mlflow
    mlflow.set_experiment("simple-iris-model")

    with mlflow.start_run():
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        score = model.score(X_test, y_test)
        mlflow.log_metric("accuracy", score)
        mlflow.sklearn.log_model(model, "model")

        logger.info(f"Modéle entrainé - Accuracy={score}")

        # Sauvegarde du modéle en .pkl
        os.makedirs(MODEL_DIR, exist_ok=True)
        joblib.dump(model, MODEL_PATH)

        logger.info(f"Modéle sauvegarder dans : {MODEL_PATH}")

if  __name__ == "__main__":
        train_model()
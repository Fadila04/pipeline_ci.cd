# pipeline_ci.cd

# Pour lancer FastAPI
cd backend
uvicorn app.app:app --reload


mlflow : mlflow ui --port 5001

Fichier tests: python -m pytest

Dans ce dossier docs : 
mkdocs new .
mkdocs serve pour accéder à la doc


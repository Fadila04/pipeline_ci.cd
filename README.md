# pipeline_ci.cd

# Pour lancer FastAPI
cd backend
uvicorn app.app:app --reload

# Pour lancer le mlflow
mlflow : mlflow ui --port 5001

# Lancement du fichier tests
Fichier tests: python -m pytest

Dans ce dossier docs : 
mkdocs new .
mkdocs serve pour accéder à la doc

# Streamlit
streamlit run streamlit_app.py

# Build et run image
docker build -t fastapi-backend .
docker run -p 8000:8000 fastapi-backend

# build docker compose
docker-compose up --build

# lorsque le port ne fonctionne pas
 lsof -i:8000
docker-compose down













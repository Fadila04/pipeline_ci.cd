
# INTRODUCTION
Objectif du projet
Ce qu’on cherche à apprendre : CI/CD, FastAPI, Streamlit, Docker, Azure

Résultat final : un pipeline complet
Ce projet vise à mettre en place une chaîne complète de développement et de déploiement d’une application IA comprenant un modèle ML, une API FastAPI, une interface Streamlit, un pipeline CI/CD avec GitHub Actions et un déploiement sur Azure App Service.

# ARCHITECTURE GENERAL
│
├── backend/
│   ├── app/
│   │   ├── app.py               # API FastAPI
│   │   ├── schemas.py           # Validation Pydantic
│   │   ├── utils.py             # Prétraitement
│   │   └── model.pkl            # Modèle sauvegardé
│   ├── tests/                   # Tests unitaires API + modèle
│        ├── test_api.py
│        ├── test_model.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── streamlit_app.py         # Interface utilisateur
│   ├── Dockerfile
│   └── requirements.txt
│
├── ml/
│   ├── train.py           # Entraînement + MLflow
│  
│
├── model/
│   └── model.pkl                # Modèle ML final
│
├── docs/                        # Documentation MkDocs
│   ├── index.md
│   └── mkdocs.yml
│
├── docker-compose.yml           # Dév local
└── .github/workflows/docker_image.yml     # Pipeline CI/CD

# PIPELINE ML
Dataset Iris : description courte

Étapes du modèle :
- Chargement
- Split train/test
- Entraînement
- Sauvegarde du modèle .pkl

# BACKEND
✔️ Endpoints : Fastapi
GET / → healthcheck
POST /predict :
validation Pydantic
chargement du modèle
prédiction

✔️ Logging
traçage des prédictions
erreurs
valeur reçues

✔️ Tests
tests des endpoints
tests du modèle

# FRONTEND
✔️ Fonctionnement
formulaire avec les 4 features Iris
appel à l’API
affichage du résultat

✔️ Gestion de l’URL backend
En local Docker Compose → http://backend:8000

En local hors Docker → http://localhost:8000

Sur Azure → https://votre-backend.azurewebsites.net


# DOCKERISATION
✔️ Dockerfile backend
installation des dépendances
copie des fichiers
démarrage uvicorn
port exposé

✔️ Dockerfile frontend
Streamlit
port exposé (8501)

✔️ docker-compose.yml
deux services : backend + frontend
même network
accès via backend:8000


# PIPELINE CI/CD
✔️ Déclenchement
on: push on main

✔️ Étapes du job CI :
Checkout du repo
Setup Python
Install deps backend
Tests
Deploy MkDocs
Login DockerHub
Build images backend + frontend
Push DockerHub


# DEPLOIMENT AZURE
✔️ Création de 2 Web Apps
backend
frontend

✔️ Déploiement depuis DockerHub
images <user>/backend:latest
images <user>/frontend:latest

✔️ Configuration
port du backend = 8000
variable BACKEND_URL pour Azure

✔️ Continuous Deployment
Mode “deployment center”
Activer le Continuous Deployment

# PROBLEME RENCONTRE
✔️ Conflit port 8000 → solution : arrêter conteneur parasite
✔️ Failed to resolve 'backend' en Azure → solution : utiliser URL Azure
✔️ Docker Compose vs exécution hors Docker
✔️ Erreurs liées aux slots Azure → ressources introuvables
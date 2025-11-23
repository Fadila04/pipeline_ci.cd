
# Projet : Pipeline CI/CD complet (Modèle ML → API FastAPI → Frontend Streamlit → Docker → GitHub Actions → Azure)
🎯 Objectif général
Ce projet a pour but de construire un pipeline CI/CD complet permettant de déployer une application IA composée de :

- Un modèle ML simple (dataset Iris)

- Une API FastAPI exposant / et /predict

- Un frontend Streamlit pour entrer des valeurs et afficher une prédiction

- Des tests automatisés

- De la documentation MkDocs

- Une dockerisation backend + frontend

- Un pipeline GitHub Actions pour :

- Lancer les tests

- Déployer la documentation

- Construire les images Docker

- Pousser les images sur DockerHub

- Un déploiement final sur Azure App Service


 1. Structure du projet
 Projet
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

2. # Le dataset Iris
Le dataset Iris contient 150 fleurs
4 features : Sepal length, Sepal width, Petal length, Petal width
3 classes : Setosa, Versicolor, Virginica

Le frontend permet de saisir ces 4 valeurs pour effectuer une prédiction.

3. Entraînement du modèle (avec MLflow)
Dans ml/train_model.py :

✔️ Chargement du dataset Iris
✔️ Entraînement d’un modèle simple de classification : LogisticRegression
✔️ Tracking MLflow : params, metrics

✔️ Sauvegarde du modèle au format model.pkl dans model/

# Gestion des chemins :
Le script doit fonctionner :

en local

en Docker

dans GitHub Actions

# Backend : API FastAPI

L’API offre deux routes :
- GET /
Renvoie :
{"status": "ok"}

Utilisé pour vérifier l’état de l’API sur Azure.
- POST /predict :
  - charge le modèle model.pkl
  - valide l’entrée grâce à Pydantic
  - effectue une prédiction
  - retourne le résultat

Exemple de réponse :
{"prediction": "setosa", "probability": 0.92}

✔️ Logging

Le backend utilise logging pour suivre :
  - chargement du modèle
  - données reçues
  - prédiction effectuée
  - erreurs éventuelles

5. Frontend Streamlit

Le frontend permet :
  - de saisir les 4 features d’iris
  - d’envoyer une requête POST à l’API FastAPI
  - d’afficher la prédiction

⚠️ Deux configurations API_URL selon le contexte :
👉 En Docker Compose (développement local)
API_URL = "http://backend:8000/predict"

 En local (backend hors Docker)
API_URL = "http://localhost:8000/predict"

 Sur Azure
API_URL = "https://VOTRE_BACKEND.azurewebsites.net/predict"

6. Tests automatisés

Tests réalisés avec pytest :

  - chargement du modèle
  - prédiction du modèle
  - test de la route GET /
  - test de la route POST /predict

Ces tests sont exécutés automatiquement dans GitHub Actions.

7. Documentation MkDocs

Dans docs/ :
génération avec mkdocs new .

lancement local :
mkdocs serve


déploiement via GitHub Actions :

mkdocs gh-deploy --force

8. Dockerisation
Backend Dockerfile :

installe les dépendances

copie le code

expose le port 8000

démarre avec uvicorn

Frontend Dockerfile :

installe les dépendances

démarre Streamlit en exposant le port 8501

9. docker-compose (en développement local)

docker-compose up --build lance :

backend → http://localhost:8000

frontend → http://localhost:8501

Les deux conteneurs sont sur le même réseau : http://backend:8000/predict

10. Pipeline CI/CD GitHub Actions

À chaque push sur main, le pipeline :

✔️ installe Python
✔️ installe les dépendances backend
✔️ lance les tests pytest
✔️ build la documentation MkDocs
✔️ se connecte à DockerHub via secrets
✔️ build image backend & frontend
✔️ push les images sur DockerHub

Les secrets nécessaires :

DOCKERHUB_USERNAME
DOCKERHUB_TOKEN

11. Déploiement sur Azure App Service
Deux Web Apps :

- Backend
Type : "Deploy from container"

Source : DockerHub <username>/backend:latest

Port exposé : 8000

accessible via :
https://fadilatoubackend-e3fseufddgh3apbb.francecentral-01.azurewebsites.net/docs

- Frontend
Type : container

Source : <username>/frontend:latest

Ajouter une variable d’environnement :

BACKEND_URL = https://votre-backend.azurewebsites.net/predict
accessible via : https://fadilatoufrontend-gyh4h5h5d5fkhdfs.francecentral-01.azurewebsites.net/

Erreur fréquente corrigée : Failed to resolve 'backend'
➡️ solution : utiliser l’URL Azure, pas backend:8000.

12. Fonctionnement final

L’utilisateur ouvre le frontend Streamlit sur Azure.

Il saisit les 4 features Iris.

Le frontend envoie la requête à l’API FastAPI (Azure backend).

L’API charge le modèle et effectue une prédiction.

Le résultat est affiché à l’écran.

13. Bonus réalisés ou possibles

(Bonus) Azure ML Tracking Server

Ruff pour formatage du code ( je l'ai mit dans le workflow pour lever les erreurs ( ruff ckeck .))

14. Conclusion

Ce projet met en place un pipeline IA complet, du développement au déploiement cloud :

Modèle ML

API FastAPI

Frontend Streamlit

Docker

CI/CD avec GitHub Actions

Déploiement Azure

Il permet de comprendre les pratiques modernes de développement et déploiement d’applications IA en production.





<!-- # pipeline_ci.cd

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
docker push , images -->

# Azure 
Tout les detail du deploiement









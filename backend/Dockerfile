# 1. Image python légère
FROM python:3.11-slim

# 2. Définir l’emplacement de travail
WORKDIR /app

# 3. Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# 4. Copier d’abord les dépendances
COPY requirements.txt .

# 5. Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copier le reste du projet
COPY . .

# 7. Exposer le port FastAPI
EXPOSE 8000

# 8. Lancer FastAPI via uvicorn
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]










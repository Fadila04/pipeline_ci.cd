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
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]










# # 1. Image de base
# FROM python:3.12-slim

# # Set working dir
# WORKDIR /app

# # Environment
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Install system dependencies often required to build scientific packages
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         build-essential \
#         gfortran \
#         libatlas-base-dev \
#         libblas-dev \
#         liblapack-dev \
#         pkg-config \
#         libffi-dev \
#         libssl-dev \
#         ca-certificates \
#         wget \
#         default-libgomp-dev \
#         cargo \
#     && rm -rf /var/lib/apt/lists/*

# # Upgrade pip/wheel/setuptools first to prefer wheels
# RUN python -m pip install --upgrade pip setuptools wheel

# # Copy requirements and install Python deps
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy application code
# COPY . .

# # Expose port and start Uvicorn
# EXPOSE 8000
# CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000"]










# Image python
FROM python:3.11-slim

# 2. Définir l’emplacement de travail
WORKDIR /streamlit_app

# 3. Copier les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y curl

# 4. Copier le reste du projet
COPY . .

# 7. Exposer le port Streamlit
EXPOSE 8501

# 8. Lancer Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
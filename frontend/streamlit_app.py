import streamlit as st
import requests

API_URL = "https://fadilatoubackend-e3fseufddgh3apbb.francecentral-01.azurewebsites.net/"

st.set_page_config(page_title="Predict App", layout="centered")
st.title("Mini frontend Streamlit — Predict Iris Dataset")

st.markdown("Entrez les 4 features puis cliquez sur **Predict**.")

# Ici on met la bonne URL par défaut
backend_url = st.text_input("Backend URL", API_URL)

col1, col2 = st.columns(2)
with col1:
    feature_1 = st.slider("Largeur Pétale", 0, 10)
    feature_2 = st.slider("Largeur Pétale 2", 0, 10)
with col2:
    feature_3 = st.slider("Longueur Sépale", 0, 10)
    feature_4 = st.slider("Largeur Sépale", 0, 10)

if st.button("Predict"):

    payload = {"features": [feature_1, feature_2, feature_3, feature_4]}
    endpoint = backend_url.rstrip("/") + "/predict"

    with st.spinner("Envoi de la requête..."):
        try:
            resp = requests.post(endpoint, json=payload, timeout=10)
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            st.error(f"Erreur lors de la requête : {e}")
        else:
            try:
                data = resp.json()
            except ValueError:
                st.error("Réponse du serveur invalide (JSON attendu).")
            else:
                if "prediction" in data:
                    st.success(f"Prediction: {data['prediction']}")
                    st.json(data)
                else:
                    st.warning(f"Réponse reçue : {data}")









# Utilise une image officielle de Python comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir \
    numpy==1.23.5 \
    pandas==1.5.3 \
    scikit-learn==1.2.2 \
    joblib==1.2.0 \
    fastapi==0.95.2 \
    pydantic==1.10.7 \
    uvicorn
# Exposer le port de l’API
EXPOSE 8000

# Commande pour lancer l'API FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

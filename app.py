from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Charger le modèle
model = joblib.load('house_price_predictor.pkl')

# Initialiser l'application FastAPI
app = FastAPI(title="API de Prédiction de Prix des Maisons")

# Définir le schéma des données attendues
class HouseData(BaseModel):
    surface_reelle_bati: float
    nombre_pieces_principales: int
    prix_m2: float
    code_postal_encoded: int
    popu_croissance: float
    rev_fisc_moyen_reference: float
    unemployment_rate: float
    schools_within_1km: int
    min_distance_km_school: float
    bus_500m: int
    min_km_bus: float

# Route de test pour vérifier que l'API fonctionne
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de Prédiction de Prix des Maisons !"}

# Endpoint pour effectuer des prédictions
@app.post("/predict")
def predict_price(data: HouseData):
    # Conversion des données en DataFrame
    df = pd.DataFrame([data.dict()])

    # Prédiction
    prediction = model.predict(df)

    # Retourner le résultat
    return {"prediction": prediction[0]}

# Lancer le serveur si exécuté directement
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

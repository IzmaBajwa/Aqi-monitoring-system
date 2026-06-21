import os
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
from dotenv import load_dotenv

# ======================================
# LOAD ENVIRONMENT VARIABLES
# ======================================

load_dotenv()

# ======================================
# DATABASE CONFIG
# ======================================

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ======================================
# API CONFIG
# ======================================

API_KEY = os.getenv("API_KEY")
LAT = float(os.getenv("LAT"))
LON = float(os.getenv("LON"))

url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={LAT}&lon={LON}&appid={API_KEY}"

# ======================================
# EXTRACT
# ======================================

response = requests.get(url)
data = response.json()

# ======================================
# TRANSFORM
# ======================================

components = data["list"][0]["components"]

record = {
    "timestamp": datetime.now(),
    "latitude": LAT,
    "longitude": LON,
    "aqi": data["list"][0]["main"]["aqi"],
    "pm2_5": components["pm2_5"],
    "pm10": components["pm10"],
    "no2": components["no2"],
    "o3": components["o3"],
    "co": components["co"]
}

df = pd.DataFrame([record])

# ======================================
# LOAD INTO POSTGIS
# ======================================

with engine.connect() as conn:

    query = text("""
        INSERT INTO aqi_data (
            timestamp,
            latitude,
            longitude,
            aqi,
            pm2_5,
            pm10,
            no2,
            o3,
            co,
            geom
        )
        VALUES (
            :timestamp,
            :latitude,
            :longitude,
            :aqi,
            :pm2_5,
            :pm10,
            :no2,
            :o3,
            :co,
            ST_SetSRID(ST_MakePoint(:longitude, :latitude), 4326)
        )
    """)

    conn.execute(query, record)
    conn.commit()

print("AQI ETL pipeline executed successfully.")
print(df)
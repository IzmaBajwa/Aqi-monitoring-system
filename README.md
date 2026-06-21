 Lahore Air Quality (AQI) Dashboard

A real-time air quality monitoring pipeline and interactive dashboard for Lahore, Pakistan. The system automatically fetches live air pollution data, stores it in a spatial database, and visualizes it through an interactive web dashboard with a live map.

## Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline combined with a geospatial dashboard. It pulls real-time air quality data from the OpenWeatherMap API, processes it, stores it in a PostGIS-enabled PostgreSQL database, and displays the latest readings on an interactive Streamlit dashboard with a live map.

## Tech stack

- **Python** — core ETL logic
- **PostgreSQL + PostGIS** — spatial database for storing AQI readings with geographic coordinates
- **SQLAlchemy** — database connection and query execution
- **pandas** — data structuring and transformation
- **geopandas** — reading spatial data from PostGIS
- **Streamlit** — interactive web dashboard
- **Folium** — interactive map rendering
- **OpenWeatherMap API** — live air pollution data source

## Features

- Automated extraction of real-time AQI, PM2.5, PM10, NO2, O3, and CO data
- Spatial storage using PostGIS geometry points
- Live interactive dashboard with color-coded AQI status (Good → Very Poor)
- Interactive map centered on Lahore with pollutant details in a popup
- Secure credential handling using environment variables

## Project structure
lahore-aqi-dashboard/

├── pipeline.py          # ETL script — fetches and loads AQI data

├── dashboard.py         # Streamlit dashboard

├── requirements.txt     # Python dependencies

├── .gitignore           # Files excluded from version control

└── README.md            # Project documentation

## How it works

1. **Extract** — `pipeline.py` calls the OpenWeatherMap Air Pollution API for Lahore's coordinates
2. **Transform** — the JSON response is parsed into a structured record with a timestamp
3. **Load** — the record is inserted into a PostgreSQL/PostGIS table, with coordinates stored as a spatial geometry point
4. **Visualize** — `dashboard.py` reads the latest record using GeoPandas and displays it through a Streamlit dashboard with live metrics and an interactive map

## Setup instructions

1. Clone this repository:
git clone https://github.com/yourusername/lahore-aqi-dashboard.git

cd lahore-aqi-dashboard

2. Install dependencies:
pip install -r requirements.txt

3. Create a `.env` file in the project root with the following variables:
DB_USER=your_postgres_username

DB_PASSWORD=your_postgres_password

DB_HOST=localhost

DB_PORT=5432

DB_NAME=Lahore_AQI

OPENWEATHER_API_KEY=your_openweathermap_api_key

LAT=31.5204

LON=74.3587

4. Run the ETL pipeline to fetch and store data:
python pipeline.py

5. Launch the dashboard:
streamlit run dashboard.py

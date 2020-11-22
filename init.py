import os
from config import db
from models import Meteo

METEO = [
    {
        "dt": 1605927600,
        "city": "Montreal",
        "temp": 272.36,
        "feels_like": 268.42,
        "temp_min": 272.36,
        "temp_max": 272.47,
        "pressure": 1024,
        "sea_level": 1024,
        "grnd_level": 1008,
        "humidity": 99,
    },
    {
        "dt": 1605938400,
        "city": "Montreal",
        "temp": 272.38,
        "feels_like": 268.5,
        "temp_min": 272.38,
        "temp_max": 272.41,
        "pressure": 1026,
        "sea_level": 1026,
        "grnd_level": 1010,
        "humidity": 98,
    },
    {
        "dt": 1605949200,
        "city": "Quebec",
        "temp": 273.01,
        "feels_like": 269.33,
        "temp_min": 273.01,
        "temp_max": 273.06,
        "pressure": 1028,
        "sea_level": 1028,
        "grnd_level": 1010,
        "humidity": 98,
    },
]


if os.path.exists("meteo.db"):
    os.remove("meteo.db")

db.create_all()

for item in METEO:
    meteo = Meteo(
        dt=item["dt"],
        city=item["city"],
        temp=item["temp"],
        feels_like=item["feels_like"],
        temp_min=item["temp_min"],
        temp_max=item["temp_max"],
        pressure=item["pressure"],
        sea_level=item["sea_level"],
        grnd_level=item["grnd_level"],
        humidity=item["humidity"],
    )
    db.session.add(meteo)

db.session.commit()

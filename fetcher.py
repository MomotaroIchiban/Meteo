import logging
import requests

from config import db
from models import Meteo
from settings import APIKEY, WEATHER_API, CITIES, LOG_FORMAT

logging.basicConfig(filename="fetcher.log", format=LOG_FORMAT)
logger = logging.getLogger("fetcher")


def job():
    for city in CITIES:
        try:
            req = requests.get(WEATHER_API.format(city, APIKEY))
            item = Meteo(
                city=city,
                dt=req.json()["dt"],
                temp=req.json()["main"]["temp"],
                feels_like=req.json()["main"]["feels_like"],
                temp_min=req.json()["main"]["temp_min"],
                temp_max=req.json()["main"]["temp_max"],
                pressure=req.json()["main"]["pressure"],
                sea_level=req.json()["main"]["sea_level"],
                grnd_level=req.json()["main"]["grnd_level"],
                humidity=req.json()["main"]["humidity"],
            )
            db.session.add(item)
        except Exception as e:
            logger.error(e)

    db.session.commit()


# stand alone mode
if __name__ == "__main__":
    job()

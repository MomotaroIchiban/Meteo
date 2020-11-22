import logging
import requests

from config import db
from models import Meteo
from settings import (
    APIKEY,
    WEATHER_API,
    CITIES,
)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('meteo')

def job():
    for city in CITIES:
        import pdb; pdb.set_trace() 
        try:
            req = requests.get(WEATHER_API.format(city, APIKEY))
            item = Meteo(
                city = city,
                dt = req.json()['dt'],
                temp = req.json()['main']['temp'],
                feels_like = req.json()['main']['feels_like'],
                temp_min = req.json()['main']['temp_min'],
                temp_max = req.json()['main']['temp_max'],
                pressure = req.json()['main']['pressure'],
                sea_level = req.json()['main']['sea_level'],
                grnd_level = req.json()['main']['grnd_level'],
                humidity = req.json()['main']['humidity'],
            )
            db.session.add(item)
        except Exception as e:
            logger.error(e)
        import pdb; pdb.set_trace()

    db.session.commit()


import logging
from flask import (
    make_response,
    abort,
)
from models import (
    Meteo,
    MeteoSchema,
)
from settings import LOG_FORMAT, CITIES

logging.basicConfig(filename="meteo.log", format=LOG_FORMAT)
logger = logging.getLogger("meteo")


def read_all():
    """
    Return all Meteo entries

    :return: JSON list of Meteo records
    """

    try:
        entries = Meteo.query.order_by(Meteo.dt).all()

        # Serialize data
        meteo_schema = MeteoSchema(many=True)
    except Exception as e:
        logger.warning(e)
        return []
    else:
        return meteo_schema.dump(entries)


def read_one(city):
    """
    Return Meteo entries for a city

    :param id: city id
    :return:   all meteo entries for specified city
    """

    if city not in CITIES:
        abort(404, "This city is not included in the data")

    try:
        entries = Meteo.query.filter(Meteo.city == city).order_by(Meteo.dt)
        # Serialize data
        meteo_schema = MeteoSchema(many=True)
    except Exception as e:
        logger.warning(e)
        return []
    else:
        return meteo_schema.dump(entries)

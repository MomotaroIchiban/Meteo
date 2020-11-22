from flask import (
    make_response,
    abort,
)
from models import (
    Meteo,
    MeteoSchema,
)


def read_all():
    """
    Return all Meteo entries

    :return: JSON list of Meteo records
    """

    entries = Meteo.query \
            .order_by(Meteo.dt) \
            .all()

    # Serialize data
    meteo_schema = MeteoSchema(many=True)
    return meteo_schema.dump(entries)

def read_one(city):
    """
    Return Meteo entries for a city

    :param id: city id
    :return:   all meteo entries for specified city
    """

    entries = Meteo.query.filter(Meteo.city==city).order_by(Meteo.dt)

    # Serialize data
    meteo_schema = MeteoSchema(many=True)
    return meteo_schema.dump(entries)


from config import db, ma

class Meteo(db.Model):
    """
    A weather entry
    """
    __tablename__ = 'meteo'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(32))
    dt = db.Column(db.Integer)
    temp = db.Column(db.Integer)
    feels_like = db.Column(db.Integer)
    temp_min = db.Column(db.Integer)
    temp_max = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    sea_level = db.Column(db.Integer)
    grnd_level = db.Column(db.Integer)
    humidity = db.Column(db.Integer)

class MeteoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Meteo
        sqla_session = db.session


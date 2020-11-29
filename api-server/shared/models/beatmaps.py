from db import db
from shared.serializer import Serializer
from sqlalchemy.dialects import mysql


class MyBeatmaps(db.Model, Serializer):

    beatmap_id =        db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    beatmapset_id =     db.Column(mysql.INTEGER(10, unsigned=True))
    artist =            db.Column(mysql.VARCHAR(80))
    title =             db.Column(mysql.VARCHAR(80))
    version =           db.Column(mysql.VARCHAR(80))
    bpm =               db.Column(mysql.FLOAT(unsigned=True))
    total_length =      db.Column(mysql.MEDIUMINT(11, unsigned=True))
    hit_length =        db.Column(mysql.MEDIUMINT(11, unsigned=True))
    difficulty_rating = db.Column(mysql.FLOAT(unsigned=True))

    def serialize(self):
        res = Serializer.serialize(self)
        return res


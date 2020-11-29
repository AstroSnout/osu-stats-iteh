from db import db
from shared.serializer import Serializer
from sqlalchemy.dialects import mysql


class MyScores(db.Model, Serializer):

    score_id =     db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    beatmap_id =   db.Column(mysql.INTEGER(10, unsigned=True))
    user_id =      db.Column(mysql.INTEGER(10, unsigned=True))
    accuracy =     db.Column(mysql.FLOAT(unsigned=True))
    pp =           db.Column(mysql.FLOAT(unsigned=True))
    enabled_mods = db.Column(mysql.VARCHAR(20))

    def serialize(self):
        res = Serializer.serialize(self)
        return res

from db import db
from shared.serializer import Serializer
from sqlalchemy.dialects import mysql


class MyUsers(db.Model, Serializer):

    user_id =    db.Column(mysql.INTEGER(10, unsigned=True), primary_key=True)
    accuracy =   db.Column(mysql.FLOAT(unsigned=True))
    playcount =  db.Column(mysql.MEDIUMINT(11, unsigned=True))
    rank =       db.Column(mysql.INTEGER(10, unsigned=True))
    pp =         db.Column(mysql.FLOAT(unsigned=True))
    country =    db.Column(mysql.CHAR(2))

    def serialize(self):
        res = Serializer.serialize(self)
        return res

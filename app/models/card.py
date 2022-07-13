from flask_sqlalchemy import SQLAlchemy
from .db import db
from datetime import datetime


class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    played = db.Column(db.Boolean, nullable=False, default=False)
    war = db.Column(db.Boolean, nullable=False, default=False)
    image = db.Column(db.String, nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.now())

    player = db.relationship("Player", back_populates="stack")

    def to_dict(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "value": self.value,
            "played": self.played,
            "war": self.war,
            "image": self.image,
            "updated": self.updated.strftime("%Y-%m-%d %H:%M:%S")
        }
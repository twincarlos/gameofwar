from flask_sqlalchemy import SQLAlchemy
from .db import db


class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    played = db.Column(db.Boolean, nullable=False, default=False)
    war = db.Column(db.Boolean, nullable=False, default=False)
    image = db.Column(db.String, nullable=False)

    player = db.relationship("Player", back_populates="stack")

    def to_dict(self):
        return {
            "id": self.id,
            "player_id": self.player_id,
            "value": self.value,
            "image": self.image
        }
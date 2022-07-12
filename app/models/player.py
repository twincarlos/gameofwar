from flask_sqlalchemy import SQLAlchemy
from .db import db


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    wins = db.Column(db.Integer, nullable=False, default=0)

    stack = db.relationship("Card", back_populates="player")
    
    def to_dict(self):
        return {
            "id": self.id,
            "wins": self.wins,
            "stack": [card.to_dict() for card in self.stack]
        }
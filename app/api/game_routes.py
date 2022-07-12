from flask import Blueprint, request
from app.models import db, Player, Card

game_routes = Blueprint("games", __name__)

@game_routes.route("")
def get_game_info():
    player_1 = Player.query.get(1).to_dict()
    player_2 = Player.query.get(2).to_dict()

    played_1 = Card.query.filter(Card.player_id == 1, Card.played is True).first()
    if played_1 is not None: played_1 = played_1.to_dict()

    played_2 = Card.query.filter(Card.player_id == 2, Card.played is True).first()
    if played_1 is not None: played_2 = played_2.to_dict()

    war = Card.query.filter(Card.war is True).all()

    return {
        "player_1": player_1,
        "player_2": player_2,
        "played_1": played_1,
        "played_2": played_2,
        "war": war
    }
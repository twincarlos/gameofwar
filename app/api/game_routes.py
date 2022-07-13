from flask import Blueprint, request
from app.models import db, Player, Card
from random import sample

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

    game_started = True

    if len(Card.query.filter(Card.player_id == 3).all()): game_started = False

    return {
        "game_started": game_started,
        "player_1": player_1,
        "player_2": player_2,
        "played_1": played_1,
        "played_2": played_2,
        "war": war
    }

@game_routes.route("/start", methods=["PUT"])
def start_game():
    numbers = sample(list(range(1, 53)), 52)

    for i in range(52):
        card = Card.query.get(numbers[i])

        if i % 2 == 0: card.player_id = 1
        else: card.player_id = 2

        db.session.commit()

    return ""
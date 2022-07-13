from flask import Blueprint, request
from app.models import db, Player, Card
from random import sample
import json
from datetime import datetime

game_routes = Blueprint("games", __name__)


@game_routes.route("")
def get_game_info():
    player_1 = Player.query.get(1).to_dict()
    player_2 = Player.query.get(2).to_dict()

    played_1 = Card.query.filter(Card.player_id == 1, Card.played == True).first()
    if played_1 is not None: played_1 = played_1.to_dict()

    played_2 = Card.query.filter(Card.player_id == 2, Card.played == True).first()
    if played_2 is not None: played_2 = played_2.to_dict()

    war = Card.query.filter(Card.war == True).all()

    game_started = True
    if len(Card.query.filter(Card.player_id == 3).all()): game_started = False

    return {
        "game_started": game_started,
        "player_1": player_1,
        "player_2": player_2,
        "played_1": played_1,
        "played_2": played_2,
        "war": [card.to_dict() for card in war]
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


@game_routes.route("/draw", methods=["PUT"])
def draw_cards():
    data = request.json

    card_1 = Card.query.get(data["card_1"])
    card_1.played = True

    card_2 = Card.query.get(data["card_2"])
    card_2.played = True

    db.session.commit()

    return ""


@game_routes.route("/continue", methods=["PUT"])
def continue_game():
    data = request.json
    card_1 = Card.query.get(data["card_1"])
    card_1.played = False
    card_1.updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    card_2 = Card.query.get(data["card_2"])
    card_2.played = False
    card_2.updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if card_1.value > card_2.value:
        card_1.player_id = 1
        card_2.player_id = 1
    elif card_1.value < card_2.value:
        card_1.player_id = 2
        card_2.player_id = 2
    else:
        card_1.war = True
        card_2.war = True
    
    db.session.commit()

    return ""
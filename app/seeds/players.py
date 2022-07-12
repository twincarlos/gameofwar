from app.models import db, Player

def seed_players():
    player_1 = Player()
    player_2 = Player()
    no_player = Player()

    db.session.add(player_1)
    db.session.add(player_2)
    db.session.add(no_player)
    
    db.session.commit()


def undo_players():
    db.session.execute('TRUNCATE players RESTART IDENTITY CASCADE;')
    db.session.commit()
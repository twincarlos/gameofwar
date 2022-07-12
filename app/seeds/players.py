from app.models import db, Player

def seed_players():
    player_1 = Player()
    player_2 = Player()

    db.session.add(player_1)
    db.session.add(player_2)
    
    db.session.commit()


def undo_players():
    db.session.execute('TRUNCATE players RESTART IDENTITY CASCADE;')
    db.session.commit()
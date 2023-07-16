from models.model import User, Team, Games, Tournament, Team_To_Tournament

def seed_database(db):
    # Insert users
    users_data = [
        {"name": "Albert Iskandar", "status": "active"},
        {"name": "Gustian REKT", "status": "active"},
        {"name": "Valdi R7", "status": "inactive"},
        {"name": "Deden Clay", "status": "active"},
        {"name": "Nando Xinn", "status": "active"},
        {"name": "Pak AP", "status": "active"},
        {"name": "Bjorn", "status": "active"},
        {"name": "Boss AE", "status": "active"},
        {"name": "BTR PUBG Manager", "status": "active"},
        {"name": "GPX PUBG Manager", "status": "active"},
        {"name": "Morph PUBG Manager", "status": "active"},
        {"name": "Aerowolf PUBG Manager", "status": "active"}
    ]
    for user_data in users_data:
        user = User(name=user_data['name'], status=user_data['status'])
        db.session.add(user)

    # Insert games
    games_data = [
        {"name": "Mobile Legends: Bang Bang", "status": "active"},
        {"name": "PUBG", "status": "active"}
    ]
    for game_data in games_data:
        game = Games(name=game_data['name'], status=game_data['status'])
        db.session.add(game)

    # Insert teams
    teams_data = [
        {"name": "RRQ Hoshi", "created_by": 6, "status": "active", "id_games": 1},
        {"name": "Evos Legends", "created_by": 7, "status": "active", "id_games": 1},
        {"name": "Alter EGO", "created_by": 8, "status": "active", "id_games": 1},
        {"name": "BTR", "created_by": 9, "status": "active", "id_games": 2},
        {"name": "GPX", "created_by": 10, "status": "active", "id_games": 2},
        {"name": "Morph Team", "created_by": 11, "status": "active", "id_games": 2},
        {"name": "Aeorowolf Genflix", "created_by": 12, "status": "active", "id_games": 2}
    ]
    for team_data in teams_data:
        team = Team(name=team_data['name'], created_by=team_data['created_by'], status=team_data['status'], id_games=team_data['id_games'])
        db.session.add(team)

    # Insert tournaments
    tournaments_data = [
        {"name": "MPL Season 13", "status": "regis_open", "id_games": 1, "max_slot": 8},
        {"name": "SEA Games", "status": "regis_open", "id_games": 1, "max_slot": 12},
        {"name": "MPL Season 12", "status": "ongoing", "id_games": 1, "max_slot": 8},
        {"name": "PUBG Mobile Crush Competition", "status": "regis_open", "id_games": 2, "max_slot": 36},
        {"name": "PINC Indonesia Championship", "status": "regis_open", "id_games": 2, "max_slot": 36},
        {"name": "PUBG Mobile Campus Championship", "status": "ongoing", "id_games": 2, "max_slot": 36}
    ]
    for tournament_data in tournaments_data:
        tournament = Tournament(name=tournament_data['name'], status=tournament_data['status'], id_games=tournament_data['id_games'], max_slot=tournament_data['max_slot'])
        db.session.add(tournament)

    # Insert team_to_tournament
    team_to_tournament_data = [
        {"id_team": 2, "id_tournament": 1, "status_daftar": "approved"},
        {"id_team": 3, "id_tournament": 1, "status_daftar": "approved"},
        {"id_team": 1, "id_tournament": 2, "status_daftar": "approved"},
        {"id_team": 3, "id_tournament": 2, "status_daftar": "approved"},
        {"id_team": 5, "id_tournament": 4, "status_daftar": "approved"},
        {"id_team": 6, "id_tournament": 4, "status_daftar": "approved"},
        {"id_team": 5, "id_tournament": 5, "status_daftar": "approved"},
        {"id_team": 5, "id_tournament": 6, "status_daftar": "approved"}
    ]
    for tt_data in team_to_tournament_data:
        team_to_tournament = Team_To_Tournament(id_team=tt_data['id_team'], id_tournament=tt_data['id_tournament'], status_daftar=tt_data['status_daftar'])
        db.session.add(team_to_tournament)

    
    db.session.commit()

    if __name__ == '__main__':
        seed_database()

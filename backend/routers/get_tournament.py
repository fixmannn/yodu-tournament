from models.model import Tournament, Games, Team, Team_To_Tournament
from flask import jsonify


#API to get recommended tournament
def recommended_tournament(db):
    try:
        query = db.session.query(
            Tournament.id.label('tourney_id'),
            Tournament.name,
            Games.id.label('game_id'),
            Games.name.label('game_name'),
            Tournament.status,
            Team.id.label('team_id'),
            Team.name.label('team_name')
        ).select_from(Games).join(Tournament, Games.id == Tournament.id_games).join(Team).join(Team_To_Tournament, (Tournament.id == Team_To_Tournament.id_tournament) & (Team_To_Tournament.status_daftar == "approved") & (Team.id == Team_To_Tournament.id_team)).filter(
            Tournament.status == 'regis_open'
        ).order_by(Games.name.asc()).all()


        data = []
        tournament_data = {}
        for row in query:
            tourney_id = row.tourney_id
            if tourney_id not in tournament_data:
                tournament_data[tourney_id] = {
                    'tourney_id': tourney_id,
                    'tournament_name': row.name,
                    'games': {
                        'game_id': row.game_id,
                        'game_name': row.game_name,
                    },
                    'status': row.status,
                    'teams': []
                }
            tournament_data[tourney_id]['teams'].append({
                'team_id': row.team_id,
                'team_name': row.team_name
            })

        data = list(tournament_data.values())

        return jsonify(data)
    
    except Exception as e:
        return str(e)



# API to get Recommended tournament by user_id
def get_tournament(db, user_id):
    try:
        # Get User by User_id
        getUserGame = db.session.query(
            Games.id.label('game_id')
        ).select_from(Games).join(Team, Games.id == Team.id_games).filter(Team.created_by == user_id).first()

        # If user is not a team creator
        if getUserGame is None:
            return jsonify({
                'message': 'This user id is not able to register for a tournament, only a creator of a team.'
            })

        
        query = db.session.query(
            Tournament.id.label('tourney_id'),
            Tournament.name,
            Games.id.label('game_id'),
            Games.name.label('game_name'),
            Tournament.status,
            Team.id.label('team_id'),
            Team.name.label('team_name')
        ).select_from(Games).join(Tournament, Games.id == Tournament.id_games).join(Team, Games.id == Team.id_games).join(Team_To_Tournament, (Tournament.id == Team_To_Tournament.id_tournament) & (Team_To_Tournament.status_daftar == "approved") & (Team.id == Team_To_Tournament.id_team)).filter(
            Tournament.status == 'regis_open',
            Games.id == getUserGame[0]
        ).distinct(Tournament.id, Games.id, Team.id).all()


        results = []
        tournament_data = {}
        for row in query:
            tourney_id = row.tourney_id
            if tourney_id not in tournament_data:
                tournament_data[tourney_id] = {
                    'tourney_id': tourney_id,
                    'tournament_name': row.name,
                    'games': {
                        'game_id': row.game_id,
                        'game_name': row.game_name,
                    },
                    'status': row.status,
                    'teams': []
                }
            tournament_data[tourney_id]['teams'].append({
                'team_id': row.team_id,
                'team_name': row.team_name
            })

        results = list(tournament_data.values())

        return jsonify(results)
    except Exception as e:
        return str(e)
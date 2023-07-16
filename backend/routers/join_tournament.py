from models.model import Tournament, Games, Team, Team_To_Tournament
from flask import jsonify

def check_tournament(team_id, tournament_id):
    try:
        # Check if the team exist
        checkTeam = Team.query.filter(Team.id == team_id).first()
        if checkTeam is None:
            return jsonify({
                'message': 'This team is not valid'
            })

        # Check if the tournament exist
        checkTournament = Tournament.query.filter(Tournament.id == tournament_id).first()
        if checkTournament is None:
            return jsonify({
                'message': "This tournament doesn't exist"
            })

        # Check if the team is registered in a tournament
        query = Team_To_Tournament.query.filter(Team_To_Tournament.id_team == team_id, Team_To_Tournament.id_tournament == tournament_id).first()

        if query is None:
            return jsonify({
                'message': 'Not registered yet'
            })
        else:
            result = {
                'team_tournament_id': query.id,
                'team_id': query.id_team,
                'tournament_id': query.id_tournament,
                'status_daftar': query.status_daftar,
                'message': 'Your team already registered on this tournament'
            }

            return jsonify(result)
    except Exception as e:
        return str(e)
    

def join_tournament(db, team_id, tournament_id):
    try:
        register_tourney = Team_To_Tournament(id_team=team_id, id_tournament=tournament_id, status_daftar="waiting")
        db.session.add(register_tourney)
        db.session.commit()
        return jsonify({
            'message': "Team registered successfully, you'll be notified if your the status is updated"
        })
    except Exception as e:
        return str(e)

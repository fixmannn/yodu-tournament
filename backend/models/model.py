from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    status = db.Column(db.Enum("active", "inactive"), nullable = False)
    teams = db.relationship("Team", backref="created_by_id")


class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    created_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False)
    status = db.Column(db.Enum("active", "inactive"), nullable = False)
    id_games = db.Column(db.Integer, db.ForeignKey("games.id"), nullable = False)
    users = db.relationship("User")
    games = db.relationship("Games")
    team_tournament = db.relationship("Team_To_Tournament")

class Games(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    status = db.Column(db.Enum("active", "inactive"))
    games = db.relationship("Team", backref="team_games_id")
    tournament = db.relationship("Tournament", backref="tournament_games_id")


class Tournament(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255), nullable = False)
    status = db.Column(db.Enum("regis_open", "ongoing", "finished"))
    id_games = db.Column(db.Integer, db.ForeignKey("games.id"), nullable = False)
    max_slot = db.Column(db.Integer, nullable = False)
    team_tournament = db.relationship("Team_To_Tournament", backref="team_tournament_id")

class Team_To_Tournament(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    id_team = db.Column(db.Integer, db.ForeignKey("team.id"), nullable = False)
    id_tournament = db.Column(db.Integer, db.ForeignKey("tournament.id"), nullable = False)
    status_daftar = db.Column(db.Enum("waiting", "pending", "approved", "rejected"), nullable = False)
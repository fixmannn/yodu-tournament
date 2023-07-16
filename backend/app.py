from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

app = Flask(__name__)
app.json.sort_keys = False

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/yodu_tournament"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from seeders.seeder import seed_database
from routers.get_tournament import recommended_tournament, get_tournament
from routers.join_tournament import check_tournament, join_tournament

# Execute database model and seeder
with app.app_context():
    inspector = inspect(db.engine)

    if not inspector.has_table('user') or not inspector.has_table('team') or not inspector.has_table('games') or not inspector.has_table('tournament') or not inspector.has_table('team__to__tournament'):
        db.create_all()

        # Dummy data, you can delete this command if you don't want to run the seeder
        seed_database(db)


# App routes

# To get all tournaments
@app.get("/recommended_tournament")
def tournament_recommendation():
    return recommended_tournament(db)

# To get tournaments based on user_id
@app.get("/recommended_tournament/<user_id>")
def tournament_by_userId(user_id):
    return get_tournament(db, user_id)

@app.get("/join_tournament/<team_id>/<tournament_id>")
def check_team(team_id, tournament_id):
    return check_tournament(team_id, tournament_id)

@app.post("/join_tournament/<team_id>/<tournament_id>")
def register_tournament(team_id, tournament_id):
    return join_tournament(db, team_id, tournament_id)

if __name__ == "__main__":
    app.run(debug=True)



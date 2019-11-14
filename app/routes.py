from app import app, db
from app.models import Team
from flask import request, jsonify

@app.route('/get_team_data', methods=['GET'])
def get_all_team_data():
    team_data = Team.query.all()
    team_data = [{'team name':team.name, 'points against qb': team.pa_qb, 'points against wr': team.pa_wr, 'points against rb': team.pa_rb, 'points against te': team.pa_te} for team in team_data]
    return jsonify({'Requested team data': team_data}), 200


@app.route('/add_team_data', methods=['POST'])
def add_team_data():
    team_name = request.json.get('team_name')
    pa_qb = request.json.get('pa_qb')
    pa_wr = request.json.get('pa_wr')
    pa_rb = request.json.get('pa_rb')
    pa_te = request.json.get('pa_te')

    team = Team(name=team_name, pa_qb=pa_qb, pa_wr=pa_wr, pa_te=pa_te)
    db.session.add(team)
    db.session.commit()
    return jsonify({'Success':'New team data added', 'team name': team_name, 'points against qb': pa_qb, 'points against wr': pa_wr, 'points against rb': pa_rb, 'points against te': pa_te}), 201

#curl -i -X POST -H "Content-Type: application/json" -d '{"team_name":"team name", "pa_qb":0.0, "pa_wr":0.0, "pa_rb":0.0, "pa_te":0.0}' http://localhost:5000/add_team_data
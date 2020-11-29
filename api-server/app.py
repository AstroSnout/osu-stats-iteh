from flask import Flask, request
import json

from shared.models.users import MyUsers
from shared.models.beatmaps import MyBeatmaps
from shared.models.scores import MyScores
from shared.queries import PremadeQueries
from db import db
import db as dbpy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1:3306/osu_simplified'
app.config['SQLALCHEMY_BINDS'] = {
    'osu_official': 'mysql://root:@127.0.0.1:3306/osu_official'
}

db.init_app(app)

with app.app_context():
    # noinspection PyBroadException
    try:
        # Will try to fetch first row
        # Exception if table not present, so init process starts
        # If no result, populates the table
        if not MyUsers.query.first():
            dbpy.fill_my_users()
        if not MyScores.query.first():
            dbpy.fill_my_scores()
        if not MyBeatmaps.query.first():
            dbpy.fill_my_beatmaps()
            dbpy.enabled_mods_num_to_mod()
    except:
        dbpy.init_all_tables()


@app.route('/api/', methods=['GET'])
def api_home():
    return f"<h1>Some Basic API</h1><br>"


@app.route('/api/get_user', methods=['GET'])
def api_get_user():
    # Needs uid or uname to find the specified user
    if 'uid' in request.args:
        uid = int(request.args['uid'])
        user = MyUsers.query.filter_by(user_id=uid).first_or_404(description=f'No user with id {uid} was found.')
    elif 'uname' in request.args:
        uname = request.args['uname']
        user = MyUsers.query.filter_by(username=uname).first_or_404(description=f'No user with username {uname} was found.')
    else:
        return "Error: No uid field provided. Please specify a user id."

    return json.dumps(user.serialize())


@app.route('/api/get_beatmap', methods=['GET'])
def api_get_beatmap():
    # Needs bid to find the specified beatmap
    if 'bid' in request.args:
        bid = int(request.args['bid'])
    else:
        return "Error: No bid field provided. Please specify a beatmap id."

    beatmap = MyBeatmaps.query.filter_by(beatmap_id=bid).first_or_404(description=f'No beatmap with id {bid} was found.')

    return json.dumps(beatmap.serialize())


@app.route('/api/get_top_maps', methods=['GET'])
def top_maps():
    # Top maps by occurrence for player ranks within selected range, for selected mods and strictness (optional)
    if 'urank' not in request.args or 'urange' not in request.args:
        return "Missing arguments"

    if 'mods' not in request.args:
        enabled_mods = ''
    else:
        enabled_mods = request.args['mods']

    if 'strict' not in request.args:
        strict_mode = False
    else:
        if request.args['strict'] == 'true':
            strict_mode = True
        elif request.args['strict'] == 'false':
            strict_mode = False
        # Invalid input for 'strict', defaults to false
        else:
            strict_mode = False

    try:
        urank = int(request.args['urank'])
        urange = int(request.args['urange'])
    except ValueError:
        return "The values provided for 'urank' and/or 'urange' are not integers"

    result = db.engine.execute(PremadeQueries.top_plays(urank, urange, enabled_mods, strict_mode))
    list_of_dicts = [{key: value for (key, value) in row.items()} for row in result]

    return json.dumps(sorted(list_of_dicts, key=lambda i: i['occurrence'], reverse=True))












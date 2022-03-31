import os
from flask import Flask, g, session, redirect, request, url_for, jsonify
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
import json
import pymongo
import pickle
from config import new_user
load_dotenv()

OAUTH2_CLIENT_ID = os.environ['OAUTH2_CLIENT_ID']
OAUTH2_CLIENT_SECRET = os.environ['OAUTH2_CLIENT_SECRET']
OAUTH2_REDIRECT_URI = 'https://ofc-watch.kulimi.tw/api/callback'
API_BASE_URL = os.environ.get('API_BASE_URL', 'https://discordapp.com/api')
AUTHORIZATION_BASE_URL = API_BASE_URL + '/oauth2/authorize'
TOKEN_URL = API_BASE_URL + '/oauth2/token'


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = OAUTH2_CLIENT_SECRET

mgclient = pymongo.MongoClient(os.getenv('dbconnect'))

ofc_db = mgclient.ofc
user_collection = ofc_db.user
data_collection = ofc_db.data

if 'http://' in OAUTH2_REDIRECT_URI:
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'true'


@app.before_request
def make_session_permanent():
    session.permanent = True


def token_updater(token):
    session['oauth2_token'] = token


def make_session(token=None, state=None, scope=None):
    return OAuth2Session(
        client_id=OAUTH2_CLIENT_ID,
        token=token,
        state=state,
        scope=scope,
        redirect_uri=OAUTH2_REDIRECT_URI,
        auto_refresh_kwargs={
            'client_id': OAUTH2_CLIENT_ID,
            'client_secret': OAUTH2_CLIENT_SECRET,
        },
        auto_refresh_url=TOKEN_URL,
        token_updater=token_updater)





@app.route('/api/login')
def index():
    scope = request.args.get(
        'scope',
        'identify email guilds')
    discord = make_session(scope=scope.split(' '))
    authorization_url, state = discord.authorization_url(AUTHORIZATION_BASE_URL)
    session['oauth2_state'] = state
    return redirect(authorization_url)


@app.route('/api/callback')
def callback():
    if request.values.get('error'):
        return request.values['error']
    discord = make_session(state=session.get('oauth2_state'))
    token = discord.fetch_token(
        TOKEN_URL,
        client_secret=OAUTH2_CLIENT_SECRET,
        authorization_response=request.url.replace('http://', 'https://'))
    session['oauth2_token'] = token
    user = discord.get(API_BASE_URL + '/users/@me').json()
    session['discord_id'] = user['id']

    try:
        user_collection.insert_one(new_user(user, pickle.dumps(token)))
    except pymongo.errors.DuplicateKeyError:
        user_collection.replace_one({'_id': user['id']}, new_user(user, pickle.dumps(token)))
    return redirect('/welcome')


@app.route('/api/links')
def links():
    user_data = user_collection.find_one({'_id': session.get('discord_id')})
    return flask.Response(json.dumps(user_data['links']), mimetype='application/json')


@app.route('/api/<_round>')
@app.route('/api/<_round>/<param>')
@app.route('/api/<_round>/<param>/<_id>')
def api(_round, param = 'none', _id = '-1'):
    if not (str_is_safe(_round) and str_is_safe(param) and str_is_safe(_id)):
        return flask.Response(json.dumps({'text': 'Unsafe string detected.'}), mimetype='application/json')

    user_data = user_collection.find_one({'_id': discord_id})
    op_level = user_data['op']
    

    if (_id != '-1'):
        round_db = mgclient[f'ofc{_round}'.replace('.', '-')]
        data_collection = round_db[param]
        result = data_collection.find_one({"_id": _id})
        if not result:
            result = data_collection.find_one({"_id": int(_id)})

        if result.get('op', 1000) > op_level:
            return flask.Response(json.dumps({'text': '存取被拒'}), mimetype='application/json')
        else:
            return flask.Response(json.dumps(result), mimetype='application/json')

    elif (param != 'none'):
        round_db = mgclient[f'ofc{_round}'.replace('.', '-')]
        data_collection = round_db['data']
        result = data_collection.find_one({"_id": param})
        if not result:
            result = data_collection.find_one({"_id": int(param)})

        if result.get('op', 1000) > op_level:
            return flask.Response(json.dumps({'text': '存取被拒'}), mimetype='application/json')
        else:
            return flask.Response(json.dumps(result), mimetype='application/json')

    else:
        round_db = mgclient[f'ofc'.replace('.', '-')]
        data_collection = round_db['data']
        result = data_collection.find_one({"_id": _round})
        if result.get('op', 1000) > op_level:
            return flask.Response(json.dumps({'text': '存取被拒'}), mimetype='application/json')
        else:
            return flask.Response(json.dumps(result), mimetype='application/json')


if __name__ == '__main__':
    app.run(port=9000)

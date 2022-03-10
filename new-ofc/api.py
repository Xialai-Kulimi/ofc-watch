import flask
import json 
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()

app = flask.Flask(__name__)
mgclient = pymongo.MongoClient(os.getenv('dbconnect'))

ofc_db = mgclient.ofc
data_collection = ofc_db.data


@app.route('//<_round>')
@app.route('//<_round>/<param>')
@app.route('//<_round>/<param>/<id>')
def api(_round, param = '', _id = -1):

    if (_id != -1):
        round_db = mgclient[f'ofc{_round}'.replace('.', '-')]
        data_collection = round_db[param]
        result = data_collection.find_one({"_id": _id})
        return flask.Response(json.dumps(result), mimetype='application/json')
    elif (param != ''):
        round_db = mgclient[f'ofc{_round}'.replace('.', '-')]
        data_collection = round_db['data']
        result = data_collection.find_one({"_id": param})
        return flask.Response(json.dumps(result['data']), mimetype='application/json')
    else:
        round_db = mgclient[f'ofc'.replace('.', '-')]
        data_collection = round_db['data']
        result = data_collection.find_one({"_id": _round})
        return flask.Response(json.dumps(result['data']), mimetype='application/json')


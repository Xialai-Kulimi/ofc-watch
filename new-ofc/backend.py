import flask
import json 
import pymongo
from dotenv import load_dotenv
import os
load_dotenv()

app = flask.Flask(__name__, static_folder = "./dist/static", template_folder = "./dist")
mgclient = pymongo.MongoClient(os.getenv('dbconnect'))

ofc_db = mgclient.ofc
data_collection = ofc_db.data

def str_is_safe(strs):
    for _char in strs:
        if not ('\u4e00' <= _char <= '\u9fa5' or 33 <= ord(_char) <= 126):
            return False
    return True


@app.route('/api/<_round>')
@app.route('/api/<_round>/<param>')
@app.route('/api/<_round>/<param>/<_id>')
def api(_round, param = 'none', _id = '-1'):
    if not (str_is_safe(_round) and str_is_safe(param) and str_is_safe(_id)):
        return flask.Response(json.dumps({'text': 'Unsafe string detected.'}), mimetype='application/json')
        
    if (_id != '-1'):
        round_db = mgclient[f'ofc{_round}'.replace('.', '-')]
        data_collection = round_db[param]
        result = data_collection.find_one({"_id": _id})
        if not result:
            result = data_collection.find_one({"_id": int(_id)})
        return flask.Response(json.dumps(result), mimetype='application/json')
    elif (param != 'none'):
        round_db = mgclient[f'ofc{_round}'.replace('.', '-')]
        data_collection = round_db['data']
        result = data_collection.find_one({"_id": param})
        if not result:
            result = data_collection.find_one({"_id": int(param)})
        return flask.Response(json.dumps(result['data']), mimetype='application/json')
    else:
        round_db = mgclient[f'ofc'.replace('.', '-')]
        data_collection = round_db['data']
        result = data_collection.find_one({"_id": _round})
        return flask.Response(json.dumps(result['data']), mimetype='application/json')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


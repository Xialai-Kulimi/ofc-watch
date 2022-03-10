import flask
import json 
import pymongo
from dotenv import load_dotenv
import os


app = flask.Flask(__name__)
mgclient = pymongo.MongoClient(os.getenv('dbconnect'))

ofc_db = mgclient.ofc
data_collection = ofc_db.data


@app.route('/api/<round>')
@app.route('/api/<round>/<param>')
@app.route('/api/<round>/<param>/<id>')
def text(round, param='', id=0):
    if (param=='' and id==0):
        result = data_collection.find_one({"name": round})
        if result:
            return flask.Response(json.dumps(result.data), mimetype='application/json')

    round_db = mgclient[f'ofc{_round}'.replace('.', '-')]
    return flask.Response(json.dumps(t), mimetype='application/json')


if __name__ == '__main__':
    app.run(port=9000)
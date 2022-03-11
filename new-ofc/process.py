import os
from dotenv import load_dotenv
import sys
import json
import pymongo
load_dotenv()

_round = sys.argv[1]

mgclient = pymongo.MongoClient(os.getenv('dbconnect'))
ofc_db = mgclient[f'ofc{_round}'.replace('.', '-')]
report_collection = ofc_db['report']


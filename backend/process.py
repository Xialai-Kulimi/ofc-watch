import os
from dotenv import load_dotenv
import sys
import json
import pymongo
import time
import anautils
load_dotenv()

_round = sys.argv[1]

mgclient = pymongo.MongoClient(os.getenv('dbconnect'))
ofc_db = mgclient[f'ofc{_round}'.replace('.', '-')]
report_collection = ofc_db['report']


anautils.anautils(ofc_db, mgclient.ofc)

if not ofc_db['data'].find_one({'_id': 'data'}):
	print(f'Detect new round: {_round}')
	ofc_db['data'].insert_one(
		{
			'_id': 'data',
			'last_work_report': 0,
		}
	)

if not ofc_db['data'].find_one({'_id': 'op_dict'}):
	ofc_db['data'].insert_one(
		{
			'_id': 'op_dict',
			'last_work_report': 0,
		}
	)
		

while True:
	ofc_data = ofc_db['data'].find_one({'_id': 'data'})
	last_work_report = ofc_data['last_work_report']
	report_list = report_collection.find({'_id': {'$gt': last_work_report}}, limit=1000).sort('_id')
	for i in report_list:
		if i['_id'] % 100 == 0:
			print(i['_id'])
		report = anautils.Report(i)
		anautils.player(report)
		anautils.match(report)
		anautils.events(report)
		anautils.weapon(report)
		anautils.hunt(report)
		
	try:
		pass
		# for i in report_list:
		# 	anautils.player(i)
		# 	anautils.match(i)
		# 	anautils.weapon(i)
		# 	anautils.hunt(i)

	except Exception as e:
		print(i)
		print(e)
		exit()
	
	ofc_db['data'].update_one({'_id': 'data'}, {"$set": {'last_work_report': i['_id']}})
	anautils.unify()



	time.sleep(1)

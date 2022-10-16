import requests
import time
import os
from dotenv import load_dotenv
import sys
import json
import pymongo
import datetime
load_dotenv()


def get_report(report_id):
    headers = {
        'User-Agent': 'I just wanna know all the secret data',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Origin': 'https://swordgale.online/',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }
    get_response = requests.get(f'https://api.swordgale.online/api/report/{report_id}', headers=headers)

    return get_response


_round = sys.argv[1]

initial_wait_time = 10
wait_time = initial_wait_time
wait_time_rate = 1.5
max_wait_time = 600
mgclient = pymongo.MongoClient(os.getenv('dbconnect'))
ofc_db = mgclient[f'ofc{_round}'.replace('.', '-')]
report_collection = ofc_db['report']


try:
    last_id = report_collection.find_one(sort=[("_id", -1)])['_id']
    if last_id != report_collection.count_documents({}):
        for i in range(1, last_id):
            if report_collection.find_one({"_id": i}) == None:
                response = get_report(i)
                report = json.loads(response.text)
                if status_code.status_code != 200:
                    print(response.text)
                    stop()

                report['_id'] = i
                report_collection.insert_one(report)

        i += 1
    else:
        i = report_collection.count_documents({}) + 1

except:
    i = 1

while True:
    print(i)
    initial_time = time.time()  # Record initial time.

    _response = get_report(i)
    print(_response.text)

    if _response.status_code == 200:
        try:
            line_dict = json.loads(_response.text)
            line_dict['_id'] = i
            report_collection.insert_one(line_dict)

            i += 1
            wait_time = initial_wait_time
            continue
        except Exception as e:
            print(e)
            print(f'Error occur while downloading report. : {i}')
            print(_response.text)

    elif _response.status_code == 400:
        print(f'Last report: {i}')

    time_use = time.time() - initial_time
    print(f'use {time_use}sec')

    time.sleep(wait_time)




    wait_time = wait_time * wait_time_rate
    if wait_time > max_wait_time:
        wait_time = max_wait_time



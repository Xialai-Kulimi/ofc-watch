import json
import time
import logging
import re
import os
from dotenv import load_dotenv
import sys
import pathlib


load_dotenv()

# =======Config=======
logging.basicConfig(level=logging.NOTSET)
try: round = sys.argv[1]
except IndexError: round = '6'
web_root = os.getenv('web-root')
record_path = os.path.join(web_root, 'ofc', f'{round}.ofc')

# =======Initialize=======
report_line_graph = {}
floor_line_graph = []
kill_count = {}
killed_count = {}
weapon_count = {}
hour_count = {}
times_count = {}
damage_count = {}
damaged_count = {}
loot_index = []
xp_count = {}
loot_count = {}
loot_list = {}
weapon_list = []
castle_damage = {}

global_weapon_list = []

match_db = {}
player_db = {}

faction_damage = {}
faction_damaged = {}
faction_times = {}
faction_loot = {}

faction_list = []

global_kill_count = 0

report_check_list = [1 for i in range(len(os.listdir(os.path.join(web_root, 'ofc', round))))]

for file in os.listdir(os.path.join(web_root, 'ofc', round)):

    try:
        with open(os.path.join(web_root, 'ofc', round, file)) as f:
            line_dict = json.loads(f.read().strip())
    except Exception as e:
        logging.error(e)
        logging.warning(f'error: Can not jsonlize. file: {file}')
        logging.warning(f.read().strip())
        continue

    match_db[line_dict['report']['id']] = line_dict

    report_check_list[line_dict['report']['id']] = 0

    report_line_graph[str(int((line_dict['report']['time']) / 60000) * 60000)] = report_line_graph.get(str(int((line_dict['report']['time']) / 3600000) * 3600000), 0) + 1
    if line_dict['report']['aFactionName'] not in faction_list: faction_list.append(line_dict['report']['aFactionName'])
    if line_dict['report']['bFactionName'] not in faction_list: faction_list.append(line_dict['report']['bFactionName'])
    times_count[line_dict['report']['aName']] = times_count.get(line_dict['report']['aName'], 0) + 1
    if line_dict['report']['bName']: times_count[line_dict['report']['bName']] = times_count.get(line_dict['report']['bName'], 0) + 1
    if line_dict['report']['location'][:len(line_dict['report']['aFactionName'])] != line_dict['report'][
        'aFactionName']: faction_times[line_dict['report']['aFactionName']] = faction_times.get(
        line_dict['report']['aFactionName'],
        0) + 1
    for fighter in line_dict['report']['messages']['stats']:
        player_db[line_dict['report']['messages']['stats'][fighter]['name']] = line_dict['report']['messages']['stats'][fighter]
        player_db[line_dict['report']['messages']['stats'][fighter]['name']]['faction'] = line_dict['report'][f'{fighter}FactionName']

    for message in line_dict['report']['messages']['messages']:

        if message.get('s') == 'critical' and '被擊殺身亡了，' in message['m']:
            killed_name, kill_name = (line_dict['report']['aName'], line_dict['report']['bName']) if message['m'].split('被擊殺身亡了，')[0] == line_dict['report']['aName'] else (line_dict['report']['bName'], line_dict['report']['aName'])
            if kill_name in kill_count:
                kill_count[kill_name] += 1
            else:
                kill_count[kill_name] = 1
            if killed_name in killed_count:
                killed_count[killed_name] += 1
            else:
                killed_count[killed_name] = 1

        if message['m'][-3:] == '點傷害':
            p = re.compile(r'\d+')

            if message['m'][:len(line_dict['report']['aName'])] == line_dict['report']['aName']:
                if line_dict['report']['bName']:
                    damage_count[line_dict['report']['aName']] = damage_count.get(line_dict['report']['aName'], 0) + int(p.findall(message['m'])[-1])
                    damaged_count[line_dict['report']['bName']] = damaged_count.get(line_dict['report']['bName'], 0) + int(p.findall(message['m'])[-1])
                    faction_damage[line_dict['report']['aFactionName']] = faction_damage.get(line_dict['report']['aFactionName'], 0) + int(p.findall(message['m'])[-1])
                    faction_damaged[line_dict['report']['bFactionName']] = faction_damage.get(line_dict['report']['bFactionName'], 0) + int(p.findall(message['m'])[-1])
                else:
                    castle_damage[line_dict['report']['aName']] = castle_damage.get(line_dict['report']['aName'], 0) + int(p.findall(message['m'])[-1])
            else:
                damage_count[line_dict['report']['bName']] = damage_count.get(line_dict['report']['bName'], 0) + int(
                    p.findall(message['m'])[-1])
                damaged_count[line_dict['report']['aName']] = damaged_count.get(line_dict['report']['aName'], 0) + int(
                    p.findall(message['m'])[-1])
                faction_damage[line_dict['report']['bFactionName']] = faction_damage.get(
                    line_dict['report']['bFactionName'], 0) + int(p.findall(message['m'])[-1])
                faction_damaged[line_dict['report']['aFactionName']] = faction_damaged.get(
                    line_dict['report']['aFactionName'], 0) + int(p.findall(message['m'])[-1])

    for message in line_dict['report']['messages']['messages']:
        if message.get('s') == 'info' and message['m'][-4:] == '點經驗值':
            xp_count[message['m'].split('獲得了')[-2]] = xp_count.get(message['m'].split('獲得了')[-2], 0) + int(
                message['m'].split(' ')[-2])

    for message in line_dict['report']['messages']['messages']:
        if message.get('s') == 'critical' and message['m'][:3] == '獲得了':
            loot_list[message['m'].split(' ')[3]] = loot_list.get(message['m'].split(' ')[3],
                                                                  {'floor': int(message['m'].split(' ')[1])})
            loot_count[line_dict['report']['aName']] = loot_count.get(line_dict['report']['aName'], []) + [
                                                           f"{line_dict['report']['bFactionName']}第{message['m'].split(' ')[1]}層：{message['m'].split(' ')[3]}"]
            if message['m'].split(' ')[3] not in loot_index: loot_index.append(message['m'].split(' ')[3])
            faction_loot[line_dict['report']['aFactionName']] = faction_loot.get(line_dict['report']['aFactionName'],
                                                                                 []) + [
                                                                    f"{line_dict['report']['bFactionName']}第{message['m'].split(' ')[1]}層：{message['m'].split(' ')[3]}"]
        if message.get('s') == 'critical' and message['m'].split(' ')[0] == '第' and message['m'].split(' ')[-1] == '層被摧毀了':
            floor_line_graph.append([line_dict['report']['time'], line_dict['report']['bFactionName'], message['m'].split(' ')[1]])

    this_hour = time.localtime(int(line_dict['report']['time']) / 1000).tm_hour
    hour_count[this_hour] = hour_count.get(this_hour, 0) + 1

    for weapon in line_dict['report']['messages']['stats']['a']['equipments']:
        weapon['faction'] = line_dict['report']['aFactionName']
        weapon_count[weapon['type']] = weapon_count.get(weapon['type'], 0) + 1
        global_weapon_list.append(weapon)

    for weapon in line_dict['report']['messages']['stats'].get('b', {}).get('equipments', []):
        weapon['faction'] = line_dict['report']['bFactionName']
        weapon_count[weapon.get('type')] = weapon_count.get(weapon.get('type'), 0) + 1
        global_weapon_list.append(weapon)

for i in range(len(report_check_list)):
    if report_check_list[i] == 1:
        print(f'{i} miss')

hour_count_list = [0 for i in range(24)]

for i in range(0, 24):
    hour_count_list[i] = hour_count[i]

# =======Generate JSON file=======

with open(os.path.join(web_root, round, 'CastleDamage.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'damage': i[1]} for i in
                 sorted(castle_damage.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Damage.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'damage': i[1]} for i in
                 sorted(damage_count.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Damaged.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'damaged': i[1]} for i in
                 sorted(damaged_count.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Faction12.json'), 'w', encoding='utf8') as f:
    f.write(str(sorted(faction_list)).replace("'", '"'))

with open(os.path.join(web_root, round, 'Faction1.json'), 'w', encoding='utf8') as f:
    f.write(str([i[1] for i in sorted(faction_damage.items())]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Faction2.json'), 'w', encoding='utf8') as f:
    faction_exp = {}
    for fighter in player_db:
        faction_exp[player_db[fighter]['faction']] = faction_exp.get(player_db[fighter]['faction'], 0) + \
                                                     player_db[fighter]['fightExp']
    f.write(str([i[1] for i in sorted(faction_exp.items())]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Faction3.json'), 'w', encoding='utf8') as f:
    f.write(str([i[1] for i in sorted(faction_times.items())]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Faction4.json'), 'w', encoding='utf8') as f:
    faction_loot_count = {}
    for faction in faction_list:
        faction_loot[faction] = faction_loot.get(faction, [])
    for faction in faction_loot:
        faction_loot_count[faction] = len(faction_loot[faction])
    f.write(str([i[1] for i in sorted(faction_loot_count.items())]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Faction5.json'), 'w', encoding='utf8') as f:
    f.write(str([[f'{str(time.localtime(int(i[0]) / 1000).tm_min).zfill(2)}-{time.localtime(int(i[0]) / 1000).tm_hour}-{time.localtime(int(i[0]) / 1000).tm_mday}-{time.localtime(int(i[0]) / 1000).tm_mon}-{time.localtime(int(i[0]) / 1000).tm_year}', i[1], i[2]] for i in floor_line_graph]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Faction6.json'), 'w', encoding='utf8') as f:
    f.write('''[{
  "name": "Time",
  "type": "date",
  "format": "%M-%H-%d-%m-%Y"
}, {
  "name": "Type",
  "type": "string"
}, {
  "name": "樓層數",
  "type": "number"
}]''')

with open(os.path.join(web_root, round, 'Kill.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'kill': i[1]} for i in sorted(kill_count.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Killed.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'killed': i[1]} for i in sorted(killed_count.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Loot.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'times': len(i[1]), 'loots': "、".join(i[1])} for i in
                 sorted(loot_count.items(), key=lambda x: len(x[1]), reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'laList.json'), 'w', encoding='utf8') as f:
    laList = []
    for la in sorted(loot_list.items(), key=lambda x: x[1]['floor']):
        la_db = {}
        for weapon in global_weapon_list:
            if weapon['name'] == la[0]:
                la_db[str(weapon)] = la_db.get(str(weapon), 0) + 1
        try: true_la = sorted(la_db.items(), key=lambda x: x[1], reverse=True)[0]
        except IndexError:
            with open(os.path.join(pathlib.Path(__file__).parent.absolute(), round, 'Unknown.json'), 'r', encoding='utf8') as unknown_f:
                unknown_las = json.loads(unknown_f.read())
                for unknown_la in unknown_las:
                    if unknown_la['name'] == la[0]:
                        unknown_la['isUnknown'] = True
                        true_la = (json.dumps(unknown_la, ensure_ascii=False), 0)
                        break
        true_la_dict = json.loads(true_la[0].replace("'", '"'))
        laList.append({'floor': la[1]['floor'], 'name': true_la_dict['name'], 'quality': true_la_dict.get('quality', "未知"),
                       'type': true_la_dict.get('type', "未知"), 'atk': true_la_dict.get('atk', "未知"), 'def': true_la_dict.get('def', "未知"),
                       'minePower': true_la_dict.get('minePower', "未知"), 'times': true_la[1], 'isUnknown': true_la_dict.get('isUnknown', False)})

    f.write(json.dumps(laList, ensure_ascii=False).replace("'", '"'))

with open(os.path.join(web_root, round, 'Report1.json'), 'w', encoding='utf8') as f:
    f.write(str(hour_count_list).replace("'", '"'))

with open(os.path.join(web_root, round, 'Report2.json'), 'w', encoding='utf8') as f:
    f.write(str([[f'{str(time.localtime(int(i[0])/1000).tm_min).zfill(2)}-{time.localtime(int(i[0])/1000).tm_hour}-{time.localtime(int(i[0])/1000).tm_mday}-{time.localtime(int(i[0])/1000).tm_mon}-{time.localtime(int(i[0])/1000).tm_year}', "戰報數", i[1]] for i in
                 sorted(report_line_graph.items(), key=lambda x: x[0])]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Report3.json'), 'w', encoding='utf8') as f:
    f.write('''[{
  "name": "Time",
  "type": "date",
  "format": "%M-%H-%d-%m-%Y"
}, {
  "name": "Type",
  "type": "string"
}, {
  "name": "戰報數",
  "type": "number"
}]''')

with open(os.path.join(web_root, round, 'Times.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'times': i[1]} for i in sorted(times_count.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Weapon1.json'), 'w', encoding='utf8') as f:
    f.write(str([weapon_count[i] for i in weapon_count]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Weapon2.json'), 'w', encoding='utf8') as f:
    f.write(str([i for i in weapon_count]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Weapon3.json'), 'w', encoding='utf8') as f:
    a = 0
    for weapon in global_weapon_list:
        if weapon['name'] in loot_index:
            a += 1
    f.write(str([len(global_weapon_list) - a, a]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Weapon4.json'), 'w', encoding='utf8') as f:
    weapon_name_count = {}
    for weapon in global_weapon_list:
        weapon_name_count[str([weapon['name'], weapon['faction'], weapon['type']])] = weapon_name_count.get(str([weapon['name'], weapon['faction'], weapon['type']]), 0) + 1
    f.write(str([{'name': eval(i[0])[0], 'faction': eval(i[0])[1], 'type': eval(i[0])[2], 'times': i[1]} for i in sorted(weapon_name_count.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))

with open(os.path.join(web_root, round, 'Xp.json'), 'w', encoding='utf8') as f:
    f.write(str([{'name': i[0], 'faction': player_db[i[0]]['faction'], 'xp': i[1]} for i in sorted(xp_count.items(), key=lambda x: x[1], reverse=True)]).replace("'", '"'))



import hashlib


def sha256(text):
	h = hashlib.new('sha256')
	h.update(bytes(text, 'utf8'))
	return h.hexdigest()



def anautils(db, _config_db):
	global ofc_db, config_db, data_collection, player_collection, match_collection, report_collection, weapon_collection, _round
	ofc_db = db
	config_db = _config_db
	data_collection = ofc_db['data']
	player_collection = ofc_db['player']
	match_collection = ofc_db['match']
	report_collection = ofc_db['report']
	weapon_collection = ofc_db['weapon']

	_round = ofc_db.name.replace('ofc', '').replace('-', '.')

	data_collection.delete_many({})

	data_collection.insert_one({'_id': 'leaderboard'})
	data_collection.insert_one({'_id': 'hunt_events', 'data': []})
	data_collection.insert_one({'_id': 'castle_events', 'data': []})
	data_collection.insert_one({'_id': 'hunts'})
	data_collection.insert_one({'_id': 'weapon_type_count', 'data': []})



def test():
	print(ofc_db['report'].find_one({}))


def get_player_db(_id):
	return player_collection.find_one({'_id': _id})


def check_or_create_player(_id):
	if (player_collection.find_one({'_id': _id}) == None):
		player_collection.insert_one(
			{
				'_id': _id,
				'name': '',
				'role': '',
				'role2': '',
				'faction': '',
				'weapon': [],
				'stat': '',
				'kill': 0,
				'bekill': 0,
				'damage': 0,
				'bedamage': 0,
				'wall_damage': 0,
				'all_xp': 0,
				'battle_xp': 0,
				'adventure_xp': 0,
				'hunt_xp': 0,
				'battle_count': 0,
				'hunt_count': 0,
				'now_hunt': [],
				'hunts': [],
				'report_summary': []
			}
		)

def get_equipment_id(equipment):
	return sha256(str(equipment))
	


def check_or_create_equipment(equipment):
	_id = get_equipment_id(equipment)
	if (weapon_collection.find_one({'_id': _id}) == None):
		equipment_base = {'_id': _id, 'count': 1, 'round': _round}
		equipment_base['data'] = equipment
		weapon_collection.insert_one(equipment_base)


def add_equipments_appear_count(equipment):
	_id = get_equipment_id(equipment)
	weapon_collection.update_one({'_id': _id}, {"$inc": {'count': 1}})


def equipment_type_add(equipment):
	weapon_type_count = data_collection.find_one({'_id': 'weapon_type_count'})['data']
	if equipment['type'] not in [t['name'] for t in weapon_type_count]:
		weapon_type_count.append({'name': equipment['type'], 'count': 1})
	else:
		for t in weapon_type_count:
			if t['name'] == equipment['type']:
				t['count'] += 1
	data_collection.update_one({'_id': 'weapon_type_count'}, {"$set": {'data': weapon_type_count}})




def player_stat_add(_id, field, amount):
	check_or_create_player(_id)
	player_collection.update_one({'_id': _id}, {"$inc": {field: amount}})


def player_stat_set(_id, field, amount):
	check_or_create_player(_id)
	player_collection.update_one({'_id': _id}, {"$set": {field: amount}})


def report_stat(report):
	return report['report']['messages']['stats']

def messages(report):
	return report['report']['messages']['messages']


def report_is_hunt(report):
	return (report['report'].get('bFactionName') == None) and (report['report'].get('bId') == None)


def report_is_wall(report):
	return (not report_is_hunt(report)) and (not report['report'].get('bId'))


def report_is_solo(report):
	return report_is_hunt(report) or report_is_wall(report)


def a_gain_xp(report):
	for m in messages(report):
		if m['m'].endswith('點經驗值') and m['s'] == 'info':
			if report_is_hunt:
				return int(m['m'].split(' ')[-2])
			else:
				if m['m'].startswith(report['report']['aName']):
					return int(m['m'].split(' ')[-2])
	return 0


def b_gain_xp(report):
	if report_is_solo(report):
		return 0
	for m in messages(report):
		if m['m'].endswith('點經驗值') and m['s'] == 'info':
			if m['m'].startswith(report['report']['bName']):
				return int(m['m'].split(' ')[-2])
	return 0


def a_deal_damage(report):
	if report_is_wall(report):
		for m in messages(report):
			if m['m'].split(' ')[0] == f"{report_stat(report)['a']['name']}直接攻擊城堡，造成":
				return int(m['m'].split(' ')[-2])
	else:
		damage = 0
		for m in messages(report):
			if m['m'].endswith('點傷害') and m['m'].split(' ')[-3].endswith(f"對{report_stat(report)['b']['name']}造成"):
				damage += int(m['m'].split(' ')[-2])
		return damage
	return 0


def b_deal_damage(report):
	if report_is_solo(report):
		return 0
	damage = 0
	for m in messages(report):
		if m['m'].endswith('點傷害') and m['m'].split(' ')[-3].endswith(f"對{report_stat(report)['a']['name']}造成"):
			damage += int(m['m'].split(' ')[-2])
	return damage


def a_take_damage(report):
	if report_is_wall(report):
		for m in messages(report):
			if m['m'].split(' ')[0] == f"{report_stat(report)['a']['name']}在攻城過程中消耗了":
				return int(m['m'].split(' ')[-2])
	else:
		return b_deal_damage(report)


def b_take_damage(report):
	return a_deal_damage(report)


def a_died(report):
	if report_is_wall(report):
		return a_take_damage(report) >= report_stat(report)['a']['hp']
	else:
		for m in messages(report):
			if m['m'].split(' ')[0] == f"{report_stat(report)['a']['name']}被擊殺死亡了，{report_stat(report)['b']['name']}還有" and m['s'] == 'critical':
				return True
		return False


def b_died(report):
	if report_is_wall(report):
		return False
	for m in messages(report):
		if m['m'].split(' ')[0] == f"{report_stat(report)['b']['name']}被擊殺死亡了，{report_stat(report)['a']['name']}還有" and m['s'] == 'critical':
			return True
	return False


def report_equipments(report):
	equipment_list = []
	for p in report_stat(report):
		for e in report_stat(report)[p]['equipments']:
			equipment_list.append(e)
	return equipment_list


def report_summary(report):
	if report_is_wall(report):
		for m in messages(report)[::-1]:
			if m.get('s') == 'critical' or m['m'].split(' ')[0] == f"{report_stat(report)['a']['name']}直接攻擊城堡，造成":
				return m['m']

	elif report_is_hunt(report):
		if not (a_died(report) or b_died(report)):
			for m in messages(report):
				if m.get('s') == 'info':
					return m['m']
		else:
			for m in messages(report)[::-1]:
				if m.get('s') == 'critical':
					return m['m']
	else:
		if a_died(report) or b_died(report):
			for m in messages(report)[::-1]:
				if m.get('s') == 'critical':
					return m['m']
		else:
			for m in messages(report):
				if m.get('s') == 'info':
					return m['m']

def report_loot(report):
	if not report_is_hunt(report):
		return []
	for m in messages(report)


class Report():
	def __init__(self, report):
		self.report = report['report']
		self.id = report['_id']
		self.stat = report_stat(report)
		self.messages = messages(report)
		self.is_hunt = report_is_hunt(report)
		self.is_wall = report_is_wall(report)
		self.is_solo = report_is_solo(report)
		self.a_gain_xp = a_gain_xp(report)
		self.b_gain_xp = b_gain_xp(report)
		self.a_deal_damage = a_deal_damage(report)
		self.b_deal_damage = b_deal_damage(report)
		self.a_take_damage = a_take_damage(report)
		self.b_take_damage = b_take_damage(report)
		self.a_died = a_died(report)
		self.b_died = b_died(report)
		self.a = self.stat['a']
		self.b = self.stat.get('b')
		self.equipments = report_equipments(report)
		self.summary = report_summary(report)
		self.time = report['report']['time']
		self.location = report['report']['location']
		self.loot = report_loot(report)



def player(report):
	aId = report.report['aId']
	bId = report.report.get('bId')


	player_stat_set(aId, 'name', report.a['name'])
	player_stat_set(aId, 'role', report.a['role'])
	if report.a.get('role2'):
		player_stat_set(aId, 'role2', report.a['role2'])
	player_stat_set(aId, 'faction', report.report['aFactionName'])
	player_stat_set(aId, 'all_xp', report.a['fightExp'])


	if report.is_hunt:
		player_stat_add(aId, 'hunt_xp', report.a_gain_xp)
		player_stat_add(aId, 'hunt_count', 1)
	else:
		if report.is_wall:
			player_stat_add(aId, 'battle_xp', report.a_gain_xp)
			player_stat_add(aId, 'wall_damage', report.a_deal_damage)

		else:
			player_stat_set(bId, 'name', report.b['name'])
			player_stat_set(bId, 'all_xp', report.b['fightExp'])

			player_stat_add(aId, 'battle_xp', report.a_gain_xp)
			player_stat_add(bId, 'battle_xp', report.b_gain_xp)
			
			player_stat_set(bId, 'role', report.b['role'])
			if report.b.get('role2'):
				player_stat_set(bId, 'role2', report.b['role2'])

			player_stat_set(bId, 'faction', report.report['bFactionName'])

			if report.a_died:
				player_stat_add(aId, 'bekill', 1)
				player_stat_add(bId, 'kill', 1)
			if report.b_died:
				player_stat_add(bId, 'bekill', 1)
				player_stat_add(aId, 'kill', 1)

			
			player_stat_add(aId, 'damage', report.a_deal_damage)
			player_stat_add(bId, 'damage', report.b_deal_damage)

			player_stat_add(aId, 'bedamage', report.a_take_damage)
			player_stat_add(bId, 'bedamage', report.b_take_damage)

			player_stat_add(aId, 'battle_count', 1)
			player_stat_add(bId, 'battle_count', 1)


def match(report):
	pass


def events(report):
	if report.is_hunt:
		data_collection.update_one({'_id': 'hunt_events'}, {'$push': {'data': {'$each': [{'text': report.summary, 'time': report.time, 'link': f'/{_round}/history/{report.id}'}], '$position': 0}}})
	else:
		data_collection.update_one({'_id': 'castle_events'}, {'$push': {'data': {'$each': [{'text': report.summary, 'time': report.time, 'link': f'/{_round}/history/{report.id}'}, 'location': report.report['location']], '$position': 0}}})




def weapon(report):
	for e in report.equipments:
		check_or_create_equipment(e)
		add_equipments_appear_count(e)
		equipment_type_add(e)



def hunt(report):
	if not report.is_hunt:
		return
	area = ' '.join(report.location.split(' ')[:-1])
	level = int(report.location.split(' ')[-1])

	hunt_add_count(area, level)
	monster_add_loot(area, report.b['name'], report.loot)




def unify():
	leaderboard = []
	for board in config_db.data.find_one({'_id': 'config'})['leaderboard']:
		this_board = {}
		this_board['name'] = board['name']
		board_list = [{
			'faction': p['faction'],
			'name': p['name'],
			'id': p['_id'],
			'count': p[board['field']]
		} for p in player_collection.find().sort([(board['field'], -1)])]
		this_board['json'] = board_list
		leaderboard.append(this_board)

	data_collection.update_one({'_id': 'leaderboard'}, {"$set": {'data': leaderboard}})


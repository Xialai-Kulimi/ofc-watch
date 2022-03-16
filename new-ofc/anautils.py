

def anautils(db, _config_db):
	global ofc_db, config_db, data_collection, player_collection, match_collection, report_collection
	ofc_db = db
	config_db = _config_db
	data_collection = ofc_db['data']
	player_collection = ofc_db['player']
	match_collection = ofc_db['match']
	report_collection = ofc_db['report']
	weapon_collection = ofc_db['weapon']

	data_collection.delete_many({})

	data_collection.insert_one({'_id': 'leaderboard'})
	data_collection.insert_one({'_id': 'events'})
	data_collection.insert_one({'_id': 'hunts'})
	data_collection.insert_one({'_id': 'weapon_type_count'})



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

def check_or_create_weapon(_id):
	if (weapon_collection.find_one({'_id': _id}) == None):
		weapon_collection.insert_one(
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
	assert (not report_is_hunt(report)) and (not report_is_wall(report))
	damage = 0
	for m in messages(report):
		if m['m'].endswith('點傷害') and m['m'].split(' ')[-3].endswith(f"對{report_stat(report)['a']['name']}造成"):
			damage += int(m['m'].split(' ')[-2])
	return damage


def a_take_damage(report):
	return b_deal_damage(report)


def b_take_damage(report):
	return a_deal_damage(report)


def a_died(report):
	for m in messages(report):
		if m['m'].split(' ')[0] == f"{report_stat(report)['a']['name']}被擊殺死亡了，{report_stat(report)['b']['name']}還有" and m['s'] == 'critical':
			return True
	return False


def b_died(report):
	for m in messages(report):
		if m['m'].split(' ')[0] == f"{report_stat(report)['b']['name']}被擊殺死亡了，{report_stat(report)['a']['name']}還有" and m['s'] == 'critical':
			return True
	return False





class Report():
	def __init__(self, report):
		self.report = report
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
		self.a = self.stat.a
		self.b = self.stat.b



def player(report):

	# check_and_add_event(report)

	aId = report['report']['aId']
	bId = report['report'].get('bId')

	player_stat_set(aId, 'name', report_stat(report)['a']['name'])
	player_stat_set(aId, 'role', report_stat(report)['a']['role'])
	if report_stat(report)['a'].get('role2'):
		player_stat_set(aId, 'role2', report_stat(report)['a']['role2'])
	player_stat_set(aId, 'faction', report['report']['aFactionName'])
	player_stat_set(aId, 'all_xp', report_stat(report)['a']['fightExp'])


	if report_is_hunt(report):
		player_stat_add(aId, 'hunt_xp', a_gain_xp(report))
		player_stat_add(aId, 'hunt_count', 1)
	else:
		if report_is_wall(report):
			player_stat_add(aId, 'battle_xp', a_gain_xp(report))
			player_stat_add(aId, 'wall_damage', a_deal_damage(report))

		else:
			player_stat_set(bId, 'name', report_stat(report)['b']['name'])
			player_stat_set(bId, 'all_xp', report_stat(report)['b']['fightExp'])

			player_stat_add(aId, 'battle_xp', a_gain_xp(report))
			player_stat_add(bId, 'battle_xp', b_gain_xp(report))
			
			player_stat_set(bId, 'role', report_stat(report)['b']['role'])
			if report_stat(report)['b'].get('role2'):
				player_stat_set(bId, 'role2', report_stat(report)['b']['role2'])

			player_stat_set(bId, 'faction', report['report']['bFactionName'])

			if a_died(report):
				player_stat_add(aId, 'bekill', 1)
				player_stat_add(bId, 'kill', 1)
			if b_died(report):
				player_stat_add(bId, 'bekill', 1)
				player_stat_add(aId, 'kill', 1)

			
			player_stat_add(aId, 'damage', a_deal_damage(report))
			player_stat_add(bId, 'damage', b_deal_damage(report))

			player_stat_add(aId, 'bedamage', a_take_damage(report))
			player_stat_add(bId, 'bedamage', b_take_damage(report))

			player_stat_add(aId, 'battle_count', 1)
			player_stat_add(bId, 'battle_count', 1)


def match(report):
	pass


def weapon(report):
	if report_is_hunt(report):
	else:
		for p in report_stat(report):



def hunt(report):
	pass


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


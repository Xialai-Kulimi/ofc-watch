data_list = ['data']

data = {
	"_id": "data",
	"last_work_report": 0,
}

def new_user(user, token):
    return {
        '_id': user['id'],
        'token': token,
        'name': user['username'],
        'avatar': user['avatar'],
        'links': [
        	{'path': '', 'icon': 'mdi-monitor-eye'},
        	{'path': 'player', 'icon': 'mdi-account-eye'},
        	{'path': 'about', 'icon': 'mdi-file-eye-outline'},
        ]
        'discriminator': user['discriminator'],
        'op': 1
     }

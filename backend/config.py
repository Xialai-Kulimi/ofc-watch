data_list = ['data']

data = {
	"_id": "data",
	"last_work_report": 0,
}

def new_user(user, token)
    return {
        '_id': user['id'],
        'token': token,
        'name': user['username'],
        'avatar': user['avatar'],
        'links': []
        'discriminator': user['discriminator'],
        'op': 1
     }

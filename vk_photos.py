import requests
from pprint import pprint

class VK:

    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()

    def get_photos(self, count=5):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'album_id': 'profile',
            'extended': True,
            'count': count            
        }
        response = requests.get(url, params={**self.params, **params})
        return response.json()


with open('token.txt', 'rt') as file:
    access_token = file.readline() 

user_id = '8841655'
vk = VK(access_token, user_id)
pprint(vk.get_photos())

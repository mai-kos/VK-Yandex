import requests
import json

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

    def log_photos_data(self, class_instance):
        json_data = {'items': []}
        photos = class_instance.get_photos()['response']['items']
        for el in photos:
            likes = el['likes']['count']
            name = f'{likes}.jpg'
            size = el['sizes'][-1]['type']
            photo_data = {
                'file_name': name,
                'size': size
            }
            json_data['items'].append(photo_data)
        with open('photos.json', 'w') as f:
            json.dump(json_data, f, indent=2)
        return
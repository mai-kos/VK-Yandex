import requests
import json
import time

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
        url_list = []
        for el in photos:
            likes = el['likes']['count']
            name = f'{likes}.jpg'
            epoch_date = el['date']
            my_date = time.strftime('%Y-%m-%d', time.localtime(epoch_date))
            for line in json_data['items']:
                if line['file_name'] == name:
                    name = f'{my_date}.jpg'
            size = el['sizes'][-1]['type']
            url = el['sizes'][-1]['url']
            url_list.append(f'{url} \n')
            photo_data = {
                'file_name': name,
                'size': size 
            }
            json_data['items'].append(photo_data)
            with open('photos_urls.txt', 'w') as txt_urls:
                txt_urls.writelines(url_list)
        with open('photos.json', 'w') as f:
            json.dump(json_data, f, indent=2)
        return json_data
import requests
import json
from tqdm import tqdm 

class Yandex:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def create_folder(self, folder_name):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = self.get_headers()
        params = {'path': folder_name}
        response = requests.put(upload_url, headers=headers, params=params)
        return folder_name

    def upload_photos(self, folder):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        with open('photos_urls.txt', 'r') as file_1, open('photos.json', 'r') as file_2:
            data = json.loads(file_2.read())
            for el in tqdm(data['items'], desc='Uploading files', ncols=100):
                name = el['file_name']
                url = file_1.readline().strip()
                disk_file_path = f'{folder}/{name}'
                params = {'url': url, 'path': disk_file_path}
                response = requests.post(upload_url, headers=headers, params=params)
                response.raise_for_status()
                if response.status_code == 202:
                    continue
        print('The files have been successfully uploaded to your disk!')
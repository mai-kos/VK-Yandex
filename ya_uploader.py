import requests

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

    # def create_folder(self, disk_file_path):
    #     upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    #     headers = self.get_headers()
    #     params = {'path': disk_file_path}
    #     response = requests.put(upload_url, headers=headers, params=params)
    #     return disk_file_path

    # def upload_photos(self, disk_file_path, filename):
    #     href = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
    #     response = requests.put(href, data=open(filename, 'r'))
    #     response.raise_for_status()
    #     if response.status_code == 202:
    #         print('Success')

    def upload_photos(self, disk_file_path, url):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'url': url, 'path': disk_file_path}
        response = requests.post(upload_url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 202:
            print('Success')
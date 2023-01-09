import vk_photos
import ya_uploader
from pprint import pprint

def run_program():
    vk_user_id = input('Hi! Please enter your VK id.')
    yandex_token = input('Please enter your Yandex token.')
    user_vk = vk_photos.VK(vk_access_token, vk_user_id)
    user_disk = ya_uploader.Yandex(yandex_token)
    folder = input('Enter a new folder name.')
    user_disk.create_folder(folder)
    pprint(user_vk.log_photos_data(user_vk))
    user_disk.upload_photos(folder)
    return

if __name__ == '__main__':
    with open('token.txt', 'rt') as file:
        vk_access_token = file.readline() 

    run_program()

    

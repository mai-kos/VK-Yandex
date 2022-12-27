import vk_photos
import ya_uploader
from pprint import pprint

if __name__ == '__main__':
    with open('token.txt', 'rt') as file:
        vk_access_token = file.readline() 

    vk_user_id = '8841655'
    my_vk = vk_photos.VK(vk_access_token, vk_user_id)
    pprint(my_vk.log_photos_data(my_vk))
    pprint(my_vk.get_photos())  
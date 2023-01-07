import vk_photos
import ya_uploader
from pprint import pprint

if __name__ == '__main__':
    with open('token.txt', 'rt') as file:
        vk_access_token = file.readline() 

    with open('ya_token.txt', 'rt') as file:
        ya_access_token = file.readline()

    

    vk_user_id = '8841655'
    my_vk = vk_photos.VK(vk_access_token, vk_user_id)
    pprint(my_vk.log_photos_data(my_vk))
    print()
    # pprint(my_vk.get_photos())

    my_disk = ya_uploader.Yandex(ya_access_token)
    # my_disk.create_folder('VK_photos')
    my_disk.upload_photos('VK_photos')

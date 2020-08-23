
import random
import time
import os
os.system("pip install vk_api")
os.system("pip3 install vk_api")
import vk_api
login = input('Введите логин: ')
password = input('Введите пароль: ')
vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()
random123 = ['😀', '🙂', '😉','🙃','😇','😛','🧐','😍','🤔','☺','😐','😑','🤨','🤐','🤫','😶','😏','😴','😌']

while True:
	print(vk.status.set(text=random.choice(random123)))
	print('Статус изменен | The status has been changed.')
	print()
	time.sleep(300)

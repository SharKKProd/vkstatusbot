
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
	result = vk.status.set(text=random.choice(random123)
        if result == '1':
            print('Статус успешно поменен.')
        else:
	    print('Ошибка')
	print()
	time.sleep(300)

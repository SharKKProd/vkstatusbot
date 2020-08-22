import vk_api
import random
import time

login = input('Введите логин: ')
password = input('Введите пароль: ')
timer = input('Введите время ожидания в секундах (60 секунд - 1 минута): ')
vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()
random123 = ['😀', '🙂', '😉','🙃','😇','😛','🧐','😍','🤔','☺','😐','😑','🤨','🤐','🤫','😶','😏','😴','😌']

while True:
	print(vk.status.set(text=random.choice(random123)))
	print('Статус изменен | The status has been changed.')
	print()
	time.sleep(timer)

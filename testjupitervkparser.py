import vk
import datetime


vkid = 
session1 = vk.AuthSession(access_token='')
vk_api = vk.API(session1, v=5.62)

def get_user_status():
	value = vk_api.users.get(user_ids=vkid, fields='last_seen')
	print(value)  # <- получаешь данные вида [{'id': айди, 'first_name': 'Имя', 'last_name': 'Фамилия', 'last_seen': {'time': 1560796737, 'platform': 7}}]

	friends = vk_api.friends.get(user_id=vkid)
	print(friends)
get_user_status()

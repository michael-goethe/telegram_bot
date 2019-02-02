import requests
import bot
import json


token = bot.token

URL = 'https://api.telegram.org/bot' + token + '/'

# https://api.telegram.org/bot720795040:AAGogGQmkzoIEEGolIPd3FsaH8IbS-XY2pQ/



def get_updates():
	url = URL+'getupdates'
	rec = requests.get(url)
	return rec.json()

def get_message():
	data = get_updates()






def main():
	d = get_updates()
	with open('updates.json', 'w') as file:
		json.dump(d, file, indent=1, ensure_ascii = False)



if __name__ == '__main__':
	main()
import requests
import bot_toke
from time import sleep
from btc_cur import btc_currency
token = bot_toke.token

URL = 'https://api.telegram.org/bot' + token + '/'

# https://api.telegram.org/bot720795040:AAGogGQmkzoIEEGolIPd3FsaH8IbS-XY2pQ/



def get_updates():
	url = URL+'getupdates'
	rec = requests.get(url)
	return rec.json()

def get_message():
	data = get_updates()
	chat_id = data['result'][-1]['message']['chat']['id']
	message_text = data['result'][-1]['message']['text']
	update_id = data['result'][-1]['update_id']
	message = {'chat_id':chat_id, 'text':message_text, 'update_id':update_id}
	return message

def send_message(chat_id, text = 'please, try again'):

	url = URL + 'sendmessage?chat_id={}&text={}-here is the price'.format(chat_id, text)
	rec = requests.get(url)




def main():

	upd = 0
	test = btc_currency()
	while True:
		rec = get_message()
		if upd != rec['update_id']:		
			upd = rec['update_id']
			chat_id = rec['chat_id']
			text = rec['text']
			if text == 'currency':
				send_message(chat_id, test['ticker']['price'])
			
	# d = get_updates()
	# with open('updates.json', 'w') as file:
	# 	json.dump(d, file, indent=1, ensure_ascii = False)



if __name__ == '__main__':
	main()
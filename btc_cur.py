import requests

def btc_currency():
	url = 'https://api.cryptonator.com/api/ticker/btc-usd'
	test = requests.get(url).json()
	return test

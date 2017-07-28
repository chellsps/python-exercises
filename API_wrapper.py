import requests
from urllib.request import urlopen

def get_quote(ticker):
        quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
        r = requests.get(quote_url + ticker)
        print(r.json())
get_quote("aapl")

def get_quote_two(ticker):
	url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
	symbol = ticker
	data = urlopen(url+symbol)
	print("URLLIB", data.read())

get_quote_two("msft")
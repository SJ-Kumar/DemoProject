##bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin'
bitcoin_api_url = 'http://api.coinlayer.com/api/live?access_key=dd61c88c20c658209ab9639b8a5e29a9'
from http.client import responses
from urllib import response
import requests

def get_latest_bitcoin_price():
    response = requests.get (bitcoin_api_url)
    response_json = response.json()
    responses
    ##return float (response_json[0]['price_usd'])
    ##def main():
    price = get_latest_bitcoin_price()
    print ("Bitcoin Price is:"+ price)
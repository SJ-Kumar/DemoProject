from sqlite3.dbapi2 import _Parameters
import requests
from requests import Session
import secrets
from pprint import pprint as pp

class CMC:
  ##url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = headers = { 'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token,
    } 
        self.session = Session()
        self.session.headers.update (self.headers) 
    
    def getAllCoins(self):
        url = self.apiurl + 'v1/cryptocurrency/map'
        r = self.session.get(url)
        data = r.json()['data']
        return data
    def getPrice(self, symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.session.get(url)
        data = r.json()['data']
        return data    

cmc = CMC(secrets.API_KEY)

pp(cmc.getPrice('BTC'))
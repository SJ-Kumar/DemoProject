import requests
import pprint

r = requests.get("https://open.er-api.com/v6/latest/USD").json()

pp = pprint.PrettyPrinter(indent=4)

pp.pprint(r)
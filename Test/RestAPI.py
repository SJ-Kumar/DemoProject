import requests
from pprint import pprint as pp

##BASE_URL = 'https://margamfarms.onrender.com'

BASE_URL = 'https://fakestoreapi.com'

response = requests.get(f"{BASE_URL}/products?limit=3")
pp(response.json())
print("Response Code is:", response.status_code)

purchase_req = {
    "title": 'Groundnut Oil',
    "price": 25,
    "description": 'lorem ipsum set',
    "image": 'https://i.pravatar.cc',
    "category": 'electronic'
}

response = requests.post(f"{BASE_URL}/products", json=purchase_req)
print ("You can view the response:")
print(response.json())

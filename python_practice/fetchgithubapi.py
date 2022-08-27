import requests
from prettytable import PrettyTable

table = PrettyTable()
##table.field_names = ["Key", "Value"]
table.field_names = ["Repository Name", "Created Date"]

github_username  = "SJ-Kumar"

#api url to grab public user data
##api_url = f"https://api.github.com/users/{github_username}"

#api url to grab public user repositories
api_url = f"https://api.github.com/users/{github_username}/repos"

#send get request
response = requests.get(api_url)

#get the data in json or equivalent dict format
data =  response.json()

for repository in data:
##for key, value in data.items():
    ##table.add_row([key, value])
    table.add_row([repository["name"], repository["created_at"]])

print(table)
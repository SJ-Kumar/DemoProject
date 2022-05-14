from typing import Container
import requests
import html
#from browser import document, html 
#container = document['container']

input = 'Cheyyar'

#def getweather(event):
 #   if event.key == 'Enter':

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": input}

headers = {
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
	"X-RapidAPI-Key": "d0553e1541msh143a6ab1560e91ep17832cjsn99f8fe81fd86"
}

response = requests.request("GET", url, headers=headers, params=querystring)


#container <= input


print(response.text)

import requests
from bs4 import BeautifulSoup
import csv
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)

print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# find all the anchor tags with "href"
##for link in soup.find_all('a'):
  ##  print(link.get('href'))



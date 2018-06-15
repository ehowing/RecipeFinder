import requests
import urllib
import json

appId = "9f58709e"
key = "9eeb6b82d09c485293c9a9e1b0dce5d2"
query = "chicken"

URL = 'https://api.edamam.com/search?q=' + query + '&app_id=' + appId + '&app_key=' + key + '&from=0&to=3&cal=500'
r = requests.get(url=URL)

response = urllib.request.urlopen(URL)
str_response = response.read().decode('utf-8')
obj = json.loads(str_response)
print(obj)

#parse json 

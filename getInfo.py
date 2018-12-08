import json
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=fr&'
       'apiKey=d552b7c31a6448c0aaeffa576506564a')
response = requests.get(url)
#print response.json()['articles'][1]['content']

#print len(response.json())


for acti in  response.json()['articles']:
	print (acti['content'])


#parsed_json = json.loads(response.json())

#print  (parsed_json['articles'][0])

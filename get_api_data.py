import requests
import json

# set urls
table_url = "https://football-web-pages1.p.rapidapi.com/league-table.json"
form_url = "https://football-web-pages1.p.rapidapi.com/form-guide.json"
fixtures_url = "https://football-web-pages1.p.rapidapi.com/fixtures-results.json"

#set key path
path = "/Users/andrew/premierleaguepredictor/.secret/api_football.json"
#load api keys
with open(path) as f:
	keys = json.load(f)
api_key = keys['api_key']
#set other api variables
querystring = {"comp":"1","team":"1","round":"1"}
headers = {'x-rapidapi-key': api_key, 'x-rapidapi-host': "football-web-pages1.p.rapidapi.com"} 
r = ""
r2 = ""
r3 = ""
	
def make_requests():
	# make GET requests
	global r, r2, r3, querystring
	r = requests.request("GET", table_url, headers=headers, params=querystring)
	r2 = requests.request("GET", form_url, headers=headers, params=querystring)
	querystring = {"comp":"1","team":"1","round":"1"}
	r3 = requests.request("GET", fixtures_url, headers=headers, params=querystring)
	

def store_responses():
	""" store responses in json file """
	file = 'league_table.json'
	with open(file, 'w') as f:
		json.dump(r.json(), f, indent=4,)

	file = 'form_guide.json'
	with open(file, 'w') as f:
		json.dump(r2.json(), f, indent=4,)

	file = 'fixtures_data.json'
	with open(file, 'w') as f:
		json.dump(r3.json(), f, indent=4,)

def fetch_data():
	make_requests()
	store_responses()

if __name__ == '__main__':
	fetch_data()

import requests
import json

#load api keys
def get_keys(path):
    with open(path) as f:
        return json.load(f)

keys = get_keys("/Users/andrew/premierleaguepredictor/.secret/api_football.json")
api_key = keys['api_key']

# load urls
table_url = "https://football-web-pages1.p.rapidapi.com/league-table.json"
form_url = "https://football-web-pages1.p.rapidapi.com/form-guide.json"
fixtures_url = "https://football-web-pages1.p.rapidapi.com/fixtures-results.json"
querystring = {"comp":"1","team":"1"}
headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "football-web-pages1.p.rapidapi.com"
    }
# make get requests
r = requests.request("GET", table_url, headers=headers, params=querystring)
r2 = requests.request("GET", form_url, headers=headers, params=querystring)
querystring = {"comp":"1","team":"1","round":"1"}
r3 = requests.request("GET", fixtures_url, headers=headers, params=querystring)

# get predictions
predictions_url = "https://api-football-v1.p.rapidapi.com/v2/predictions/157462"
headers = {
    'x-rapidapi-key': "ec77ba6a5fmsh79e0926558f3a80p19b4aejsn907505bcb806",
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }
r4 = requests.request("GET", predictions_url, headers=headers)

#store responses
file = 'league_table.json'
with open(file, 'w') as f:
	json.dump(r.json(), f, indent=4,)

file = 'form_guide.json'
with open(file, 'w') as f:
	json.dump(r2.json(), f, indent=4,)

file = 'fixtures_data.json'
with open(file, 'w') as f:
	json.dump(r3.json(), f, indent=4,)

file = 'predictions_data.json'
with open(file, 'w') as f:
	json.dump(r4.json(), f, indent=4,)
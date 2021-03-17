import get_api_data
import json
from datetime import datetime, timedelta

#retrieve league table response data
file = 'data/league_table.json'
with open(file, 'r') as f:
  league_data = json.load(f)

# export league teams data to new file
teams_data = league_data['league-table']['teams']
file = 'data/teams_data.json'
with open(file, 'w') as f:
  json.dump(teams_data, f) 

#retrieve form response data
file = 'data/form_guide.json'
with open(file, 'r') as f:
  form_data = json.load(f)

# export teams form data to new file
teams_form_data = form_data['form-guide']['teams']
file = 'data/teams_form_data.json'
with open(file, 'w') as f:
  json.dump(teams_form_data, f)

#retrieve fixtures response data
file = 'data/fixtures_data.json'
with open(file, 'r') as f:
  fixtures_data = json.load(f)

# export fixtures data to new file
team_fixtures_data = fixtures_data['fixtures-results']['matches']
file = 'data/teams_fixtures_data.json'
with open(file, 'w') as f:
  json.dump(team_fixtures_data, f)

# filter for next fixtures
next_fixtures = []
for match in team_fixtures_data:
	match['date'] = datetime.strptime(match['date'], "%Y-%m-%d")
for match in team_fixtures_data:
	if match['date'] > datetime.today() and match['date'] < datetime.today() + timedelta(days=7):
		next_fixtures.append(match)
for match in next_fixtures:
	match['date'] = match['date'].strftime("%Y-%m-%d")



# file = 'data/remaining_fixtures_data.json'
# with open(file, 'w') as f:
#   json.dump(remaining_fixtures, f)

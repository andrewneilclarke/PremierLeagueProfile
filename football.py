import get_api_data
import json

#retrieve league table response data
file = 'league_table.json'
with open(file, 'r') as f:
  league_data = json.load(f)

# export league teams data to new file
teams_data = league_data['league-table']['teams']
file = 'teams_data.json'
with open(file, 'w') as f:
  json.dump(teams_data, f) 

#retrieve form response data
file = 'form_guide.json'
with open(file, 'r') as f:
  form_data = json.load(f)

# export teams form data to new file
teams_form_data = form_data['form-guide']['teams']
file = 'teams_form_data.json'
with open(file, 'w') as f:
  json.dump(teams_form_data, f)

#retrieve fixtures response data
file = 'fixtures_data.json'
with open(file, 'r') as f:
  fixtures_data = json.load(f)

# export fixtures data to new file
team_fixtures_data = fixtures_data['fixtures-results']['team']
file = 'teams_fixtures_data.json'
with open(file, 'w') as f:
  json.dump(team_fixtures_data, f)
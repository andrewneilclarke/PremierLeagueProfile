import get_api_data as api
import json

#retrieve file data
file = 'league_table.json'
with open(file, 'r') as f:
  league_data = json.load(f)

# export teams data (first level)
teams_data = league_data['league-table']['teams']
file = 'teams_data.json'
with open(file, 'w') as f:
  json.dump(teams_data, f)

file = 'form_guide.json'
with open(file, 'r') as f:
  form_data = json.load(f)

teams_form_data = form_data['form-guide']['teams']
file = 'teams_form_data.json'
with open(file, 'w') as f:
  json.dump(teams_data, f)

file = 'fixtures_data.json'
with open(file, 'r') as f:
  fixtures_data = json.load(f)
teams_fixtures_data = fixtures_data['fixtures-results']['team']

file = 'predictions_data.json'
with open(file, 'r') as f:
  predictions_data = json.load(f)
predictions = predictions_data['api']['predictions']

# create team class
class Team:
    def __init__(self, position, total_points, name):
        self.name = name
        self.total_points = total_points
        self.position = position
        self.played = teams_data[self.position -1]['all-matches']['played']
        self.won = teams_data[self.position -1]['all-matches']['won']
        self.drawn = teams_data[self.position -1]['all-matches']['drawn']
        self.lost = teams_data[self.position -1]['all-matches']['lost']
        self.gf = teams_data[self.position -1]['all-matches']['for']
        self.ga = teams_data[self.position -1]['all-matches']['against']
        self.gd = teams_data[self.position -1]['all-matches']['goal-difference']
        self.homeplayed = teams_data[self.position -1]['home-matches']['played']
        self.homewon = teams_data[self.position -1]['home-matches']['won']
        self.homedrawn = teams_data[self.position -1]['home-matches']['drawn']
        self.homelost = teams_data[self.position -1]['home-matches']['lost']
        self.homefor = teams_data[self.position -1]['home-matches']['for']
        self.awayagainst = teams_data[self.position -1]['away-matches']['against']
        self.awayplayed = teams_data[self.position -1]['away-matches']['played']
        self.awaywon = teams_data[self.position -1]['away-matches']['won']
        self.awaydrawn = teams_data[self.position -1]['away-matches']['drawn']
        self.awaylost = teams_data[self.position -1]['away-matches']['lost']
        self.awayfor = teams_data[self.position -1]['away-matches']['for']
        self.awayagainst = teams_data[self.position -1]['away-matches']['against']
        self.form = teams_form_data[self.position -1]['points'] / teams_form_data[self.position -1]['played']       

    def get_descriptive_name(self):
        """Return a neatly formatted team description """
        return f"This team is {self.name}. They are in position {self.position} in the table with {self.total_points} points. "

    @property
    def position_rating(self):
        return 20 - self.position + 1
    
    @property
    #marks out of 20
    def form_rating(self):
        return round(self.form * 8)
    
    @property
    #marks out of 10
    def goal_threat_rating(self):
        return (self.gf / self.played) * 5

    @property
    #marks out of 10
    def defence_rating(self):
        return 10 - (self.ga / self.played) * 4

    @property
    def home_rating(self):
        return ((self.homewon) * 3) + (self.homedrawn) / (self.homeplayed) * 6

    @property
    def away_rating(self):
        return round((self.awaywon) * 3) + (self.awaydrawn)  / (self.awayplayed) * 6
    @property
    def home_team(self):
        return str(int(round((self.position_rating + self.form_rating + self.goal_threat_rating + self.defence_rating + self.home_rating), -1)/10))
    @property
    def away_team(self):
        return str(int(round(self.position_rating + self.form_rating + self.goal_threat_rating + self.defence_rating + self.away_rating, -1)/10))

#create team instances
teams = [] 
for team in teams_data:
    team = Team(team['position'], team['total-points'], team['name'])
    teams.append(team)

# function to print table
def print_table():
    print('Team Name   P  W  D  L  F  A  GD  FORM')
    for team in teams:
        print(team.name, team.played, team.won, team.drawn, team.lost, team.gf, 
                team.ga, team.gd, team.form_rating, team.home_team)

# for team in teams:
#   print(team.name + team.home_team())

#print_table()
print(predictions[0]['advice'])

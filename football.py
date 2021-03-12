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

    def get_descriptive_name(self):
        """Return a neatly formatted team description """
        return f"This team is {self.name}. They are in position {self.position} in the table with {self.total_points} points. "

    @property
    def position_rating(self):
        return 20 - self.position + 1
    """
    @property
    #marks out of 20
    def form_rating(self):
        return round(self.pointsinlastten * 0.666666)
    """
    @property
    #marks out of 10
    def goal_threat_rating(self):
        return (self.gf / self.played) * 5

    @property
    #marks out of 10
    def defence_rating(self):
        return 10 - (self.ga / self.played) * 4
    """
    @property
    def home_rating(self):
        return (self.hpoints / self.hgamesp) * 6

    @property
    def away_rating(self):
        return (self.apoints / self.agamesp) * 6
    """
    def calculate_home_team(self):
        return str(int(round((self.position_rating + self.form_rating + self.goal_threat_rating + self.defence_rating + self.home_rating), -1)/10))

    def calculate_away_team(self):
        return str(int(round(self.position_rating + self.form_rating + self.goal_threat_rating + self.defence_rating + self.away_rating, -1)/10))
          

#create team instances
teams = [] 
for team in teams_data:
    team = Team(team['position'], team['total-points'], team['name'])
    teams.append(team)

# #print table
# for team in teams:
#     print(team.name, team.played, team.won, team.drawn, team.lost, team.ga, team.gf, team.gd)

for team in teams:
    print(team.defence_rating)

# print('Burnley: ' + Burnley.calculate_home_team())
# print('Arsenal: ' + Arsenal.calculate_away_team() + '\n')
# print('SheffU: ' + SheffU.calculate_home_team())
# print('Southampton: ' + Southampton.calculate_away_team() + '\n')
# print('AstonV: ' + AstonV.calculate_home_team())
# print('Wolves: ' + Wolves.calculate_away_team() + '\n')
# print('Brighton: ' + Brighton.calculate_home_team())
# print('Leicester: ' + Leicester.calculate_away_team() + '\n')
# print('WestBrom: ' + WestBrom.calculate_home_team())
# print('Newcastle: ' + Newcastle.calculate_away_team() + '\n')
# print('Liverpool: ' + Liverpool.calculate_home_team())
# print('Fulham: ' + Fulham.calculate_away_team() + '\n')
# print('Manure: ' + Manure.calculate_home_team())
# print('ManchesterCity: ' + ManchesterCity.calculate_away_team() + '\n')
# print('Spurs: ' + Spurs.calculate_home_team())
# print('CPalace: ' + CPalace.calculate_away_team() + '\n')
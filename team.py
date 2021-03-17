import football as f

# create team class
class Team:
    def __init__(self, position, total_points, name):
        self.name = name
        self.total_points = total_points
        self.position = position
        self.played = f.teams_data[self.position -1]['all-matches']['played']
        self.won = f.teams_data[self.position -1]['all-matches']['won']
        self.drawn = f.teams_data[self.position -1]['all-matches']['drawn']
        self.lost = f.teams_data[self.position -1]['all-matches']['lost']
        self.gf = f.teams_data[self.position -1]['all-matches']['for']
        self.ga = f.teams_data[self.position -1]['all-matches']['against']
        self.gd = f.teams_data[self.position -1]['all-matches']['goal-difference']
        self.homeplayed = f.teams_data[self.position -1]['home-matches']['played']
        self.homewon = f.teams_data[self.position -1]['home-matches']['won']
        self.homedrawn = f.teams_data[self.position -1]['home-matches']['drawn']
        self.homelost = f.teams_data[self.position -1]['home-matches']['lost']
        self.homefor = f.teams_data[self.position -1]['home-matches']['for']
        self.awayagainst = f.teams_data[self.position -1]['away-matches']['against']
        self.awayplayed = f.teams_data[self.position -1]['away-matches']['played']
        self.awaywon = f.teams_data[self.position -1]['away-matches']['won']
        self.awaydrawn = f.teams_data[self.position -1]['away-matches']['drawn']
        self.awaylost = f.teams_data[self.position -1]['away-matches']['lost']
        self.awayfor = f.teams_data[self.position -1]['away-matches']['for']
        self.awayagainst = f.teams_data[self.position -1]['away-matches']['against']
        self.form = f.teams_form_data[self.position -1]['points'] / f.teams_form_data[self.position -1]['played']       

    def profile(self):
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
for team in f.teams_data:
    team = Team(team['position'], team['total-points'], team['name'])
    teams.append(team)

# function to print table
def print_table():
    print('Team Name   P  W  D  L  F  A  GD  FORM')
    for team in teams:
        print(team.name, team.played, team.won, team.drawn, team.lost, team.gf, 
                team.ga, team.gd, team.form_rating, team.home_team)
def print_home_table():
    for team in teams:
        print(team.name + " " + team.home_team)

def print_away_table():
    for team in teams:
        print(team.name + " " + team.away_team)

def print_form_table():
    for team in teams:
        print(team.name + " " + (str(team.form_rating)))
        
def next_fixtures():
    #print fixtures (next 7 days)
    for fixture in f.next_fixtures:
        print(fixture['home-team']['name'] + " v " + fixture['away-team']['name'])

next_fixtures()
#print_remaining_fixtures()


#     print(fixture['home-team']['score'])
#print(f.remaining_fixtures[0]['home-team']['score'])
#print(f.remaining_fixtures[0:10])
# #rint_form_table()
# print_table()
# print_away_table()
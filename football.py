import get_api_data as api
import pandas as pd

class Team:
  def __init__(self, id, position, total_points, name):
    self.id = id
    self.position = position
    self.total_points = total_points
    self.name = name


  def get_descriptive_name(self):
    """Return a neatly formatted team description """
    return f"This team is {self.name}. ID is {self.id}. They are in position {self.position} in the table with {self.total_points} points. "
  
  def add_attr(lost, against, gd, won, gf, drawn, played):
    self.lost = lost
    self.against = against
    self.gd = gd
    self.won = won
    self.gf = gf
    self.drawn = drawn
    self.played = played

  @property
  def position_rating(self):
      return 20 - self.position + 1
  
  @property
  #marks out of 20
  def form_rating(self):
      return round(self.pointsinlastten * 0.666666)
  @property
  #marks out of 10
  def goal_threat_rating(self):
      return (self.goalsf / self.gamesp) * 5

  @property
  #marks out of 10
  def defence_rating(self):
      return 10 - (self.goalsa / self.gamesp) * 4
  
  @property
  def home_rating(self):
      return (self.hpoints / self.hgamesp) * 6

  @property
  def away_rating(self):
      return (self.apoints / self.agamesp) * 6

  def calculate_home_team(self):
      return str(int(round((self.position_rating + self.form_rating + self.goal_threat_rating + self.defence_rating + self.home_rating), -1)/10))

  def calculate_away_team(self):
      return str(int(round(self.position_rating + self.form_rating + self.goal_threat_rating + self.defence_rating + self.away_rating, -1)/10))

"""
print('Burnley: ' + Burnley.calculate_home_team())
print('Arsenal: ' + Arsenal.calculate_away_team() + '\n')
print('SheffU: ' + SheffU.calculate_home_team())
print('Southampton: ' + Southampton.calculate_away_team() + '\n')
print('AstonV: ' + AstonV.calculate_home_team())
print('Wolves: ' + Wolves.calculate_away_team() + '\n')
print('Brighton: ' + Brighton.calculate_home_team())
print('Leicester: ' + Leicester.calculate_away_team() + '\n')
print('WestBrom: ' + WestBrom.calculate_home_team())
print('Newcastle: ' + Newcastle.calculate_away_team() + '\n')
print('Liverpool: ' + Liverpool.calculate_home_team())
print('Fulham: ' + Fulham.calculate_away_team() + '\n')
print('Manure: ' + Manure.calculate_home_team())
print('ManchesterCity: ' + ManchesterCity.calculate_away_team() + '\n')
print('Spurs: ' + Spurs.calculate_home_team())
print('CPalace: ' + CPalace.calculate_away_team() + '\n')

"""






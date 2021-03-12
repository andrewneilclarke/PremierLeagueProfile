

#for team in teams:
#	print(team.get_descriptive_name())
"""
played = []
for team in teams_data:
	team['played'] = played
	print(played)



#print(league_data["league-table"]["teams"])
#print(league_data["league-table"]["teams"][0]["all-matches"]["won"])
#file = 'form_guide.json'
#with open(file, 'w') as f:
#	json.dump(r2.json(), f, indent=4,)


#pandas_df = pd.json_normalize(all_teams_data)
#print(pandas_df)

#readable_file = 'readable_data.json'
#with open('readable_file', 'w') as f:
#	json.dump(all_league_data, f, indent=4)


#names = []

#print(teams_dict[0]['all-matches']['for'])


loses = []
wins = []
draws = []




#all_lost = all_league_data["teams"]["all-matches"]

#print(len(all_lost))

for league_data in all_league_data:
	lost = all_league_data["league-table"]["teams"]
	losts.append(lost)

#print("Status code:", r.status_code)
# Check keys of response
#print(r.json().keys())
# Check keys at next level of response
print(r.json()['league-table'].keys())
#print(r.json()['league-table']['competition'])
#print(r.json()['league-table']['description'])
#print(r.json()['league-table']['teams'])
#print(r.json()['league-table']['teams'].keys())
# Create dictionary of results for 'teams' key
teams_dict = r.json()['league-table']['teams']
#desc_dict = r.json()['league-table']['description']
# Visualize df for all English Premier league seasons available
teams_df = pd.DataFrame.from_dict(teams_dict)
print(teams_df['name'])
#desc_df = pd.DataFrame.from_dict(desc_dict)

#print(desc_df)

"""
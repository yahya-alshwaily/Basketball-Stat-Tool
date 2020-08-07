import constants
import copy
import sys

teams_main = copy.deepcopy(constants.TEAMS)
players_main = copy.deepcopy(constants.PLAYERS)

panthers = teams_main [0] = []
bandits = teams_main [1] = []
warriors = teams_main [2] = []

"""
The app file imports the set of data from "constants" and are copied to prevent mutation of the original imported data
The list of teams is further assigned lists for each element, demarking the names of the teams
"""

def clean_data_and_balance_teams():

	"""
	This function takes the data from the constants file and clean them for the application of this file, which is to clean
	it to the desired values and used to allocate the players data to the teams list.

	the data being cleaned is:
	1) the heights from strings with "inches" attached to each height value to an int value
	2) the player's expereince is cleaned from the string "yes" and "no" to boolean values of True and False
	3) seperate the guardians strings into individual strings for each guardian and store them in a list inside the player's dict data

	the data is then allocated to each team:
	1) each team gets an equally experienced list of players sequentially
	"""
	# Experience counters to limit how many experienced and inexperienced players are allocated to each team
	panthers_xp = 0
	panthers_inxp = 0
	bandits_xp = 0
	bandits_inxp = 0
	warriors_xp = 0
	warriors_inxp = 0
	
	# cleaning begins
	for element in players_main:
			
		element['height'] = int(element['height'][0:2])
		
		if element['experience'] == 'NO':
			element['experience'] = False
			
		elif element['experience'] == 'YES':							  
			element['experience'] = True
			
		element['guardians'] = element['guardians'].split(' and ')
	
	for element in players_main:
		element['guardians'] = ', '.join(element['guardians'])
	# cleaning ends

	for player in players_main:
			
		if player['experience'] == False and panthers_inxp < 3:
			panthers.append(player)
			panthers_inxp += 1
		elif player['experience'] == True and panthers_xp < 3:
			panthers.append(player)
			panthers_xp += 1
		elif player['experience'] == False and bandits_inxp < 3:
			bandits.append(player)
			bandits_inxp += 1
		elif player['experience'] == True and bandits_xp < 3:
			bandits.append(player)
			bandits_xp += 1
		elif player['experience'] == False and warriors_inxp < 3:
			warriors.append(player)
			warriors_inxp += 1
		elif player['experience'] == True and warriors_xp < 3:
			warriors.append(player)
			warriors_xp += 1


def get_choice():
	
	"""
	This function display the menu options for the user, the input values are guarded against user erroneous 
	inputs by accepting inputs as strings and using these strings to compare with the available choices
	"""

	print("""
BASKETBALL TEAM STATS TOOL
---- MENU----
Here are your choices:
 1) Display Team Stats
 2) Quit
  """)
	
	menu_choice = input("Enter an option > ")
	while menu_choice != "1" and menu_choice != "2":
		menu_choice = input("Please Enter an option from the choices > ")
		
		
	if menu_choice == "2":
		sys.exit()
	
	elif menu_choice == "1":
		print("""
1) Panthers
2) Bandits
3) Warriors
	""")
	
	team_choice = input("Enter an option > ")
	while team_choice != "1" and team_choice != "2" and team_choice != "3":
		team_choice = input("Please Enter an option from the choices > ")
		
	return int(team_choice)


def get_team(team_choice):
	"""
	This function takes the choice inputed from the user and displays the team's data in a user friendly manner,
	Other jobs this function does is:
	1) calculate and display the average heights of the player's teams
	2) Extrapolate the team's experience in a list and display the number of experienced and inexperienced players
	3) Extrapolate the team's player names and store it in a list for it to be diplayed
	4) Extrapolate the team's guardians and store it in a list for it to be diplayed
	"""
	team_heights = []
	for element in teams_main[team_choice - 1]:
		team_heights.append(element['height'])
	
	team_avg_height = sum(team_heights)/len(teams_main[team_choice - 1])
	
	team_names = ['Panthers', 'Bandits', 'Warriors']
	
	team_name = f"\nTeam: {team_names[team_choice-1]} Stats\n"
	
	print(team_name+ "-" * len(team_name))
	
	print(f"Total Players: {len(teams_main[team_choice - 1])}")
	
	experienced_placeholder = []
	for element in teams_main[team_choice - 1]:
		experienced_placeholder.append(element['experience'])
		
	inexperienced_placeholder = len(teams_main[team_choice - 1]) - sum(experienced_placeholder)
	
	print(f"Total experienced: {sum(experienced_placeholder)}")
	print(f"Total inexperienced: {inexperienced_placeholder}")
	print(f"Average height: {team_avg_height:.2f}")
	
	store_names = []
	for element in teams_main [team_choice - 1]:
		store_names.append(element['name'])
	
	print("\nPlayers on Team:\n"," ", ", ".join(store_names))
	
	store_guardians = []
	for element in teams_main [team_choice - 1]:
		store_guardians.append(element['guardians'])

	print("\nGuardians:\n"," ", ", ".join(store_guardians))	

if __name__ == "__main__":
	clean_data_and_balance_teams()
	
	ENTER = ''
	while ENTER == '':
		get_team(get_choice())
		ENTER = input("\nPress ENTER to continue...")
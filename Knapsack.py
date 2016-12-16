import csv
import nba
 

class Player():
	def __init__(self,playerID, points, salary, position, value):
		self.self = self
		self.playerID = playerID
		self.points = points
		self.salary = salary
		self.position = position
		self.value = value

	def __iter__(self):
		return iter(self.list)
	
	def __str__(self):
		return "{} {} {} {}".format(self.playerID, self.points, self.salary, self.position)
	
preds_dict = nba.generate_random_pred(20)
players = []
for i in range(20):
	playerID = preds_dict['playerID'][i]
	points = preds_dict['points'][i]
	salary = preds_dict['salary'][i]
	position = preds_dict['position'][i]
	value = points/salary
	player = Player(playerID,points,salary,position,value)
	players.append(player)


def knapsack(players):
	budget = 60000
	used_cap_space = 0


	players.sort(key = lambda x: x.value, reverse = True)
	team = []

	for player in players:
		if used_cap_space + player.salary < budget and len(team) < 9:
			team.append(player)
			used_cap_space = used_cap_space + player.salary
			continue

	players.sort(key = lambda x: x.points, reverse = True)
	for player in players:
		if player not in team:
			for i in range(8):
				if(used_cap_space + player.salary - team[i].salary < budget and player.points > team[i].points):
					used_cap_space = used_cap_space + player.salary - team[i].salary
					team[i] = player
					break

	return team

team = knapsack(players)
points = 0
salary = 0
for player in team:
	points = points + player.points
	salary = salary + player.salary
	print player

print "\nPoints: {}".format(points)
print "Salary: {}". format(salary)






		


import urllib2
from bs4 import BeautifulSoup
import csv
import re

filename = 'stuffer.html'
html_report_part1 = open(filename,'r')
soup = BeautifulSoup( html_report_part1, "html.parser")

td_num = 1
all_players = []

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

#406 is number of nba players and 25 is the number of other divs that we dont care about

for i in range(406):
	if (soup.find('tbody').find_all('td')[td_num] is not None):
		str_html = str(soup.find('tbody').find_all('td')[td_num])
		player_div = cleanhtml(str_html)
		#print player_div
		all_players.append(player_div)
		td_num += 25
		i += 1
resultFile = open('players.csv', 'wb')
wr = csv.writer(resultFile)

for player in all_players:
	wr.writerow([player,])

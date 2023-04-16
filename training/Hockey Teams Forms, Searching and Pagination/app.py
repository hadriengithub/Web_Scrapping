import requests
from bs4 import BeautifulSoup

class HockeyTeam:
	"Classe qui modélise toutes les données récupérable sur une équipe de hockey"
	team_name = 'default_team_name'
	year = 0
	wins = 0
	losses = 0
	win_rating = 0.0
	goals_for = 0
	goals_against = 0
	goals_rating = 0

def create_new_soup(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')
	return soup

def scrap_this_soup(soup, hockey_team_list):
	team_tab = soup.find_all('tr', {'class' : 'team'})
	for team_row in team_tab:
		name = team_row.find('td', {'class' : 'name'})
		year = team_row.find('td', {'class' : 'year'})
		wins = team_row.find('td', {'class' : 'wins'})
		losses = team_row.find('td', {'class' : 'losses'})
		win_rating = team_row.find('td', {'class' : 'pct text-danger'})
		goals_for = team_row.find('td', {'class' : 'gf'})
		goals_against = team_row.find('td', {'class' : 'ga'})
		goals_rating = team_row.find('td', {'class' : 'diff text-success'})
		team = HockeyTeam()
		team.name = name.text.strip()
		team.year = year
		team.wins = wins
		team.losses = losses
		team.win_rating = win_rating
		team.goals_for = goals_for
		team.goals_against = goals_against
		team.goals_rating = goals_rating
		hockey_team_list.append(team)
		# print('Added team : ', team.name)
	return hockey_team_list

def sort_by_name(hockey_team_list):
	new_hockey_team_list = []
	

# formation de la requête et creation de la soup
url = 'https://www.scrapethissite.com'
r = requests.get(url + '/pages/forms/')
soup = BeautifulSoup(r.text, 'html.parser')

# recupération d'une liste de liens a scrap entiérement
# selection du html content contenant les liens
ul = soup.find('ul', {'class' : 'pagination'})
a = ul.find_all('a')
# formation de la liste de liens brute
link_list = []
for l in a:
	link = url + l['href']
	link_list.append(link)
# supression de tous les liens doublons dans la liste de liens
prossesed_list = []
for link in link_list:
	if link not in prossesed_list:
		prossesed_list.append(link)
	else:
		print('remove : ', link)
link_list = prossesed_list
# affichage de la liste de liens propre
for link in link_list:
	print(link)

# scrap data from the first page
hockey_team_list = []

for link in link_list:
	new_soup = create_new_soup(link)
	print('scrapping in progress, url=',link)
	hockey_team_list = scrap_this_soup(new_soup, hockey_team_list)

print(len(hockey_team_list))
print('name of the 52th team : ', hockey_team_list[51].name)
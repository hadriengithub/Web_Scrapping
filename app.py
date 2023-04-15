# Le but de ce projet et de récupérer tout les pays de la page de scrapping et de les classé

# importation des bibliothèques de code (requests, BeautifulSoup)
import requests
from bs4 import BeautifulSoup

# code principale
url = "https://www.scrapethissite.com/pages/simple/" # cible du scrapping

# requête centrale
r = requests.get(url)

# création de l'objet soup
soup = BeautifulSoup(r.text, "html.parser")

# création de la classe pays
class Country:
	"Classe représentant les différent pays"
	name = "default_country_name"
	capital = "default_capital"
	population = 0
	area = 0.0

def sort_by_name(countries_data):
	list_of_countries_name = []
	for country in countries_data:
		list_of_countries_name.append(country.name)
		sorted_list_of_countries_name = sorted(list_of_countries_name)
		print(sorted_list_of_countries_name)

def sort_by_population(countries_data):
	sorted_list_of_countries_by_population = countries_data
	sorted_list_of_countries_by_population.sort(key = lambda x : x.population, reverse=True)
	for country_sorted in sorted_list_of_countries_by_population:
		print("population : ", country_sorted.population, " (", country_sorted.name,")")

def sort_by_area(countries_data):
	sorted_list_of_countries_by_area = countries_data
	sorted_list_of_countries_by_area.sort(key = lambda x : x.area, reverse=True)
	for country_sorted in sorted_list_of_countries_by_area:
		print("population : ", country_sorted.area, " (", country_sorted.name,")")

countries_data = []

countries = soup.find_all("div", {"class": "col-md-4 country"})

for country in countries:
	c = Country()

	name = country.find("h3", {"class": "country-name"})
	capital = country.find("span", {"class": "country-capital"})
	population = country.find("span", {"class": "country-population"})
	area = country.find("span", {"class": "country-area"})
	
	c.name = name.text
	c.capital = capital.text
	c.population = int(population.text)
	c.area = float(area.text)

	countries_data.append(c)

sort_by_area(countries_data)

# print("Longueur de la liste : ", len(countries_data))

# print("nom du pays : ", countries_data[0].name)
# print("capitale du pays : ", countries_data[0].capital)
# print("population du pays : ",countries_data[0].population)
# print("superficie du pays : ", countries_data[0].area)

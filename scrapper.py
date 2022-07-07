# -*- coding: utf-8 -*-

"""
pokemon-stats-scrapper

Scrap all base stats of all pokemon of each generation with Beautifulsoup webscrapping
"""

import requests
from bs4 import BeautifulSoup
import re

# Retrieve All Pokemon Names By Generation Id
def getPokemonIds():
    pokemonIds=[]
    for i in range(1, 9):
        url = "https://pokeapi.co/api/v2/generation/" + str(i) + "/"
        r = requests.get(url)
        data = r.json()
        for i in data['pokemon_species']:
            url = i['url']
            pat = r'/pokemon-species/(\d+)/'       
            match = re.search(pat, url)
            pokemonIds.append(match.group(1))
            
    return pokemonIds

pokemonIds = getPokemonIds()
BASE_STATS = []

for current_id in pokemonIds:
    url = "https://pokeapi.co/api/v2/pokemon/" + current_id
    r = requests.get(url)
    data = r.json()
    obj = {
            'hp': data['stats'][0]['base_stat'],
            'atk': data['stats'][1]['base_stat'],
            'def': data['stats'][2]['base_stat'],
            'satk': data['stats'][3]['base_stat'],
            'sdef': data['stats'][4]['base_stat'],
            'spd': data['stats'][5]['base_stat']
        }
    string = str('\'' + data['species']['name'] + '\': ' ) + str(obj) + ','

    BASE_STATS.append(obj)
    print(string)
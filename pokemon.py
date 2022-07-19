import requests
import json
import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="abuser"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

response_API = requests.get('https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')

keys = response_API.json()['count']
lst = []
for i in range(keys):
    b = response_API.json()['results'][i]
    lst.append(b['url'])


for i in lst:
    data = requests.get(i)
    b = data.json()
    
    cnt_abl = 0
    for i in b['abilities']:
        cnt_abl += 1

    for i in range(cnt_abl):
        nama = b['name']
        abilities = b['abilities'][i]['ability']['name']
        spesies = b['species']['name']
        weight = b['weight']
        height = b['height']
        cur.execute(
            "INSERT INTO abuser.pokemon (nama, abilities, species, weight, height) VALUES (?, ?, ?, ?, ?)", (nama, abilities, spesies, weight, height))


conn.commit() 
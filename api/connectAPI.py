# kết nối và giao tiếp API

import requests

base_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
query = input("enter drink to search: ")

request = requests.get(f'{base_url}{query}')
result = request.json()['drinks']
instructions = result[0]['strInstructions']

print(f'Instructions: {instructions}')
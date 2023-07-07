# kết nối và giao tiếp API

import requests

base_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s="
query = input("enter drink to search: ")

request = requests.get(f'{base_url}{query}')
result = request.json()['drinks']
instructions = result[0]['strInstructions']

print(f'Instructions: {instructions}')

# craft the request

url = "https://reddit.com/"

c = {
    'test_cookies':'say something random'
}
h = {
    'User-agent':'Googlebot' #Mozilla/5.0
}
response = requests.get(
    url,
    cookies=c,
    headers=h
)

code = response.status_code

print(code)

if code==200:
    print("Successfully!")
    
#maniputation header

print(response.text)
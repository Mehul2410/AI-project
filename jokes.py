import requests
url ='https://v2.jokeapi.dev/joke/Any?type=single'
json_data = requests.get(url).json()

joke = json_data['joke']


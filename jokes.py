import requests
url ='https://v2.jokeapi.dev/joke/Any?type=single'
json_data = requests.get(url).json()

import threading

def joke():
  threading.Timer(60.0, joke).start()
  json_data = requests.get(url).json()
  return json_data['joke']





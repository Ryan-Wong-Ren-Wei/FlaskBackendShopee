import requests
import json

BASE = "http://127.0.0.1:5000/"
# BASE = "https://flaskshopeebackend.herokuapp.com"
# id = 1

# response = requests.put(BASE + "wishlist/9", {'item_id' : 12, 'post' : "hi how are you" })
# print(response.message)
response = requests.get(BASE + "/wishlist/2")
print(response)
print(response.json())
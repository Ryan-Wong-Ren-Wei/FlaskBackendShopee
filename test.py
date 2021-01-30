import requests
import json

# BASE = "http://127.0.0.1:5000/"
BASE = "https://flaskshopeebackend.herokuapp.com"
id = 1

# response = requests.put(BASE + "customer/2", {"name" : "Kek", "email":"kek@hello.sg"})
# print(response.message)
response = requests.get(BASE + "/customer/5")
print(response)
print(response.message)
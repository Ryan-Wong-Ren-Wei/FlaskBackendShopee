import requests
import json

BASE = "http://127.0.0.1:5000/"
id = 2

# response = requests.put(BASE + "customer/2", {"name" : "Kek", "email":"kek@hello.sg"})
# print(response.message)
response = requests.get(BASE + "customer/2")
print(response.message)
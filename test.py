import requests

BASE = "http://127.0.0.1:5000/"
TENBIS = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"

response = requests.get(TENBIS)
print(response.json())

response2 = requests.get(TENBIS + "drinks/")
print(response2.json())

id_5 = 0
id_6 = 0
order1 = {"drinks": [id_5, id_6],
          "desserts": [id_5, id_6],
          "pizzas": [2055830, 2055831]}
response3 = requests.post(BASE + "tenbis/order", order1)
print(response3.json())


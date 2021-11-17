# from flask import Flask, request
# from flask_restful import Api, Resource
# import requests
# # from data import *
#
# app = Flask(__name__)
# api = Api(app)
#
# # @app.route('/home')
#
# def home():
#     return "hello, welcome to our website";
#
# TENBIS = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
# dishes = {"pizzaA": {"id": 3, "desc": "tasty", "price": 45},
#          "pizzaB": {"id": 4, "desc": "well", "price": 60}}
#
# class TenBis(Resource):
#     def get(self, dish_id):
#         self.getit(dish_id)
#         response = requests.get(TENBIS)
#         print(response)
#         return dishes
#
#     def post(self, order: dict):
#         request.method
#         print(request.form["pizzas"])
#         return {"data": "posten"}
#
#     def getit(self, dish_id):
#         print(dish_id)
#
#
# api.add_resource(TenBis, "/drinks/<int:dish_id>")
# # api.add_resource(TenBis, "/tenbis/<dict:order>")
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#

from flask import Flask, request
from flask_restful import Api, Resource
import requests
from flask import Flask

app = Flask(__name__)

TENBIS = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"


@app.route('/<type>')
def home(type):
    response = requests.get(TENBIS)
    result = get_by_type((response.json()), type)
    return result

def get_by_type(data: dict, type):
    tmp = data["Data"]
    for category in tmp["categoriesList"]:
        if (category["categoryName"].lower() == type):
            print(category["dishList"])
            return dict([ (category["dishList"]["dishId"], category["dishList"]) for dish in category["dishList"] ])

    return "Not Found"

if __name__ == "__main__":
    app.run(debug=True)
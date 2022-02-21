from flask import Flask, request
from flask_restful import Api, Resource
import requests


app = Flask(__name__)
api = Api(app)


TENBIS = "https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup"
dishes = {"pizzaA": {"id": 3, "desc": "tasty", "price": 45},
         "pizzaB": {"id": 4, "desc": "well", "price": 60}}

class TenBis(Resource):
    def get(self, dish_id):
        response = requests.get(TENBIS)
        return dishes

    def post(self, order: dict):
        request.method
        print(request.form["pizzas"])
        return {"data": "posten"}


api.add_resource(TenBis, "/drinks/<int:dish_id>")
# api.add_resource(TenBis, "/tenbis/<dict:order>")



@app.route('/<name>')
def home(name):
    response = requests.get(TENBIS)
    result = get_by_type((response.json()), name)
    return result

def get_by_name(data: dict, name):
    tmp = data["Data"]
    for category in tmp["categoriesList"]:
        if (category["categoryName"].lower() == name):
            print(category["dishList"])
#             return dict([ (category["dishList"]["dishId"], category["dishList"]) for dish in category["dishList"] ]) #unfinished
    return "Not Found"

if __name__ == "__main__":
    app.run(debug=True)

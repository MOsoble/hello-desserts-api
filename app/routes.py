from flask import Blueprint, jsonify

class Dessert:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

desserts_list = [

Dessert(1,"Red Velvet Cake", "A type of chocolate cake"),
Dessert(2,'Brownies','littler cakes'),
Dessert(3,'Ice cream','Gelato with a different name')

]

desserts_bp = Blueprint('desserts',__name__, url_prefix="/desserts")

@desserts_bp.route("", methods=["GET"])
def handle_desserts():
    desserts_response=[]
    for dessert in desserts_list:
        desserts_response.append(
            {"id": dessert.id,
            "name": dessert.name,
            "description":dessert.description
        }
        )
    return jsonify(desserts_response)

@desserts_bp.route("/<dessert_id>", methods=["GET"])
def handle_dessert(dessert_id):
    dessert_id=int(dessert_id)

    for dessert in desserts_list:
        if dessert.id==dessert_id:
            return{
            "id": dessert.id,
            "name": dessert.name,
            "description":dessert.description
            }
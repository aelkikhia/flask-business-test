from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from section6.src.models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")
    parser.add_argument("store_id",
                        type=int,
                        required=True,
                        help="Item needs store id.")

    @jwt_required()
    def get(self, name):
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': 'an error occurred'}, 500

        if item:
            return item.json(), 200
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {
                       "message": f"An item with name '{name}' already exists."
                   }, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except:
            return {'message': 'an error occurred inserting the item'}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()

        return {'message': f'item {name} deleted'}

    def put(self, name):
        data = Item.parser.parse_args()  # data = request.get_json()
        try:
            item = ItemModel.find_by_name(name)
        except:
            return {'message': 'an error occurred'}, 500

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']


        try:
            item.save_to_db()
        except:
            return {'message': 'an error occurred updating item'}, 500

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all())


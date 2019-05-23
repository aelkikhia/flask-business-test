from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from section6.src.resources.store import Store, StoreList
from section6.src.security import authenticate, identity
from section6.src.resources.user import UserRegister
from section6.src.resources.item import Item, ItemList


app = Flask(__name__)

# point at db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# turns of flask_sqlalchemy tracker not sqlalchemy's

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'taz'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, "/register")


if __name__ == '__main__':
    from section6.src.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

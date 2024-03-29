from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.store import Store, StoreList
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.Accounts import AccountList


app = Flask(__name__)

# point at db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# turns of flask_sqlalchemy tracker not sqlalchemy's

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'taz'
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(AccountList, "/accounts")

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

api.add_resource(UserRegister, "/register")


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

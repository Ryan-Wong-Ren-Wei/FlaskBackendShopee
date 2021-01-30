from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers
from database_init import WishlistModel, FriendsModel

app  = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Wishlist(Resource):
    def get(self, user_id):
        result = WishlistModel.query.filter_by(user_id = user_id).first()
        print(result)
        if not result:
            abort(404, message = "Customer id does not yet exist")
        return result

class Friends(Resource):
    def get(self, user_id):
        result = FriendsModel.query.filter_by(user_id = user_id).first()
        print(result)
        if not result:
            abort(404, message = "Customer id does not yet exist")
        return result

    # def put(self, user_id):
    #     result = FriendsModel.query.filter_by(user_id = user_id).first()


@app.route("/")
def home():
    return "a buttplug"
    
def getApp():
    return app
    
api.add_resource(Friends, "/friends/<int:user_id>")
api.add_resource(Wishlist, "/wishlist/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
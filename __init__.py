from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers
from database_init import WishlistModel, FriendsModel

app  = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# db.create_all()

# Resource fields for wishlist database model
wishlist_resource_fields = {
    'user_id': fields.Integer,
    'item_id': fields.Integer,
    'post': fields.String
}
class Wishlist(Resource):
    @marshal_with(wishlist_resource_fields)
    def get(self, user_id):
        result = WishlistModel.query.filter_by(user_id = user_id).first()
        print(result)
        if not result:
            abort(404, message = "Customer id does not yet exist")

        return result

    @marshal_with(wishlist_resource_fields)
    def put(self, user_id):

        for i in range(0,5):
            wishlist = WishlistModel(user_id = i, item_id = , post = "hello")
            db.session.add(wishlist)
            db.session.commit()
        


# Resource fields for friends database model
friends_resource_fields = {
    'user_id': fields.Integer,
    'friends_id': fields.String
}
class Friends(Resource):
    def get(self, user_id):
        result = FriendsModel.query.filter_by(user_id = user_id).first()
        print(result)
        if not result:
            abort(404, message = "Customer id does not yet exist")
        return result

@app.route("/")
def home():
    return "a buttplug"
    
def getApp():
    return app
    
api.add_resource(Friends, "/friends/<int:user_id>")
api.add_resource(Wishlist, "/wishlist/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers

app  = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class WishlistModel(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    item_id = db.Column(db.String, nullable = False)
    post = db.Column(db.String, nullable = False)

class FriendsModel(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    friend_id = db.Column(db.String, nullable = False)

db.create_all()

# api.add_resource(, "/customer/<int:customer_id>")

if __name__ == "__main__":
    app.run(debug=True)
# RUNNING THIS WILL DELETE ALL DATA IN DATABASE

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers
import sys

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

if __name__ == "__main__":
    yn = input("Warning: This will delete all database entries and create new db file. type y to continue and n to exit ->")

    if yn != "y":
        print("exiting")
        sys.exit()
    db.create_all()
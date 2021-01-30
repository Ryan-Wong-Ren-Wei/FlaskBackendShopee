from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers

app  = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Customer(Resource):
    def get(self, customer_id):
        result = CustomerModel.query.filter_by(id = customer_id).first()
        print(result)
        if not result:
            abort(404, message = "Customer id does not yet exist")
        return result
    
def getApp():
    return app
    
api.add_resource(Customer, "/customer/<int:customer_id>")
# api.add_resource(Wishlist)

if __name__ == "__init__":
    app.run(debug=True)
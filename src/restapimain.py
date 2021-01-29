from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from reqparsers import initializeParsers

app  = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class CustomerModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    # wishlist = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = False)

    # def __init__(self, id, name, email):
    #     self.id = id
    #     self.name = name
    #     self.email = email

    def __repr__(self):
        return f"Customer(name = {self.name}), email = {self.email}"

# db.create_all()

putreqparser, updatereqparser = initializeParsers()

customer_resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    # 'wishlist': fields.String,
    'email': fields.String
}



class Customer(Resource):
    @marshal_with(customer_resource_fields)
    def get(self, customer_id):
        result = CustomerModel.query.filter_by(id = customer_id).first()
        print(result)
        if not result:
            abort(404, message = "Customer id does not yet exist")
        return result
    
    @marshal_with(customer_resource_fields)
    def put(self, customer_id: int):
        args = putreqparser.parse_args()
        # result = CustomerModel.query.filter_by(id=customer_id).first()
        # if result:
        #     abort(409, message = 'Customer already in database')
        
        customer = CustomerModel(id = customer_id, name = args['name'], email = args['email'])
        print(customer.id)
        print(customer)
        db.session.add(customer)
        db.session.commit()
        # print(customer)
        return (customer_id, args)

    @marshal_with(customer_resource_fields)
    def patch(self, customer_id):
        return

    def delete(self, customer_id):
        return
    
api.add_resource(Customer, "/customer/<int:customer_id>")

if __name__ == "__main__":
    app.run(debug=True)
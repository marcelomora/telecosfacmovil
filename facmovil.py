# -*- encoding: utf-8 -*-
from flask import Flask, request
from flask_restful import Resource, Api
from models import lexus, couch_model

app = Flask(__name__)
api = Api(app)
customers = {}

class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'World'}

class Customer(Resource):
    def get(self, fin):
        couch_manager_obj = couch_model.couchdb_manager()
        return couch_manager_obj.get_customer_by_fin(fin)

    def put(self, fin):
        customers[fin] = request.form['name']
        return {fin: customers[fin]}

api.add_resource(HelloWorld, '/')
api.add_resource(Customer, '/<string:fin>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

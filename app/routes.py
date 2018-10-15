from flask import Flask, redirect,jsonify,make_response, request
from flask_restful import Resource, Api
# create flask app
app = Flask(__name__)
api=Api(app)

if __name__ == '__main__':
    app.run(debug=True)

items=[]


class Cart(Resource):
    def get(self):
        return make_response(jsonify([{'items':items,
    'status':'ok'
    }]),200)

    def post(self):
        data=request.get_json()
        product={'name':data['name'],'amount':data['amount'],'quantity':data['quantity']}
        items.append(product)
        return make_response(jsonify({'items':items}),201)


api.add_resource(Cart,'/cart')

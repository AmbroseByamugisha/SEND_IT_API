from flask import Flask, jsonify, request 
from models import Parcel_Delivery_Order, User

app = Flask(__name__)

parcel_delivery_orders = []

@app.route('/')
def hello():
    return jsonify({'message' : 'Hello world'})

@app.route('/api/v1/parcels', methods=['GET'])
def get_all_parcel_delivery_orders():
    output = []
    for parcel_delivery_order in parcel_delivery_orders:
        parcel_data = {}
        parcel_data['order_id'] = parcel_delivery_order.order_id
        parcel_data['public_id'] = parcel_delivery_order.public_id
        parcel_data['contents'] = parcel_delivery_order.contents
        parcel_data['destination'] = parcel_delivery_order.destination
        parcel_data['location'] = parcel_delivery_order.location
        parcel_data['status'] = parcel_delivery_order.status
        parcel_data['price'] = parcel_delivery_order.price
        output.append(parcel_data)

    return jsonify ({'parcel_delivery_orders': output}) 
@app.route('/api/v1/parcels', methods=['POST'])
def create_parcel_delivery_order():
    data = request.get_json()

    try:
        print(data)
        if type(data['price']) is not int:
            raise ValueError('Price should be integer')
        new_parcel_delivery_order = Parcel_Delivery_Order(data["order_id"], \
            data["public_id"], data["contents"], data["destination"], \
            data["location"], data["status"], data["price"])
        parcel_delivery_orders.append(new_parcel_delivery_order)
    except ValueError as e:
        print(e)
        return jsonify({'message': 'Price should be integer'}), 400
    return jsonify({'message': ' the parcel_delivery_order has been created'}), 201

if __name__ == '__main__':
    app.run(debug=True)

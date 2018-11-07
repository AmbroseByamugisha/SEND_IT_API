from flask import Flask, jsonify 
from models import Parcel_Delivery_Order, Users

app = Flask(__name__)

@app.route('/')
def hello():
	return jsonify({'message' : 'Hello world'})

@app.route('api/v1/parcels', methods=['POST'])
def create_parcel_delivery_order():
    data = request.get_json()

    try:
        print(data)
        if type(data['price']) is not int:
            raise ValueError('Price should be integer')
        new_parcel_delivery_order = Parcel_Delivery_Order(data['order_id'], /
        	data['public_id'], data['contents'], data['destination'], /
        	data['location'], data['status'], data['price'])
        parcel_delivery_orders.append(new_parcel_delivery_order)
    except ValueError as e:
        print(e)
        return jsonify({'message': 'Price should be integer'}), 400
    return jsonify({'parcel_delivery_orders': [new_parcel_delivery_order.to_json()]}), 201

if __name__ == '__main__':
	app.run(debug=True)

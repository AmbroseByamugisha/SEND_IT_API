class User:


	def __init__(self, user_id, public_id, username, password, admin):
		self.user_id = user_id
		self.public_id = public_id
		self.username = username
		self.password = password
		self.admin = admin

	def to_json(self):
        return {'user_id': self.user_id, 'public_id': self.public_id, \
        'username': self.username, 'password': self.password, \
        'admin': self.admin}


class Parcel_Delivery_Order:

	def __init__(self, order_id, public_id, contents, destination, location, status, price):
		self.order_id = order_id
		self.public_id = public_id
		self.contents = contents
		self.destination = destination
		self.location = location
		self.status = status
		self.price = price

	def to_json(self):
        return {'order_id': self.order_id, 'public_id': self.public_id, \
        'destination': self.destination, 'location': self.location, \
        'status': self.status, 'price': self.price}



from flask import Flask
from flask_restful import Api, Resource, reqparse

app= Flask(__name__, static_folder="client", static_url_path='')
api = Api(app)

# Data
users = [
	{
	"name":"John",
	"age": 25,
	"occupation":"Developer"
	},
	{
    "name":"Aron",
    "age": 36,
    "occupation":"Test Engineer"
    }
]

# Resources
class User(Resource):
	def get(self,name):
		for user in users:
			if(name==user["name"]):
				return user, 200
		return "User not found", 404

	def post(self,name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()

		for user in users:
			if(name == user["name"]):
				return "User with name {} already exists".format(name), 400
		user = {
			"name": name,
			"age": args["age"],
			"occupation": args["occupation"]
		}
		users.append(user)
		return user, 201

	def put(self, name):
		parser = reqparse.RequestParser()
		parser.add_argument("age")
		parser.add_argument("occupation")
		args = parser.parse_args()

		for user in users:
			if(name == user["name"]):
				user["age"] = args["age"]
				user["occupation"] = args["occupation"]
				return user, 200
        
			user = {
				"name": name,
				"age": args["age"],
				"occupation": args["occupation"]
			}
		users.append(user)
		return user, 201

	def delete(self, name):
		global users
		users = [user for user in users if user["name"] != name]
		return "{} is deleted.".format(name), 200

# Endpoints
api.add_resource(User, "/user/<string:name>") # Resource 'User' is the class name
#app.run(debug=True) # this is moved to wsgi.py

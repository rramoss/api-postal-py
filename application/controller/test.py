from flask import request
from flask_restful import Resource

class testClass(Resource):

	def get(self):
		return {"hello":'world'}
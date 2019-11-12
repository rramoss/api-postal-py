from flask import request
from flask_restful import Resource
from app import mysql
import json

class postalClass(Resource):

	def get(self, cp):
		cur = mysql.get_db().cursor()
		#query insert record
		cur.execute("INSERT INTO records (url, cp, host) VALUES ('/postal',%s,%s)",(cp,request.remote_addr) )
		# query consult código postal
		query=cur.execute("SELECT cp,colonia,municipio,estado,ciudad FROM `location_postal` WHERE cp=%s ",(cp))
		cur.connection.commit()
		if query>0:
			#result=cur.fetchone()
			#col_names = [i[0] for i in cur.description]
			col_names = cur.fetchone()
			col_colonias = [i[1] for i in cur]
			res={"status": "success","data": {"cp":col_names[0],"colonia": col_colonias,"municipio":col_names[2],"estado":col_names[3],"ciudad":col_names[4]}, "error": ""}
			return res
		else:
			return {"status": "error","data": "", "error": "No se encontraron coincidencias"}
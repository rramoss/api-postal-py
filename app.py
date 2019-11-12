#Import library
from flask import Flask
from flask_restful import Api
from flaskext.mysql import MySQL
from dotenv import load_dotenv
import os

#name app flask app
app = Flask(__name__)
api = Api(app)
#cache flask
app.config["CACHE_TYPE"] = "null"

#env dot load data
#load_dotenv()

#mysql config
app.config['MYSQL_DATABASE_HOST'] = os.getenv('mysql_host')
app.config['MYSQL_DATABASE_USER'] = os.getenv('mysql_user')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('mysql_pass')
app.config['MYSQL_DATABASE_DB'] = os.getenv('mysql_base')
mysql = MySQL(app)

#import Controller
from app.controller.postal import postalClass

#Rest services
api.add_resource(postalClass,'/postal/<int:cp>')


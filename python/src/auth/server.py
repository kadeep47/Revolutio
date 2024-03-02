import jwt #jason web token to login logout 
import datetime # expire on the token 
import os 
from flask import Flask,request
from flask_mysqldb import MySQL


server = Flask(__name__)
myql = MySQL(server)

server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST") #resolve to local host that we have set 
print(server.config["MYSQL_HOST"])


server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

@server.route("/login",methods =  ["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing cred"
    auth.user 
    auth.password






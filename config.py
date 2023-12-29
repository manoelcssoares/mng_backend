from app import app
from flask import Flask, request
from MySQLdb

app = Flask(__name__)


MYSQL_USER = 'mng_user'
MYSQL_PASSWORD = '2)KA=P2ir4'
MYSQL_DB = 'mng_db'
MYSQL_HOST = 'localhost'

def connect_to_mysql():
    return MySQLdb.connect(host=MYSQL_HOST,
                           user=MYSQL_USER,
                           passwd=MYSQL_PASSWORD,
                           db=MYSQL_DB)
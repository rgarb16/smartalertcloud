"""This module is to configure app to connect with database."""

from pymongo import MongoClient
import urllib

DATABASE = MongoClient()['sensordb'] # DB_NAME
DEBUG = True
uri = "mongodb://sensor_user1:"+urllib.quote("user@123")+"@127.0.0.1/sensordb"
client = MongoClient(uri)

"""This module is to configure app to connect with database."""

from pymongo import MongoClient
import urllib

DATABASE = MongoClient()['sensordb'] # DB_NAME
DEBUG = True
uri = "mongodb://XXXX:"+urllib.quote("XXXX")+"@127.0.0.1/sensordb"
client = MongoClient(uri)

"""This module will serve the api request."""

from config import client
from app import app
from bson.json_util import dumps
from flask import request, jsonify
import json
import ast
import imp
import calendar
import datetime
from bson.objectid import ObjectId
"""
 04/24/2019 
   - Added functionality to generate report
"""

# Import the helpers module
helper_module = imp.load_source('*', './app/helpers.py')

# Select the database
db = client.sensordb
# Select the collection
collection = db.sensor

@app.route("/")
def get_initial_response():
    # Message to the user
    message = {
        'apiVersion': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Sensor Data API'
    }
    # Making the message looks good
    resp = jsonify(message)
    return resp


@app.route("/api/v1/sensor", methods=['POST'])
def create_sensor():
    """
       Function to Add sensor data 
       """
    try:
        # Add sensor 
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as request body is not available
            # Add message for debugging purpose
            return "", 400

        record_created = collection.insert(body)

        # Prepare the response
        if isinstance(record_created, list):
            # Return list of Id of the newly created item
            return jsonify([str(v) for v in record_created]), 201
        else:
            # Return Id of the newly created item
            return jsonify(str(record_created)), 201
    except:
        return "", 500


@app.route("/api/v1/sensor", methods=['GET'])
def get_sensor_data():
    """
       Function to get sensors data.
       """
    try:
        # Call the function to get the query params
        query_params = helper_module.parse_query_params(request.query_string)
        # Check if dictionary is not empty
        if query_params:

            # Try to convert the value to int
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

            records_fetched = collection.find(query)

            # Check if the records are found
            if records_fetched.count() > 0:
                # Prepare the response
                return dumps(records_fetched)
            else:
                # No records are found
                return "", 404

        # If dictionary is empty
        else:
            if collection.find().count > 0:
                # Prepare response if sensor data is found
                return dumps(collection.find())
            else:
                # Return empty array if no sensor data are found
                return jsonify([])
    except:
        return "", 500

#Generate reports
@app.route("/api/v1/sensor/report/<int:hours>", methods=['GET'])
def get_report_data(hours):
    try:
      if collection.find().count > 0:
          gen_time = datetime.datetime.today() - datetime.timedelta(hours=hours) 
          records = ObjectId.from_datetime(gen_time)
          result = list(db.coll.find({"_id": {"$gte": records}}))

          return dumps(collection.find({"_id": {"$gte": records}}))
      else:
          return jsonify([])
    except Exception as e:
        print e.message, e.args
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500


@app.errorhandler(404)
def page_not_found(e):
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

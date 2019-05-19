# smartcity

curl -X POST   http://mysensor-db-906737534.us-east-2.elb.amazonaws.com/api/v1/sensor   -H 'Content-Type: application/json'   -d '{
    "sensor_id": 81,
    "recorded_time": "03:21:02.381230",
    "recorded_date": "2019-04-24”
    "battery_health": "ok",
    "sensor_type": "humidity",
    "humidity_range": 11,
    "humidity_alarm_state": "warning",
    "geo_tag_location": 95014
}'

curl  -k https://mysensor-db-906737534.us-east-2.elb.amazonaws.com/api/v1/sensor?sensor_type=humidity 
curl  -k https://mysensor-db-906737534.us-east-2.elb.amazonaws.com/api/v1/sensor?sensor_type=smoke
curl  -k https://mysensor-db-906737534.us-b.amazonaws.com/api/v1/sensor | jq .

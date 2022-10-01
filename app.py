from flask import Flask
import dbhelper
import json

app = Flask(__name__)

@app.get('/cars')
def get_cars():
    results = dbhelper.run_statment('CALL show_all_cars()')
    if(type(results) == list):
        cars_json = json.dumps(results, default=str)
        return cars_json
    else:
        return 'sorry'

app.run(debug=True)
from datetime import date

import flask
from flask import render_template
from flask import request, jsonify
from werkzeug.exceptions import abort
from DAL.DBTemp import DBTemp
from Entities.Temperature import Temperature

dbtemp = DBTemp()

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/temperatures', methods=['GET'])
def get():
    temperatures = dbtemp.select_all_temperatures()
    return jsonify(temperatures)


@app.route('/temperatures/<int:tempId>', methods=['GET'])
def get_one(tempId):
    temp = dbtemp.select_temperature(tempId)
    return jsonify(temp)


@app.route('/temperatures/new', methods=['POST'])
def create():

    temp = request.json.get("temp")
    humidity = request.json.get("humidity")
    datetime = request.json.get("datetime")
    temperature = Temperature(datetime, temp, humidity)
    last_row_id = dbtemp.insert_temperature(temperature)
    return get_one(last_row_id)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('template_404.html'), 404


app.run()

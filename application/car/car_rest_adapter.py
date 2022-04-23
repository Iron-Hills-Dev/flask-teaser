import logging
import uuid

from flask import request

from app import app, ports
from application.car.car_add_request import CarAddRequest
from application.car.car_id_response import CarIdResponse
from application.car.car_response import CarResponse
from domain.car.car_modify_port import CarModifyPort
from domain.car.car_query_port import CarQueryPort
from domain.car.model.car_add_command import CarAddCommand

car_query_port: CarQueryPort = ports.car_query_port
car_modify_port: CarModifyPort = ports.car_modify_port


@app.route("/car", methods=["POST"])
def add_car():
    logging.info(f'Processing add car request: {request}, body={request.get_json()}')
    body = CarAddRequest(request.get_json())
    car_id = car_modify_port.add_car(CarAddCommand(body.model, body.regNum))
    return CarIdResponse(car_id).to_json(), 200


@app.route("/car/<car_id>", methods=["DELETE"])
def del_car(_car_id: str):
    logging.info(f'Processing delete car request: {request}, id={_car_id}')
    car_modify_port.delete_car(uuid.UUID(_car_id))
    return '', 204


@app.route("/car/<car_id>", methods=["GET"])
def find_car(_car_id: str):
    logging.info(f'Processing find car request: {request}, id={_car_id}')
    car = car_query_port.find_car(uuid.UUID(_car_id))
    return CarResponse(car).to_json(), 200

import logging
import os
import time
from logging.handlers import RotatingFileHandler
from threading import Thread

import requests
from flask import Flask, request
from flask_socketio import SocketIO
from requests import session

import Constants


# Socket-io server example
# https://github.com/miguelgrinberg/Flask-SocketIO/blob/v2.2/example/app.py
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



@app.route("/")
def index():
    socketio.emit('my response',
                  {'data': 'Server generated event', 'count': 4},
                  namespace='/test',
                  broadcast = True)
    return 'Hello World'

# @app.route("/iphone")
# def iphone():
#     session['name'] = 'iphone'
#     return index()
#
# @app.route("/dash")
# def dashboard():
#     session['name'] = 'dash'
#     return index()
#
# @app.route("/send")
# def send_msg():
#     socketio.emit('message','HELLO WORLDDDD', namespace='/test',broadcast= True)
#     return 'yo'

@app.before_first_request
def initialSetup():
    #TODO Implement Logging
    # if Constants.ENABLE_FLASK_LOGGING:
    #     formatter = logging.Formatter(
    #         Constants.LOG_FORMAT_FLASK)
    #     handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_FLASK, Constants.LOG_FILENAME_FLASK),
    #                                   maxBytes=10000000, backupCount=5)
    #     handler.setLevel(logging.DEBUG)
    #     handler.setFormatter(formatter)
    #     app.logger.addHandler(handler)

    import Bonjour
    service = Bonjour.Bonjour()
    service.publish()

    #TODO Serial Read(Arduino Communication)
    #SERIAL SERVICE
    # from Serial_Listener import Serial_Worker
    # global Serial_Worker
    # Serial_Worker = Serial_Worker()


@socketio.on('connect', namespace= Constants.SOCKETIO_NAMESPACE)
def test_connect():
    print('Client connected : ', request.sid)
    return True

@socketio.on('disconnect', namespace= Constants.SOCKETIO_NAMESPACE)
def test_disconnect():
    print('Client disconnected : ', request.sid)
    return True
@socketio.on('message', namespace= Constants.SOCKETIO_NAMESPACE)
def handle_message(data):
    # TODO Pass the message to the ios message parser
    pass

def send_to_ios(data):
    socketio.send('message',data,namespace=Constants.SOCKETIO_NAMESPACE)
def receive_from_arduino(data):
    # TODO Pass the message to Arduino Message Parser
    pass
@socketio.on('do_task', namespace= Constants.SOCKETIO_NAMESPACE)
def handle_message(message):
    """
    :param message : A string message containing function to call, and values if required
    Sent from iphone
    """

    message = SENDER_Arduino.message_to_send(message)
    Serial_Worker.send(message)
    emit('my response', {'data': 'SUCCESS'})


if __name__ == '__main__':
    socketio.run(app,
                 debug=Constants.ENABLE_FLASK_DEBUG_MODE,
                 host=Constants.SERVER_IP,
                 port=Constants.SERVER_PORT,
                 use_reloader=False)

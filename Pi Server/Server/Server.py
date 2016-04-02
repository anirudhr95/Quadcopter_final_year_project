import logging
import os
import time
from logging.handlers import RotatingFileHandler
from threading import Thread

import requests
from flask import Flask, request
from flask_socketio import emit, SocketIO, join_room, leave_room
from requests import session

import Constants

class global_vars:
    Serial_Worker = None
    SENDER_Iphone = None
    SENDER_Arduino = None
    socketio = None


# Socket-io server example
# https://github.com/miguelgrinberg/Flask-SocketIO/blob/v2.2/example/app.py
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
global_vars.socketio = SocketIO(app)



@app.route("/")
def index():
    global_vars.socketio.emit('my response',
                  {'data': 'Server generated event', 'count': 4},
                  namespace='/test',
                  broadcast = True)
    return 'Hello World'

@app.route("/iphone")
def iphone():
    session['name'] = 'iphone'
    return index()

@app.route("/dash")
def dashboard():
    session['name'] = 'dash'
    return index()

@app.route("/send")
def send_msg():
    emit('message','HELLO WORLDDDD', namespace='/test',broadcast= True)
    return 'yo'

@app.before_first_request
def initialSetup():
    if Constants.ENABLE_FLASK_LOGGING:
        formatter = logging.Formatter(
            Constants.LOG_FORMAT_FLASK)
        handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_FLASK, Constants.LOG_FILENAME_FLASK),
                                      maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)




    import Bonjour
    service = Bonjour.Bonjour()
    service.publish()

    #SERIAL SERVICE
    from Serial_Listener import Serial_Worker
    global Serial_Worker
    global_vars.Serial_Worker = Serial_Worker()

    # MIDDLEWARE MESSAGE PASSERS
    from middleware import middleware
    global SENDER_Arduino, SENDER_Iphone
    global_vars.SENDER_Iphone = middleware(1)
    global_vars.SENDER_Arduino = middleware(2)


@global_vars.socketio.on('connect', namespace='/test')
def test_connect():
    print('Client connected : ', request.sid)
    return True

@global_vars.socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected : ', request.sid)
    return True


@global_vars.socketio.on('do_task', namespace='/test')
def handle_message(message):
    """
    :param message : A string message containing function to call, and values if required
    Sent from iphone
    """

    message = SENDER_Arduino.message_to_send(message)
    Serial_Worker.send(message)
    emit('my response', {'data': 'SUCCESS'})


if __name__ == '__main__':
    global_vars.socketio.run(app,
                 debug=Constants.ENABLE_FLASK_DEBUG_MODE,
                 host=Constants.SERVER_IP,
                 port=Constants.SERVER_PORT)

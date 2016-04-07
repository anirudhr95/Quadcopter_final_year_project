import logging
from logging.handlers import RotatingFileHandler
import os

from Quad_Controls import Quadcopter

async_mode = None

if async_mode is None:
    try:
        import eventlet

        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey

            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet

    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey

    monkey.patch_all()

import threading

from threading import Thread

import serial
from flask import Flask, request
from flask_socketio import SocketIO
from pi_send import pi_send_toArduino
import Constants

# Socket-io server example
# https://github.com/miguelgrinberg/Flask-SocketIO/blob/v2.2/example/app.py
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)
serial_port = None
quadcopter = None
e = None
middleware_ios = None
middleware_arduino = None

ard_msg_converter = pi_send_toArduino()
class messages:
    message_queue = []

    def append(self, msg):
        messages.message_queue.append(msg)
        e.set()


def read_from_port(event=None, serial_port=None):
    """

    :param event: Thread.Event to call upon reading data froms serial (Used by IOSSenderThread)
    :param serial_port: serial.Serial() variable specifying serial port of arduino decice
    """
    serial_port = serial.Serial('/dev/cu.usbmodem1411', 9600)
    print "SERIAL WORKER THREAD STARTED with event %s" % event
    while True:
        reading = serial_port.readline().decode("Utf-8").rstrip()
        print "READING FROM SERIAL : ", reading
        event.set()
        middleware_arduino.parseMessage(reading)


def speed_control():
    """

    """
    global quadcopter

    import time
    print "PID CONTROL THREAD STARTED"
    while True:
        speeds = quadcopter.refresh()
        msg = ard_msg_converter.set_speeds(speeds)
        send_to_arduino(msg)
        time.sleep(Constants.REFRESH_PID_TIME)


@app.route("/")
def index():
    socketio.emit('my response',
                  {'data': 'Server generated event', 'count': 4},
                  namespace='/test',
                  broadcast=True)
    return 'Hello World'


@app.before_first_request
def initialSetup():
    global quadcopter, middleware_arduino, middleware_ios
    from middleware import Middleware_IOS, Middleware_Arduino
    quadcopter = Quadcopter()

    middleware_arduino = Middleware_Arduino(quadcopter, messages)
    middleware_ios = Middleware_IOS(quadcopter)

    # TODO Implement Logging
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

    # Create Thread event for notifying threads about serial read success op (Used by ios_senderthread to send to ios)
    global e
    e = threading.Event()

    # SERIAL SERVICE
    # from Serial_Comm import read_from_port


    global serial_port
    try:
        serial_port = serial.Serial(Constants.ARDUINO_PORT, Constants.ARDUINO_BAUDRATE, timeout=0)
        # except serial.SerialException():
        #     print("FAILED TO CONNECT TO SERIAL PORT : %s"%msg)
        thread = threading.Thread(name="Serial Thread",
                                  target=read_from_port,
                                  kwargs={'event': e,
                                          'serial_port': serial_port}
                                  )
        thread.daemon = True
        thread.start()
    except serial.SerialException as e:
        print "COULD NOT START SERIAL : \n",e

    # IOS SENDER THREAD
    thread2 = Thread(name="IOS Sender Thread",
                     target=ios_sender_thread,
                     kwargs={'event': e})
    thread2.daemon = True
    thread2.start()

    # PID THREAD
    try:
        thread3 = Thread(name="PID Thread",
                         target=speed_control)
        thread3.daemon = True
        thread3.start()
    except Exception as e:
        print e
    messages.append("Ready")
    print 'Sent'

    # TEST USING A BACKGROUND THREAD
    # thread3 = Thread(target=background_thread)
    # thread3.daemon = True
    # thread3.start()


def ios_sender_thread(event=None):
    print 'IOS SENDER THREAD STARTED with event %s' % event
    while True:
        event_is_set = event.wait()
        print "EVENT RECEIVED AT IOS SENDER THREAD"
        for val in messages.message_queue:
            send_to_ios(val)
        event.clear()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    import time
    while True:
        time.sleep(10)
        count += 1
        socketio.emit('my response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@socketio.on('connect', namespace=Constants.SOCKETIO_NAMESPACE)
def test_connect():
    print('Client connected : ', request.sid)
    return True


@socketio.on('disconnect', namespace=Constants.SOCKETIO_NAMESPACE)
def test_disconnect():
    print('Client disconnected : ', request.sid)
    return True


@socketio.on('message', namespace=Constants.SOCKETIO_NAMESPACE)
def handle_message(data):
    # TODO Pass the message to the ios message parser
    print 'Received Message : %s'%data
    middleware_ios.parseMessage(data)


def send_to_ios(data):
    print 'SENDING %s To IOS ' % str(data)
    socketio.emit('message', data, namespace=Constants.SOCKETIO_NAMESPACE)


def send_to_arduino(data):
    print "SENDING '%s' TO ARDUINO" % data
    global serial_port
    serial_port.write(data)


def receive_from_arduino(data):
    # TODO Pass the message to Arduino Message Parser
    send_to_ios(data)
    # send_to_arduino(data)


if __name__ == '__main__':
    socketio.run(app,
                 debug=Constants.ENABLE_FLASK_DEBUG_MODE,
                 host=Constants.SERVER_IP,
                 port=Constants.SERVER_PORT,
                 use_reloader=False)

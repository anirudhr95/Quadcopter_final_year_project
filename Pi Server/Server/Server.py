import multiprocessing

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

import logging
import os
from logging.handlers import RotatingFileHandler
from Quadcopter import Quadcopter

import serial
from flask import Flask, request, render_template
from flask_socketio import SocketIO
import Constants

# Socket-io server example
# https://github.com/miguelgrinberg/Flask-SocketIO/blob/v2.2/example/app.py
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)
serial_port = None
quadcopter = None
middleware_ios = None
middleware_arduino = None
message_sender = None
queue = None


def read_from_port(port, baud_rate, queue):
    """

    :param event: Thread.Event to call upon reading data froms serial (Used by IOSSenderThread)
    :param serial_port: serial.Serial() variable specifying serial port of arduino decice
    """
    serial_port = serial.Serial(port, baud_rate, queue)
    print "SERIAL WORKER THREAD STARTED with object (%s)" % serial_port
    while True:
        reading = serial_port.readline().decode("Utf-8").rstrip()
        if reading:
            try:
                queue.put(reading)
            except:
                while not queue.empty():
                    queue.get()


def speed_control(queue, quadcopter, message_sender, middleware_arduino):
    """
        Requires middleware_arduino, quadcopter, message_sender params
    """
    print "PID CONTROL THREAD STARTED : Waiting for first reading"
    import time

    # Wait for Serial Setup to complete (Marked by "SETUP COMPLETED:" MESSAGE)

    reading = queue.get()
    while not middleware_arduino.parseMessage(reading):
        # parseMessage returns true, when setup is completed
        reading = queue.get()
        middleware_arduino.parseMessage(reading)
    # TODO BROADCAST Ready message
    print "SETUP COMPLETED"

    speeds, oldspeeds = [0, 0, 0, 0], [0, 0, 0, 0]
    while True:
        # CHECK MESSAGE QUEUE FOR ARDUINO INPUTS
        if queue.empty():
            # TODO: This means that no data is being received from arduino, which means quad needs to go into hover mode/land, because of some serial error
            quadcopter.land()
        while not queue.empty():
            reading = queue.get_nowait()
            middleware_arduino.parseMessage(reading)

        oldspeeds = speeds[:]
        speeds = quadcopter.refresh()
        if oldspeeds != speeds:
            message_sender.toArduino_set_speed(speeds)
        time.sleep(Constants.REFRESH_PID_TIME)


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        if 'quad_setSpeed' in request.form:
            quadcopter.set_speed(int(request.form["quad_setSpeed_text"]))
        elif 'set_ypr' in request.form:
            print request.form
            ypr = [0.0, 0.0, 0.0]
            if request.form['set_ypr_y'] != '':
                ypr[0] = float(request.form['set_ypr_y'])
            if request.form['set_ypr_p'] != '':
                ypr[1] = float(request.form['set_ypr_p'])
            if request.form['set_ypr_r'] != '':
                ypr[2] = float(request.form['set_ypr_r'])
            quadcopter.set_YPR_Desired(ypr)

        elif 'takeoff' in request.form:
            quadcopter.takeoff()
        elif 'land' in request.form:
            quadcopter.land()
        elif 'hover' in request.form:
            quadcopter.set_Mode_Hover_Enable()
        elif 'hold_altitude' in request.form:
            quadcopter.set_Mode_Altitude_Hold_Enable()
        elif 'reset_baro' in request.form:
            message_sender.toArduino_reset_baro()
        elif 'change_pid' in request.form:
            p, i, d = 0.0, 0.0, 0.0
            if request.form['set_kp'] != '':
                p = float(request.form['set_kp'])
            if request.form['set_ki'] != '':
                i = float(request.form['set_ki'])
            if request.form['set_kd'] != '':
                d = float(request.form['set_kd'])
            quadcopter.__set_PID_Test__(p, i, d)
    return render_template("index.html")


@app.before_first_request
def initialSetup():
    global quadcopter, middleware_arduino, middleware_ios, message_sender
    from middleware import Middleware_IOS, Middleware_Arduino

    from CustomLogger import PILogger
    quadcopter = Quadcopter(PILogger())

    from message_sender import Message_sender
    message_sender = Message_sender(socketio, serial_port)

    middleware_arduino = Middleware_Arduino(quadcopter)
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

    # SERIAL SERVICE
    # from Serial_Comm import read_from_port

    global queue
    queue = multiprocessing.Queue()

    if Constants.ENABLE_SERIAL:
        global serial_port
        serial_port = serial.Serial(Constants.ARDUINO_PORT, Constants.ARDUINO_BAUDRATE, timeout=0)
        thread = multiprocessing.Process(name="Serial Thread",
                                         target=read_from_port,
                                         kwargs={'port': Constants.ARDUINO_PORT,
                                                 'baud_rate': Constants.ARDUINO_BAUDRATE,
                                                 'queue': queue})
        thread.daemon = True
        thread.start()
    if Constants.ENABLE_PID:
        # PID THREAD
        thread3 = multiprocessing.Process(name="PID Thread",
                                          target=speed_control,
                                          kwargs={'queue': queue,
                                                  'quadcopter': quadcopter,
                                                  'message_sender': message_sender,
                                                  'middleware_arduino': middleware_arduino})
        thread3.daemon = True
        thread3.start()

        # TEST USING A BACKGROUND THREAD
        # thread3 = Thread(target=background_thread)
        # thread3.daemon = True
        # thread3.start()


# def background_thread():
#     """Example of how to send server generated events to clients."""
#     count = 0
#     import time
#     while True:
#         time.sleep(10)
#         count += 1
#         socketio.emit('my response',
#                       {'data': 'Server generated event', 'count': count},
#                       namespace='/test')


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
    middleware_ios.parseMessage(data)


if __name__ == '__main__':
    socketio.run(app,
                 debug=Constants.ENABLE_FLASK_DEBUG_MODE,
                 host=Constants.SERVER_IP,
                 port=Constants.SERVER_PORT,
                 use_reloader=False)

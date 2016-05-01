async_mode = None
queue = None
if async_mode is None:
    try:
        from gevent import monkey, Timeout

        async_mode = 'gevent'

    except ImportError:
        pass

    # if async_mode is None:
    #     try:
    #         import eventlet
    #
    #         async_mode = 'eventlet'
    #
    #     except ImportError:
    #         pass
    #
    # if async_mode is None:
    #     async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'gevent':
    from gevent import monkey

    monkey.patch_all()
# elif async_mode == 'eventlet':
#     from eventlet import monkey_patch
#
#     monkey_patch()

import logging
import os
from logging.handlers import RotatingFileHandler

import gipc
import serial
from flask import Flask, request, render_template
from flask_socketio import SocketIO

import constants
from quadcopterComponents.quadcopter import Quadcopter

# Socket-io server example
# https://github.com/miguelgrinberg/Flask-SocketIO/blob/v2.2/example/app.py

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)
thread = None
quadcopter = None
thread3 = None
middleware = None
message_sender = None
pi_logger = None
sender, reader = None,None

def read_from_port(port, baud_rate, sender, logger):
    """

    :param event: Thread.Event to call upon reading data froms serial (Used by IOSSenderThread)
    :param serial_port: serial.Serial() variable specifying serial port of arduino decice
    """

    name = "ArduinoReaderSubroutine"
    logger.setup_init(name)
    try:
        serial_port = serial.Serial(port, baud_rate)
    except Exception as e:
        logger.error(e)
        logger.setup_failure(name)
        return
    logger.setup_success(name)
    # queue.put("HELLO")
    logger.setup_message("SERIAL WORKER THREAD STARTED with object (%s)" % serial_port)

    while True:
        reading = serial_port.readline().decode("Utf-8").rstrip()
        if reading:
            try:
                sender.put(reading)
            except Exception as e:
                logger.error(e)


def speed_control(reader, quadcopter, message_sender, middleware, logger):
    """
        Requires middleware, Quadcopter, Message_sender params
    """
    import time
    # Wait for Serial Setup to complete (Marked by "SETUP COMPLETED:" MESSAGE)

    # logger.setup_init(name)
    #
    # logger.setup_message("Waiting for first reading")
    # reading = reader.get()
    # while not middleware.parseMessage(reading):
    #     # parseMessage returns true, when setup is completed
    #     reading = reader.get()
    #     # middleware.parseMessage(reading)
    # logger.setup_success(name)
    name = "QuadController"
    # def parseMessage(msg):
    #     from customlogger import arduino_logger
    #     logger = arduino_logger()
    #     try:
    #         # from quadcopterComponents import Quadcopter
    #         # self.quadcopter = Quadcopter()
    #
    #         functionName, params = msg.split(':')
    #         if functionName == constants.ARDUINOMESSAGE_GYRO:
    #
    #             # DATA:Y;P;R;Mx;My;Mz;Mh
    #
    #             y, p, r, heading = map(lambda x: float(x), params.split(';'))
    #             logger.data_gyromag(gyro=[y, p, r], heading=heading)
    #             quadcopter.gyro.set_ypr_current([y, p, r])
    #
    #         elif functionName == constants.ARDUINOSTATUS_ULTRA:
    #             logger.data_ultrasound(params.split(';'))
    #             # ORDER: BOTTOM, TOP, FRONT, RIGHT, LEFT
    #             bottom, top, front, right, left = map(lambda x: float(x), params.split(';'))
    #             quadcopter.altitude.set_sensor_altitude_current(bottom)
    #             quadcopter.ultra.set_sensor_ultra_values(front=front, left=left, right=right, top=top)
    #
    #         elif functionName == constants.ARDUINOMESSAGE_MOTOR:
    #             logger.data_motor_speeds(params.split(';'))
    #         elif functionName == constants.ARDUINOSTATUS_SETUP_INITIALIZING:
    #             logger.setup_init(params)
    #         elif functionName == constants.ARDUINOSTATUS_SETUP_SUCCESS:
    #             logger.setup_success(params)
    #         elif functionName == constants.ARDUINOSTATUS_SETUP_FAILURE:
    #             logger.setup_failure(params)
    #         elif functionName == constants.ARDUINOSTATUS_SETUP_ERRORCODE:
    #             logger.setup_errorcode(params)
    #         elif functionName == constants.ARDUINOSTATUS_SETUP_MESSAGE:
    #             logger.setup_message(params)
    #         elif functionName == "SETUP COMPLETED":
    #             return True
    #         return False
    #
    #     except ValueError as e:
    #         print e

    speeds, oldspeeds = [0, 0, 0, 0], [0, 0, 0, 0]
    quadcopter.takeoff()
    while True:
        # CHECK MESSAGE QUEUE FOR ARDUINO INPUTS
        reading = None
        with Timeout(constants.ARDUINO_MESSAGE_REFRESHTIME,False) as t:
            reading = reader.get(timeout=t)
        if reading is None:
            # TODO: This means that no data is being received from arduino, which means quad needs to go into hover mode/land, because of some serial error
            logger.error("ARDUINO NOT SENDING DATA..")
        else:
            middleware.parseMessage(reading)
            while True:
                reading = None
                with Timeout(0.02, False) as t:
                    reading = reader.get(timeout=t)
                if reading is not None:
                    middleware.parseMessage(reading)
                else:
                    break
        oldspeeds = speeds[:]
        speeds = quadcopter.refresh()
        if should_send_new_motor_speed(oldspeeds, speeds):
            print speeds
            message_sender.toArduino_set_speed(speeds)
        time.sleep(constants.REFRESH_PID_TIME)


def should_send_new_motor_speed(old_speed, new_speed):
    return old_speed != new_speed


@app.route("/", methods=['GET', 'POST'])
def index():
    global quadcopter,sender
    if request.method == "POST":
        if 'quad_setSpeed' in request.form:
            sender.put(constants.IOSMESSAGE_SETSPEED+':'+request.form["quad_setSpeed_text"])

            # quadcopter.set_speed(int(request.form["quad_setSpeed_text"]))
        elif 'set_ypr' in request.form:
            print request.form
            ypr = [0.0, 0.0, 0.0]
            if request.form['set_ypr_y'] != '':
                ypr[0] = float(request.form['set_ypr_y'])
            if request.form['set_ypr_p'] != '':
                ypr[1] = float(request.form['set_ypr_p'])
            if request.form['set_ypr_r'] != '':
                ypr[2] = float(request.form['set_ypr_r'])
            sender.put(constants.IOSMESSAGE_SETYPR+':'+';'.join(ypr))
            # quadcopter.set_ypr_desired(ypr)

        elif 'takeoff' in request.form:
            sender.put(constants.IOSMESSAGE_TAKEOFF)
            # quadcopter.takeoff()
        elif 'land' in request.form:
            sender.put(constants.IOSMESSAGE_LAND)
            # quadcopter.land()
        elif 'hover' in request.form:
            sender.put(constants.IOSMESSAGE_HOVER)
            # quadcopter.set_mode_hover_enable()
        elif 'hold_altitude' in request.form:
            sender.put(constants.IOSMESSAGE_HOLDALTITUDE)
            # quadcopter.set_mode_altitude_hold_enable()

        # elif 'change_pid' in request.form:
        #     p, i, d = 0.0, 0.0, 0.0
        #     if request.form['set_kp'] != '':
        #         p = float(request.form['set_kp'])
        #     if request.form['set_ki'] != '':
        #         i = float(request.form['set_ki'])
        #     if request.form['set_kd'] != '':
        #         d = float(request.form['set_kd'])
        #     quadcopter.__set_pid_test__(p, i, d)
    # return '%s' % queue.get()
    return render_template("index.html")


# @app.before_first_request
def initialSetup():
    global quadcopter, middleware, message_sender, pi_logger
    from middleware import Middleware

    from customlogger import pi_logger
    pi_logger = pi_logger()
    quadcopter = Quadcopter(pi_logger)

    from message_sender import Message_sender
    message_sender = Message_sender(socketio)

    middleware = Middleware(quadcopter)

    # TODO Implement Logging
    if constants.ENABLE_FLASK_LOGGING:
        formatter = logging.Formatter(
            constants.LOG_FORMAT_FLASK)
        handler = RotatingFileHandler(os.path.join(constants.LOG_LOCATION_FLASK, constants.LOG_FILENAME_FLASK),
                                      maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)

    import bonjour
    service = bonjour.Bonjour(pi_logger)
    service.publish()


    # global queue
    # from gevent import queue
    # queue = queue.Queue()
    # http://www.gevent.org/gevent.queue.html
    global sender,reader
    reader,sender = gipc.pipe()
    global thread, thread3


    if constants.ENABLE_SERIAL:
        # thread = threading.Thread(name="Serial Thread",

        thread = gipc.start_process(name="Serial Thread",
                                    daemon=True,

                                    target=read_from_port,
                                    kwargs={'port': constants.ARDUINO_PORT,
                                            'baud_rate': constants.ARDUINO_BAUDRATE,
                                            'sender': sender,
                                            'logger': pi_logger}
                                    )

    thread3 = gipc.start_process(name="PID Thread",
                                 daemon=True,
                                 target=speed_control,
                                 kwargs={'reader': reader,
                                         'quadcopter': quadcopter,
                                         'message_sender': message_sender,
                                         'middleware': middleware, 'logger': pi_logger},

                                 )
    # speed_control(reader=reader,quadcopter=quadcopter,message_sender=message_sender,middleware=middleware,logger=pi_logger)
    # message_sender.__send_msg_to_arduino__("HELLOn\n")

    @socketio.on('connect', namespace=constants.SOCKETIO_NAMESPACE)
    def test_connect():
        print 'Client connected : %s' % request
        return True

    @socketio.on('disconnect', namespace=constants.SOCKETIO_NAMESPACE)
    def test_disconnect():
        print 'Client disconnected : %s' % request
        return True

    @socketio.on('message', namespace=constants.SOCKETIO_NAMESPACE)
    def handle_message(data):
        print data
        socketio.emit('message', 'HELLOAGAIN')
        global middleware
        middleware.parseMessage(data)


if __name__ == '__main__':
    initialSetup()
    socketio.run(app,
                 debug=constants.ENABLE_FLASK_DEBUG_MODE,
                 host=constants.SERVER_IP,
                 port=constants.SERVER_PORT,
                 use_reloader=False)

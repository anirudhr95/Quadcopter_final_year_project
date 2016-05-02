async_mode = None

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

import Constants
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
queue = None
senderexternal,readerexternal = None,None

def read_from_port(port, baud_rate, sender, logger):
    """

    :param event: Thread.Event to call upon reading data froms serial (Used by IOSSenderThread)
    :param serial_port: serial.Serial() variable specifying serial port of arduino decice
    """
    import time
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
                # externalreceiver.append(reading)
                sender.put(reading)
                # print reading
            except Exception as e:
                logger.error(e)

        # time.sleep(Constants.ARDUINO_MESSAGE_REFRESHTIME - 0.1)

def speed_control(reader, quadcopter, message_sender, middleware, logger, reader2):
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

    logger.setup_init(name)

    logger.setup_message("Waiting for first reading")

    reading = reader.get()
    while not middleware.parseMessage(reading):
        # parseMessage returns true, when setup is completed
        # print externalreceiver
        reading = reader.get()
        # middleware.parseMessage(reading)
    logger.setup_success(name)
    speeds, oldspeeds = [0, 0, 0, 0], [0, 0, 0, 0]
    quadcopter.takeoff()
    while True:
        # CHECK MESSAGE QUEUE FOR ARDUINO INPUTS
        for val in [reader,reader2]:
            reading = None
            with Timeout(Constants.ARDUINO_MESSAGE_REFRESHTIME,False) as t:
                reading = val.get(timeout=t)
                if reading is None:
                    # TODO: This means that no data is being received from arduino, which means quad needs to go into hover mode/land, because of some serial error
                    logger.error("ARDUINO NOT SENDING DATA..")
                else:
                    # print reading
                    middleware.parseMessage(reading)
                    while True:
                        reading = None
                        with Timeout(0.02, False) as t:
                            reading = val.get(timeout=t)
                        if reading is not None:
                            middleware.parseMessage(reading)
                        else:
                            break
        # CALCULATE PID AND ADJUST

        speeds = quadcopter.refresh()
        if should_send_new_motor_speed(oldspeeds, speeds):
            # print speeds
            # print oldspeeds,speeds,should_send_new_motor_speed(oldspeeds, speeds)
            message_sender.toArduino_set_speed(speeds)
            oldspeeds = speeds[:]

        time.sleep(Constants.REFRESH_PID_TIME)


def should_send_new_motor_speed(old_speed, new_speed):
    # def gorl(a,b,lim=50):
    #     return True if (b>a+lim or b<a-lim) else False
    #
    # if filter(lambda x:  gorl(x[0],x[1]),zip(old_speed,new_speed)):
    #     return True
    # return False
    return old_speed != new_speed


@app.route("/", methods=['GET', 'POST'])
def index():
    global queue
    if request.method == "POST":
        if 'quad_setSpeed' in request.form:
            queue.put(Constants.IOSMESSAGE_SETSPEED+':'+request.form["quad_setSpeed_text"])

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
            queue.put('%s:%s'%(Constants.IOSMESSAGE_SETYPR,';'.join(str(val) for val in ypr)))
            # quadcopter.set_ypr_desired(ypr)

        elif 'takeoff' in request.form:
            # queue.put(Constants.IOSMESSAGE_TAKEOFF)
            from gevent import Greenlet
            Greenlet.spawn(passmessagetoproc, senderexternal)
            # quadcopter.takeoff()
        elif 'land' in request.form:
            queue.put(Constants.IOSMESSAGE_LAND)
            # quadcopter.land()
        elif 'hover' in request.form:
            queue.put(Constants.IOSMESSAGE_HOVER)
            # quadcopter.set_mode_hover_enable()
        elif 'hold_altitude' in request.form:
            queue.put(Constants.IOSMESSAGE_HOLDALTITUDE)
            # quadcopter.set_mode_altitude_hold_enable()

    return render_template("index.html")

def passmessagetoproc(sender):


    print "\n\n\nGOT VAL : %s"%Constants.IOSMESSAGE_TAKEOFF
    sender.put(Constants.IOSMESSAGE_TAKEOFF)


# @app.before_first_request
def initialSetup():
    global quadcopter, middleware, message_sender, pi_logger
    from middleware import Middleware

    from CustomLogger import pi_logger
    pi_logger = pi_logger()
    quadcopter = Quadcopter(pi_logger)

    from message_sender import Message_sender
    message_sender = Message_sender(socketio)

    middleware = Middleware(quadcopter)

    # TODO Implement Logging
    if Constants.ENABLE_FLASK_LOGGING:
        formatter = logging.Formatter(
            Constants.LOG_FORMAT_FLASK)
        handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_FLASK, Constants.LOG_FILENAME_FLASK),
                                      maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        app.logger.addHandler(handler)

    import bonjour
    service = bonjour.Bonjour(pi_logger)
    service.publish()


    global queue
    from gevent import queue,Greenlet
    queue = queue.Queue()
    # http://www.gevent.org/gevent.queue.html

    global sender,reader,senderexternal,readerexternal
    reader,sender = gipc.pipe()
    readerexternal,senderexternal = gipc.pipe()
    global thread, thread3


    if Constants.ENABLE_SERIAL:
        # thread = threading.Thread(name="Serial Thread",

        thread = gipc.start_process(name="Serial Thread",
                                    daemon=True,

                                    target=read_from_port,
                                    kwargs={'port': Constants.ARDUINO_PORT,
                                            'baud_rate': Constants.ARDUINO_BAUDRATE,
                                            'sender': sender,
                                            'logger': pi_logger,
                                            }
                                    )
    Greenlet.spawn(passmessagetoproc,senderexternal)
    thread3 = gipc.start_process(name="PID Thread",
                                 daemon=True,
                                 target=speed_control,
                                 kwargs={'reader': reader,
                                         'quadcopter': quadcopter,
                                         'message_sender': message_sender,
                                         'middleware': middleware, 'logger': pi_logger,
                                         'reader2':readerexternal}

                                 )
    # speed_control(reader=reader,quadcopter=quadcopter,message_sender=message_sender,middleware=middleware,logger=pi_logger)
    # message_sender.__send_msg_to_arduino__("HELLOn\n")

    @socketio.on('connect', namespace=Constants.SOCKETIO_NAMESPACE)
    def test_connect():
        print 'Client connected : %s' % request
        return True

    @socketio.on('disconnect', namespace=Constants.SOCKETIO_NAMESPACE)
    def test_disconnect():
        print 'Client disconnected : %s' % request
        return True

    @socketio.on('message', namespace=Constants.SOCKETIO_NAMESPACE)
    def handle_message(data):
        print data
        socketio.emit('message', 'HELLOAGAIN')
        global middleware
        middleware.parseMessage(data)


if __name__ == '__main__':
    initialSetup()
    socketio.run(app,
                 debug=Constants.ENABLE_FLASK_DEBUG_MODE,
                 host=Constants.SERVER_IP,
                 port=Constants.SERVER_PORT,
                 use_reloader=False)

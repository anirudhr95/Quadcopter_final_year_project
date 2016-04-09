"""
Logs each kind of input differently
"""
from logging.handlers import RotatingFileHandler
import os
import logging, logging.config
import Constants


class ArduinoLogger:
    def __init__(self):
        self.logger = logging.getLogger("ARDUINO")
        formatter = logging.Formatter(
            Constants.LOG_FORMAT_APP)
        handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_APP, Constants.LOG_FILENAME_APP),
                                      maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def setup_init(self, module):
        self.logger.info("SETUP-INITIALIZING:%s" % module)

    def setup_success(self, module):
        self.logger.info("SETUP-SUCCESS:%s" % module)

    def setup_failure(self, module):
        self.logger.critical("SETUP-FAILURE:%s" % module)

    def setup_message(self, message):
        self.logger.info("SETUP-MESSAGE:%s" % message)

    def setup_errorcode(self, code):
        self.logger.error("ERROR-CODE:%s" % code)

    def data_motor_speeds(self, speeds):
        self.logger.debug("MOTOR-SPEED:%s" % (";".join(speeds)))

    def data_gyromag(self, gyro, mag, heading):
        self.logger.debug("GYRO-MAG:%s;%s;%s" % (";".join(gyro), ';'.join(mag), heading))

    def data_ultrasound(self, mode, data):
        self.logger.debug("%s:%s" % (mode, data))

    def data_altitude(self, data):
        self.logger.debug("ALTITUDE:%s" % data)


class IOSLogger:
    def __init__(self):
        self.logger = logging.getLogger("IPHONE")
        formatter = logging.Formatter(
            Constants.LOG_FORMAT_APP)
        handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_APP, Constants.LOG_FILENAME_APP),
                                      maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def Takeoff(self):
        self.logger.debug("%s" % (Constants.IOSMESSAGE_TAKEOFF))

    def Land(self):
        self.logger.debug("%s" % (Constants.IOSMESSAGE_LAND))

    def Set_Speed(self, speed):
        self.logger.debug("%s %s" % (Constants.IOSMESSAGE_SETSPEED, speed))

    def hover(self, state):
        self.logger.debug("%s:%s" % (Constants.IOSMESSAGE_HOVER, state))

    def altitude_hold(self, state):
        self.logger.debug("%s:%s" % (Constants.IOSMESSAGE_HOLDALTITUDE, state))

    def set_ypr(self, ypr):
        self.logger.debug("%s:%s" % (Constants.IOSMESSAGE_SETYPR, ";".join(ypr)))

    def error(self, error):
        self.logger.error("%s:%s" % (Constants.IOSMESSAGE_ERROR, error))


class PILogger:
    def __init__(self):
        self.logger = logging.getLogger("PI")

        formatter = logging.Formatter(
            Constants.LOG_FORMAT_APP)
        handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_APP, Constants.LOG_FILENAME_APP),
                                      maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def data_set_speeds(self, motor_speeds):  # int i 0 to 4
        self.logger.debug("%s:%s" % (Constants.PIMESSAGE_SETSPEEDS, ';'.join(str(val) for val in motor_speeds)))

    def state_ultra_mode(self, mode):
        self.logger.info("%s;%s" % (Constants.PIMESSAGE_ULTRAMODE, mode))

    def data_set_altitude(self,altitude):
        self.logger.debug("SET_ALTITUDE:"%altitude)
    def data_set_ypr(self, ypr):
        self.logger.info("%s:%s" % (Constants.IOSMESSAGE_SETYPR, ";".join(str(val) for val in ypr)))

    def state_reset_baro(self):
        self.logger.info("%s" % Constants.PIMESSAGE_RESETBAROREFERENCE)

    def warn_collision(self, direction, sensor_value):
        self.logger.critical("COLLISION:%s-%s" % (direction, sensor_value))

    def mode_Takeoff(self):
        self.logger.info("%s" % (Constants.IOSMESSAGE_TAKEOFF))

    def mode_Land(self):
        self.logger.info("%s" % (Constants.IOSMESSAGE_LAND))

    def mode_hover(self):
        self.logger.info("%s" % (Constants.IOSMESSAGE_HOVER))

    def mode_flight(self):
        self.logger.info("%s" % (Constants.IOSMESSAGE_FLIGHTMODE))

    def mode_altitude_hold(self, state):
        self.logger.info("%s:%s" % (Constants.IOSMESSAGE_HOLDALTITUDE, state))
    def error(self,msg):
        self.logger.error("PROCESSING_ERROR:%s"%msg)



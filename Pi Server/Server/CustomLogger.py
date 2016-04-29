"""
Logs each kind of input differently
"""
import logging
import logging.config
import os
from logging.handlers import RotatingFileHandler

import constants


class arduino_logger:
    def __init__(self):
        self.logger = logging.getLogger("ARDUINO")
        formatter = logging.Formatter(
            constants.LOG_FORMAT_APP)
        handler = RotatingFileHandler(os.path.join(constants.LOG_LOCATION_APP, constants.LOG_FILENAME_APP),
                                      maxBytes=10000000, backupCount=5)

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.logger.setLevel(logging.DEBUG)

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

    def data_gyromag(self, gyro,heading):
        self.logger.debug("GYRO-MAG:%s;%s" % (";".join(str(val) for val in gyro), heading))

    def data_ultrasound(self, data):
        # print data
        self.logger.debug("ULTRA:%s" % (';'.join(str(val) for val in data)))
        assert isinstance(data, list)



    def data_altitude(self, data):
        self.logger.debug("ALTITUDE:%s" % data)


class ios_logger:
    def __init__(self):
        self.logger = logging.getLogger("IPHONE")
        formatter = logging.Formatter(
            constants.LOG_FORMAT_APP)
        handler = RotatingFileHandler(os.path.join(constants.LOG_LOCATION_APP, constants.LOG_FILENAME_APP),
                                      maxBytes=10000000, backupCount=5)

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.logger.setLevel(logging.DEBUG)

    def takeoff(self):
        self.logger.debug("%s" % (constants.IOSMESSAGE_TAKEOFF))

    def land(self):
        self.logger.debug("%s" % (constants.IOSMESSAGE_LAND))

    def set_Speed(self, speed):
        self.logger.debug("%s %s" % (constants.IOSMESSAGE_SETSPEED, speed))

    def hover(self):
        self.logger.debug("%s" % (constants.IOSMESSAGE_HOVER))

    def flight(self):
        self.logger.debug("%s" % (constants.IOSMESSAGE_FLIGHTMODE))

    def altitude_hold(self, state):
        self.logger.debug("%s:%s" % (constants.IOSMESSAGE_HOLDALTITUDE, state))

    def set_ypr(self, ypr):
        self.logger.debug("%s:%s" % (constants.IOSMESSAGE_SETYPR, ";".join(ypr)))

    def error(self, error):
        self.logger.error("%s:%s" % (constants.IOSMESSAGE_ERROR, error))


class pi_logger:
    def __init__(self):
        self.logger = logging.getLogger("PI")

        formatter = logging.Formatter(
            constants.LOG_FORMAT_APP)
        handler = RotatingFileHandler(os.path.join(constants.LOG_LOCATION_APP, constants.LOG_FILENAME_APP),
                                      maxBytes=10000000, backupCount=5)

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.logger.setLevel(logging.DEBUG)

    def data_set_speeds(self, motor_speeds):  # int i 0 to 4
        self.logger.debug("%s:%s" % (constants.PIMESSAGE_SETSPEEDS, ';'.join(str(val) for val in motor_speeds)))



    def data_set_altitude(self, altitude):
        self.logger.debug("SET_ALTITUDE:%s" % altitude)

    def data_set_ypr(self, ypr):
        self.logger.info("%s:%s" % (constants.IOSMESSAGE_SETYPR, ";".join(str(val) for val in ypr)))

    def warn_collision(self, direction, sensor_value):
        self.logger.critical("COLLISION:%s-%s" % (direction, sensor_value))

    def mode_Takeoff(self):
        self.logger.info("%s" % (constants.IOSMESSAGE_TAKEOFF))

    def mode_Land(self):
        self.logger.info("%s" % (constants.IOSMESSAGE_LAND))

    def mode_hover(self):
        self.logger.info("%s" % (constants.IOSMESSAGE_HOVER))

    def mode_flight(self):
        self.logger.info("%s" % (constants.IOSMESSAGE_FLIGHTMODE))

    def mode_altitude_hold(self, state):
        self.logger.info("%s:%s" % (constants.IOSMESSAGE_HOLDALTITUDE, state))

    def error(self, msg):
        self.logger.error("PROCESSING_ERROR:%s" % msg)

    def data_ultrasound(self, data):
        # assert isinstance(data, list)
        self.logger.debug("%s" % (';'.join(str(val) for val in data)))

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
    def message(self,module,message):
        self.logger.info("MESSAGE:%s:%s"%(module,message))

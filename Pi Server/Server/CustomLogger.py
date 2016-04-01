"""
Logs each kind of input differently
"""
from logging.handlers import RotatingFileHandler
import os
import logging
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

    def ultrasound_data(self, data = [0 for i in range(4)]):
        pass
    def error(self, message, options = ''):
        pass
    def flight_mode_changed(self, active_modes, options=''):
        pass

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
    def sensor_data(self, ypr):
        pass
    def Takeoff(self):
        pass

    def Land(self):
        pass

    def Set_Speed(self, speed):
        pass

    def hover(self, state):
        pass

    def altitude_hold(self, state):
        pass

class PILogger:
    def __init__(self):
        self.logger = logging.getLogger("RASP-PI")

        formatter = logging.Formatter(
            Constants.LOG_FORMAT_APP)
        handler = RotatingFileHandler(os.path.join(Constants.LOG_LOCATION_APP, Constants.LOG_FILENAME_APP),
                                      maxBytes=10000000, backupCount=5)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

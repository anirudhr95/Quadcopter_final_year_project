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
        logging.info("%s %s" %(Constants.ARDUINOSTATUS_ULTRASOUND_DATA,data))

    def error(self, message, options = ''):
        logging.info("%s %s %s" %(Constants.ARDUINOSTATUS_ERROR,message,options))

    def ultrasound_collide(self,sensor_ID):
        logging.info("%s %s" %(Constants.ARDUINOSTATUS_ULTRASOUND_COLLISION,sensor_ID))

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
        logging.info("%s" %(Constants.IOSCOMMAND_TAKEOFF))

    def Land(self):
        logging.info("%s" %(Constants.IOSCOMMAND_LAND))

    def Set_Speed(self, speed):
        logging.info("%s %s"%(Constants.IOSCOMMAND_SETSPEED,speed))

    def hover(self, state):
        logging.info("%s %s"%(Constants.IOSCOMMAND_HOVER,state))

    def altitude_hold(self, state):
        logging.info("%s %s"%(Constants.IOSCOMMAND_HOLDALTITUDE,state))
    def set_ypr(self,y,p,r):
        logging.info("%s %s %s %s"%(Constants.IOSCOMMAND_SETYPR,y,p,r))
    def error(self,error):
        logging.info("%s %s"%(Constants.IOSCOMMAND_ERROR,error))

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

        def set_speed(self, motor_speed ): #int i 0 to 4
            logging.info("%s %s"%(Constants.PICOMMAND_SETSPEEDS,motor_speed))
        def error(self , error):
            logging.info("%s %s"%(Constants.PICOMMAND_ERROR,error))

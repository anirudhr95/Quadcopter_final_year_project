import Constants
import pi_send
from Server import socketio

class middleware:
    def __init__(self, direction):
        """
        directions : 1-ArduinoToIphone, 2- IphoneToArduino"""
        self.direction = direction

        self.p2a = pi_send.pi_send_toArduino()
        self.p2i = pi_send.pi_send_toIOS()

    def __send_to_iphone__(self, data):
        functionName,params = data.split(':')
        if functionName == Constants.ARDUINOSTATUS_ERROR:
            return self.p2i.error(params)
        if functionName == Constants.ARDUINOSTATUS_ULTRASOUND_COLLISION:
            return self.p2i.collision(params.split(';'))
        if functionName == Constants.ARDUINOSTATUS_ULTRASOUND_DATA:
            return self.p2i.ultra_data(params.split(';'))
    def __send_to_arduino__(self, data):
        functionName,params = str(data).split(' ')
        if functionName ==Constants.IOSCOMMAND_TAKEOFF:
            return self.p2a.takeoff()
        if functionName == Constants.IOSCOMMAND_LAND:
            return self.p2a.land()
        if functionName == Constants.IOSCOMMAND_HOLDALTITUDE:
            return self.p2a.altitude_hold()
        if functionName == Constants.IOSCOMMAND_HOVER:
            return self.p2a.hover()
        if functionName == Constants.IOSCOMMAND_SETSPEED:
            return self.p2a.set_speed(params)
        if functionName == Constants.IOSCOMMAND_SETYPR:
            return self.p2a.setYPR(params.split(';'))

    def message_to_send(self, params):
        if self.direction==1:
            return self.__send_to_iphone__(params)
        elif self.direction == 2:
            return self.__send_to_arduino__(params)
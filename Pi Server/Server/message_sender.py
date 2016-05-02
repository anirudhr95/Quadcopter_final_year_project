import serial

import Constants


class Message_sender:
    def __init__(self, socketio):
        self.__message_queue__ = []
        self.socketio = socketio
        self.serial_port = None
        if Constants.ENABLE_SERIAL:
            self.serial_port = serial.Serial(Constants.ARDUINO_PORT, Constants.ARDUINO_BAUDRATE)

    def __send_msg_to_ios__(self, msg):
        print "\n\n\n\n\n\nSENDING '%s' To IOS " % str(msg)
        self.socketio.emit('message', msg, namespace=Constants.SOCKETIO_NAMESPACE)

    def __send_msg_to_arduino__(self, msg):
        if self.serial_port:
            self.serial_port.write(msg)
            return True
        return False

    def toIOS_error(self, message):
        self.__send_msg_to_ios__({
            'event': Constants.PIMESSAGE_ERROR,
            'data': message
        })

    def toIOS_collision(self, idANDval):
        self.__send_msg_to_ios__({
            'event': Constants.PIMESSAGE_COLLISION,
            'data': {'id': idANDval[0],
                     'val': idANDval[1]}

        })

    def toIOS_ultra_data(self, ultraValues):
        self.__send_msg_to_ios__({
            'event': Constants.ARDUINOSTATUS_ULTRA,
            'data': ultraValues
        })

    def toArduino_set_speed(self, speeds):
        msg = '%s:%s;%s;%s;%s\n' % (Constants.PIMESSAGE_SETSPEEDS, speeds[0], speeds[1], speeds[2], speeds[3])
        return self.__send_msg_to_arduino__(msg)

import serial

import Constants


class Message_sender:
    def __init__(self, socketio):
        self.__message_queue__ = []
        self.socketio = socketio
        if Constants.ENABLE_SERIAL:
            self.serial_port = serial.Serial(Constants.ARDUINO_PORT, Constants.ARDUINO_BAUDRATE)

    def __send_msg_to_ios__(self, msg):
        print "SENDING '%s' To IOS " % str(msg)
        self.socketio.emit('message', msg, namespace=Constants.SOCKETIO_NAMESPACE)

    def __send_msg_to_arduino__(self, msg):
        if Constants.ENABLE_SERIAL:
            self.serial_port.write(msg)

    def toIOS_error(self, message):
        self.__send_msg_to_ios__({
            'event': Constants.ARDUINOSTATUS_ERROR,
            'data': message
        })

    def toIOS_collision(self, idANDval):
        self.__send_msg_to_ios__({
            'event': Constants.ARDUINOSTATUS_ULTRASOUND_COLLISION,
            'data': {'id': idANDval[0],
                     'val': idANDval[1]}

        })

    def toIOS_ultra_data(self, ultraValues):
        self.__send_msg_to_ios__({
            'event': Constants.ARDUINOSTATUS_ULTRASOUND_DATA,
            'data': ultraValues
        })

    def toArduino_set_speed(self, speeds):
        msg = '%s:%s;%s;%s;%s' % (Constants.PIMESSAGE_SETSPEEDS, speeds[0], speeds[1], speeds[2], speeds[3])
        self.__send_msg_to_arduino__(msg)



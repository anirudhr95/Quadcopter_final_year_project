import serial

import Constants


class Message_sender:
    def __init__(self, socketio, serial_port):
        self.__message_queue__ = []
        self.socketio = socketio
        self.serial_port = serial.Serial('/dev/cu.usbmodem1421', 115200)

    def __send_msg_to_ios__(self, msg):
        print "SENDING '%s' To IOS " % str(msg)
        self.socketio.emit('message', msg, namespace=Constants.SOCKETIO_NAMESPACE)

    def __send_msg_to_arduino__(self, msg):
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

    def toArduino_reset_baro(self):
        self.__send_msg_to_arduino__(Constants.PIMESSAGE_RESETBAROREFERENCE)

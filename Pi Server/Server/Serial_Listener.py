"""
# http://stackoverflow.com/questions/17553543/pyserial-non-blocking-read-loop
TODO USE Threading for async reads as shown in link above
import threading

connected = False
port = 'COM4'
baud = 9600

serial_port = serial.Serial(port, baud, timeout=0)

def handle_data(data):
    print(data)

def read_from_port(ser):
    while not connected:
        #serin = ser.read()
        connected = True

        while True:
           print("test")
           reading = ser.readline().decode()
           handle_data(reading)

thread = threading.Thread(target=read_from_port, args=(serial_port,))
thread.start()


#Interfacing with arduino (http://playground.arduino.cc/Interfacing/Python)

 import serial
ser = serial.Serial('/dev/tty.usbserial', 9600)
while True:
...     print ser.readline()
'1 Hello world!\r\n'
'2 Hello world!\r\n'
'3 Hello world!\r\n'

Writing data to Arduino is easy too (the following applies to Python 2.x):

import serial # if you have not already done so
ser = serial.Serial('/dev/tty.usbserial', 9600)
ser.write('5')

"""

import threading
import serial
import Constants
from middleware import middleware
from Server import global_vars

def handle_data(reading):
    message = global_vars.SENDER_Iphone.message_to_send(reading)
    global_vars.socketio.emit(message['event'],message['data'],'/test')


class Serial_Worker:
    connected = False
    middleware = middleware(direction=1)
    def __init__(self):


        self.serial_port = serial.Serial(Constants.ARDUINO_PORT, Constants.ARDUINO_BAUDRATE, timeout=0)
        self.thread = threading.Thread(target=self.__read_from_port__, args=(self.serial_port,))

    def send(self, message):
        # Serial_Worker.messageQueue.append(message)
        if Serial_Worker.connected:
            Serial_Worker.connected = False
            self.thread.join(timeout=0.1)
        self.__write__(message)
        self.thread.start()

    def start_worker(self):
        self.thread.start()

    def __read__(self):
        return self.serial_port.readline()

    def __write__(self, msg):
        self.serial_port.flushInput()
        self.serial_port.write(msg)

    def __read_from_port__(self):
        """
        :param ser Serial port (serial.Serial) to read from
        """

        while not Serial_Worker.connected:

            Serial_Worker.connected = True

            while True:
                reading = self.serial_port.readline()
                # Handles the data



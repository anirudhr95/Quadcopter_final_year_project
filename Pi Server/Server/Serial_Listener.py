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

connected = False
serial_port = serial.Serial(Constants.ARDUINO_PORT, Constants.ARDUINO_BAUDRATE, timeout=0)


def handle_data(data):
    print(data)


def __read_from_port__(ser):
    """
    :param ser Serial port (serial.Serial) to read from
    """
    global  connected
    while not connected:

        connected = True

        while True:
            reading = ser.readline()
            handle_data(reading)


thread = threading.Thread(target=__read_from_port__, args=(serial_port,))


def start_service():
    thread.start()

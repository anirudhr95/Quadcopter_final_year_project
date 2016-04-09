import socket

# CONTROL VARIABLES
ENABLE_FLASK_LOGGING = False
ENABLE_FLASK_DEBUG_MODE = True
ENABLE_BONJOUR_REGISTER = True
ENABLE_SERIAL = True
ENABLE_IOS_SENDER = True
ENABLE_PID = True
TESTING_MODE = True


#SOCKET-IO
SOCKETIO_NAMESPACE = '/test'

# SERVER INFO
SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5000

# LOGGING CONSTANTS
LOG_LOCATION_FLASK = "~/Desktop"
LOG_FILENAME_FLASK = "FlaskLog.log"
LOG_FORMAT_FLASK   = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
LOG_LOCATION_APP   = "./"
LOG_FILENAME_APP   = "Quadcopter.log"
LOG_FORMAT_APP     = "%(asctime)s %(name)s %(levelname)s : %(message)s"

# BONJOUR SERVICE INFO

BONJOUR_TYPE = "_http._tcp.local."
BONJOUR_NAME = "quadcopter bonjour service"
BONJOUR_DESC = {'Project_By': 'Shyam, Jo, Anirudh, Kaushik'}
BONJOUR_SERVICE_NAME = "dont-have-a-server-socool.local."
BONJOUR_REPLACEMENT_STATICIP = "0.0.0.0"
BONJOUR_WEIGHT = 0
BONJOUR_PRIORITY = 0


#PYSERIAL
# ARDUINO_PORT = '/dev/tty.usbserial'
ARDUINO_PORT = '/dev/cu.usbmodem1411'
ARDUINO_BAUDRATE = 9600

#IOS COMMANDS RECEIVED
IOSMESSAGE_TAKEOFF = 'TAKEOFF'
IOSMESSAGE_LAND = 'LAND'
IOSMESSAGE_SETSPEED = 'SET_SPEED'
IOSMESSAGE_HOVER = 'MODE_HOVER'
IOSMESSAGE_HOLDALTITUDE = 'MODE_ALTITUDE_HOLD'
IOSMESSAGE_SETYPR = 'SET_YPR'
IOSMESSAGE_ERROR = "ERROR"
IOSMESSAGE_FLIGHTMODE = "MODE_FLIGHT"

#PI COMMANDS
PIMESSAGE_SETSPEEDS = 'MOTOR_SPEEDS'
PIMESSAGE_RESETBAROREFERENCE = 'RESET_BARO'
PIMESSAGE_ULTRAMODE = 'ULTRA_MODE'






#ARDUINO MESSAGES
ARDUINOSTATUS_DATA = 'DATA'
ARDUINOSTATUS_ERROR = 'Error'
ARDUINOSTATUS_ULTRASOUND_DATA = 'Ultrasound_data'
ARDUINOSTATUS_ULTRASOUND_COLLISION = 'Ultrasound_Object'

#FLIGHT
TAKEOFF_PREFERED_ALTITUDE = 150
MAX_ROLL = 35.0
MAX_PITCH = 35.0
YPR_STATIONARY = [0.0,0.0,0.0,0.0]
MOTOR_MAX = 2000
MOTOR_MIN = 1000
REFRESH_PID_TIME = 1

KP_NORMAL = 2
KD_NORMAL = 1
KI_NORMAL = 1

KP_ALTITUDE = 3
KD_ALTITUDE = 1
KI_ALTITUDE = 1

KP_FLIGHTMODE = 5
KD_FLIGHTMODE = 1
KI_FLIGHTMODE = 1
import socket

# CONTROL VARIABLES
ENABLE_FLASK_LOGGING = False
ENABLE_FLASK_DEBUG_MODE = True
ENABLE_BONJOUR_REGISTER = True
ENABLE_SERIAL = False
ENABLE_PID = False

# SOCKET-IO
SOCKETIO_NAMESPACE = '/test'

# SERVER INFO
SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5000

# LOGGING CONSTANTS
LOG_LOCATION_FLASK = "~/Desktop"
LOG_FILENAME_FLASK = "FlaskLog.log"
LOG_FORMAT_FLASK = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
LOG_LOCATION_APP = "/Users/Shyam/Desktop"
LOG_FILENAME_APP = "Quadcopter.log"
LOG_FORMAT_APP = "%(asctime)s %(name)s %(levelname)s : %(message)s"

# BONJOUR SERVICE INFO

BONJOUR_TYPE = "_http._tcp.local."
BONJOUR_NAME = "quad"
BONJOUR_DESC = {'Project_By': 'Shyam, Jo, Anirudh, Kaushik'}
BONJOUR_SERVICE_NAME = "dont-have-a-server-socool.local."
BONJOUR_REPLACEMENT_STATICIP = "0.0.0.0"
BONJOUR_WEIGHT = 0
BONJOUR_PRIORITY = 0

# PYSERIAL
# ARDUINO_PORT = '/dev/tty.usbserial'
ARDUINO_PORT = '/dev/cu.usbmodem1421'
ARDUINO_BAUDRATE = 115200

# IOS COMMANDS RECEIVED
IOSMESSAGE_TAKEOFF = 'TAKEOFF'
IOSMESSAGE_LAND = 'LAND'
IOSMESSAGE_SETSPEED = 'SET_SPEED'
IOSMESSAGE_HOVER = 'MODE_HOVER'
IOSMESSAGE_HOLDALTITUDE = 'MODE_ALTITUDE_HOLD'
IOSMESSAGE_SETYPR = 'SET_YPR'
IOSMESSAGE_ERROR = "ERROR"
IOSMESSAGE_FLIGHTMODE = "MODE_FLIGHT"

# PI COMMANDS
PIMESSAGE_SETSPEEDS = 'MOTOR_SPEEDS'
PIMESSAGE_RESETBAROREFERENCE = 'RESET_BARO'
PIMESSAGE_ULTRAMODE = 'ULTRA_MODE'

# ARDUINO MESSAGES
ARDUINOMESSAGE_MOTOR = 'MOTOR'
ARDUINOMESSAGE_GYRO = 'GYROMAG'
ARDUINOMESSAGE_ALTITUDE = 'ALTITUDE'
ARDUINOSTATUS_SETUP_INITIALIZING = 'SETUP_INITIALIZING'
ARDUINOSTATUS_SETUP_SUCCESS = 'SETUP_SUCCESS'
ARDUINOSTATUS_SETUP_FAILURE = 'SETUP_FAILURE'
ARDUINOSTATUS_SETUP_ERRORCODE = 'SETUP_ERRORCODE'
ARDUINOSTATUS_SETUP_MESSAGE = 'SETUP_MESSAGE'
ARDUINOSTATUS_ULTRA_F = 'ULTRA_F'
ARDUINOSTATUS_ULTRA_ALL = 'ULTRA_ALL'
ARDUINOSTATUS_ULTRA_L = 'ULTRA_L'
ARDUINOSTATUS_ULTRA_R = 'ULTRA_R'
ARDUINOSTATUS_ULTRA_T = 'ULTRA_T'

# FLIGHT
TAKEOFF_PREFERED_ALTITUDE = 25.0
MAX_ROLL = 35.0
MAX_PITCH = 35.0
YPR_STATIONARY = [0.0, 0.0, 0.0, 0.0]
MOTOR_MAX = 2000
MOTOR_MIN = 1000
ULTRASOUND_TOWINGTIP_OFFSET = 25

# YAW : Determine wing rotation direction
WING_FR_ANTICLOCKWISE = True

REFRESH_PID_TIME = 1

KP_NORMAL = 0.3
KD_NORMAL = 0.1
KI_NORMAL = 0

KP_ALTITUDE = 0.3
KD_ALTITUDE = 0
KI_ALTITUDE = 0

KP_FLIGHTMODE = 0.3
KD_FLIGHTMODE = 0
KI_FLIGHTMODE = 0

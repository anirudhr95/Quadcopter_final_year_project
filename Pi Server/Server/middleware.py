import constants
from customlogger import arduino_logger, ios_logger


class Middleware_IOS:
    """
    Class for processing messages from IOS devices
    """

    def __init__(self, quadcopter):
        """
        Doesnt require a message handler, because the quadcopter_worker thread handles sending messages to arduino
        :param quadcopter:
        """

        self.quadcopter = quadcopter
        self.logger = ios_logger()

    def parseMessage(self, msg):
        if ':' in msg:
            functionName, params = msg.split(':')
            if functionName == constants.IOSMESSAGE_SETSPEED:
                self.logger.set_Speed(params)
                self.quadcopter.set_speed(float(params))
            elif functionName == constants.IOSMESSAGE_SETYPR:
                self.logger.set_ypr(params)
                params = map(lambda x: float(x), params.split(";"))
                self.quadcopter.set_ypr_desired(params)
            elif functionName == constants.IOSMESSAGE_HOLDALTITUDE:

                if int(params) == 1:
                    self.logger.altitude_hold(1)
                    self.quadcopter.set_mode_altitude_hold_enable()
                else:
                    self.logger.altitude_hold(0)
                    self.quadcopter.set_mode_altitude_hold_disable()

            elif functionName == constants.IOSMESSAGE_ERROR:
                self.logger.error(params)

        else:
            # Message is a single line command

            if msg == constants.IOSMESSAGE_HOVER:
                self.logger.hover()
                self.quadcopter.set_mode_hover_enable()
            elif msg == constants.IOSMESSAGE_LAND:
                self.logger.land()
                self.quadcopter.land()
            elif msg == constants.IOSMESSAGE_TAKEOFF:
                self.logger.takeoff()
                self.quadcopter.takeoff()
            else:
                self.logger.error(msg)


class Middleware_Arduino:
    """
    Class for processing messages from Arduino
    Possible Messages :

    const char* FORMAT_SETUP_INIT = "SETUP_INITIALIZING:%s\n"; //(MOTOR/GYRO)
    const char* FORMAT_SETUP_SUCCESS = "SETUP_SUCCESS:%s\n"; // (MOTOR/GYRO)
    const char* FORMAT_SETUP_FAILURE = "SETUP_FAILURE:%s\n"; // (MOTOR/GYRO)
    const char* FORMAT_SETUP_ERRORCODE = "SETUP_ERRORCODE:%d\n"; // (MOTOR/GYRO)
    const char* FORMAT_SETUP_MESSAGE = "SETUP_MESSAGE:%s\n"; // (MESSAGE)
    // MOTORS
    const char* FORMAT_MOTOR_SPEEDS = "MOTOR:%d;%d;%d;%d\n"; // MOTOR SPEEDS
    // GYRO+MAG
    const char* FORMAT_GYROMAG = "GYROMAG:%d;%d;%d;%d\n"; //YPR,MAG(x,y,z),heading
    // ULTRASOUND
    const char* FORMAT_ULTRA_ALL = "ULTRA:%d;%d;%d;%d;%d\n";
    """

    def __init__(self, quadcopter):

        self.quadcopter = quadcopter
        self.logger = arduino_logger()
        self.flag = False
    def parseMessage(self, msg):
        try:

            functionName, params = msg.split(':')
            if functionName == constants.ARDUINOMESSAGE_GYRO:

                # DATA:Y;P;R;Mx;My;Mz;Mh

                y, p, r, heading = map(lambda x: float(x), params.split(';'))
                self.logger.data_gyromag(gyro=[y,p,r],heading=heading)
                self.quadcopter.set_ypr_current([y, p, r])

            elif functionName == constants.ARDUINOSTATUS_ULTRA:
                self.logger.data_ultrasound(params.split(';'))
                # ORDER: BOTTOM, TOP, FRONT, RIGHT, LEFT
                bottom,top,front,right,left = map(lambda x: float(x), params.split(';'))
                self.quadcopter.set_sensor_altitude_current(bottom)
                self.quadcopter.set_sensor_ultra_values(front=front, left=left, right=right, top=top)

            elif functionName == constants.ARDUINOMESSAGE_MOTOR:
                self.logger.data_motor_speeds(params.split(';'))
            elif functionName == constants.ARDUINOSTATUS_SETUP_INITIALIZING:
                self.logger.setup_init(params)
            elif functionName == constants.ARDUINOSTATUS_SETUP_SUCCESS:
                self.logger.setup_success(params)
            elif functionName == constants.ARDUINOSTATUS_SETUP_FAILURE:
                self.logger.setup_failure(params)
            elif functionName == constants.ARDUINOSTATUS_SETUP_ERRORCODE:
                self.logger.setup_errorcode(params)
            elif functionName == constants.ARDUINOSTATUS_SETUP_MESSAGE:
                self.logger.setup_message(params)
            elif functionName == "SETUP COMPLETED":
                return True
            return False

        except ValueError as e:
            print e

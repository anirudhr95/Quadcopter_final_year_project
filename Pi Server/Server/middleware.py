import Constants
from CustomLogger import ArduinoLogger, IOSLogger


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
        self.logger = IOSLogger()

    def parseMessage(self, msg):
        if ':' in msg:
            functionName, params = msg.split(':')
            if functionName == Constants.IOSMESSAGE_SETSPEED:
                self.logger.set_Speed(params)
                self.quadcopter.set_speed(float(params))
            elif functionName == Constants.IOSMESSAGE_SETYPR:
                self.logger.set_ypr(params)
                params = map(lambda x: float(x), params.split(";"))
                self.quadcopter.set_YPR_Desired(params)
            elif functionName == Constants.IOSMESSAGE_HOLDALTITUDE:

                if int(params) == 1:
                    self.logger.altitude_hold(1)
                    self.quadcopter.mode_Altitude_Hold_Enable()
                else:
                    self.logger.altitude_hold(0)
                    self.quadcopter.mode_Altitude_Hold_Disable()

            elif functionName == Constants.IOSMESSAGE_ERROR:
                self.logger.error(params)

        else:
            # Message is a single line command

            if msg == Constants.IOSMESSAGE_HOVER:
                self.logger.hover()
                self.quadcopter.mode_Hover_Enable()
            elif msg == Constants.IOSMESSAGE_LAND:
                self.logger.land()
                self.quadcopter.land()
            elif msg == Constants.IOSMESSAGE_TAKEOFF:
                self.logger.takeoff()
                self.quadcopter.takeoff()


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
    const char* FORMAT_GYROMAG = "GYROMAG:%d;%d;%d;%d;%d;%d;%d\n"; //YPR,MAG(x,y,z),heading
    // ULTRASOUND

    const char* FORMAT_ULTRA_F = "ULTRA_F:%d\n";
    const char* FORMAT_ULTRA_ALL = "ULTRA_ALL:%d;%d;%d;%d\n";
    const char* FORMAT_ULTRA_L = "ULTRA_L:%d\n";
    const char* FORMAT_ULTRA_R = "ULTRA_R:%d\n";
    const char* FORMAT_ULTRA_T = "ULTRA_T:%d\n";

    const char* FORMAT_BARO = "ALTITUDE:%d\n";
    """

    def __init__(self, quadcopter):
        self.quadcopter = quadcopter
        self.logger = ArduinoLogger()

    def parseMessage(self, msg):
        try:
            functionName, params = msg.split(':')
            if functionName == Constants.ARDUINOMESSAGE_GYRO:
                # DATA:Y;P;R;Mx;My;Mz;Mh

                y, p, r, mx, my, mz, heading, = map(lambda x: float(x), params.split(';'))
                self.logger.data_gyromag(gyro=[y,p,r],heading=heading,mag=[mx,my,mz])
                self.quadcopter.sensor_set_YPR_Current([y, p, r])

            elif functionName == Constants.ARDUINOMESSAGE_ALTITUDE:
                self.quadcopter.sensor_set_Altitude_Current(float(params))
            elif functionName == Constants.ARDUINOMESSAGE_MOTOR:
                self.logger.data_motor_speeds(params)
            elif functionName == Constants.ARDUINOSTATUS_SETUP_INITIALIZING:
                self.logger.setup_init(params)
            elif functionName == Constants.ARDUINOSTATUS_SETUP_SUCCESS:
                self.logger.setup_success(params)
            elif functionName == Constants.ARDUINOSTATUS_SETUP_FAILURE:
                self.logger.setup_failure(params)
            elif functionName == Constants.ARDUINOSTATUS_SETUP_ERRORCODE:
                self.logger.setup_errorcode(params)
            elif functionName == Constants.ARDUINOSTATUS_SETUP_MESSAGE:
                self.logger.setup_message(params)
            elif functionName == Constants.ARDUINOSTATUS_ULTRA_F:
                self.logger.data_ultrasound(functionName, params)
            elif functionName == Constants.ARDUINOSTATUS_ULTRA_ALL:
                self.logger.data_ultrasound(functionName, params)
            elif functionName == Constants.ARDUINOSTATUS_ULTRA_L:
                self.logger.data_ultrasound(functionName, params)
            elif functionName == Constants.ARDUINOSTATUS_ULTRA_R:
                self.logger.data_ultrasound(functionName, params)
            elif functionName == Constants.ARDUINOSTATUS_ULTRA_T:
                self.logger.data_ultrasound(functionName, params)
        except ValueError as e:
            print e

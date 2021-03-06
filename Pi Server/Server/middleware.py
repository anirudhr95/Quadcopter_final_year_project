import Constants
from CustomLogger import arduino_logger, ios_logger

class Middleware:
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
        self.arduinologger = arduino_logger()
        self.ioslogger = ios_logger()
        self.flag = False

    def ready(self):
        return self.flag
    def parseMessage(self, msg):
        try:
            # from quadcopterComponents import Quadcopter
            # self.quadcopter = Quadcopter()
            if ':' in msg:
                functionName, params = msg.split(':')
                if functionName == Constants.IOSMESSAGE_SETSPEED:
                    self.ioslogger.set_Speed(params)
                    self.quadcopter.motor.set_speed(float(params))
                elif functionName == Constants.IOSMESSAGE_SETYPR:
                    self.ioslogger.set_ypr(params)
                    params = map(lambda x: float(x), params.split(";"))
                    self.quadcopter.gyro.set_ypr_desired(params)
                elif functionName == Constants.IOSMESSAGE_HOLDALTITUDE:

                    if int(params) == 1:
                        self.ioslogger.altitude_hold(1)
                        self.quadcopter.set_mode_altitude_hold_enable()
                    else:
                        self.ioslogger.altitude_hold(0)
                        self.quadcopter.set_mode_altitude_hold_disable()

                elif functionName == Constants.IOSMESSAGE_ERROR:
                    self.ioslogger.error(params)
                elif functionName == Constants.ARDUINOMESSAGE_GYRO:
                    # DATA:Y;P;R;Mx;My;Mz;Mh
                    y, p, r, heading = map(lambda x: float(x), params.split(';'))
                    self.arduinologger.data_gyromag(gyro=[y, p, r], heading=heading)
                    self.quadcopter.gyro.set_ypr_current([y, p, r])

                elif functionName == Constants.ARDUINOSTATUS_ULTRA:
                    self.arduinologger.data_ultrasound(params.split(';'))
                    # ORDER: BOTTOM, TOP, FRONT, RIGHT, LEFT
                    bottom, top, front, right, left = map(lambda x: float(x), params.split(';'))
                    self.quadcopter.altitude.set_sensor_altitude_current(bottom)
                    self.quadcopter.ultra.set_sensor_ultra_values(front=front, left=left, right=right, top=top)

                elif functionName == Constants.ARDUINOMESSAGE_MOTOR:
                    self.arduinologger.data_motor_speeds(params.split(';'))
                elif functionName == Constants.ARDUINOSTATUS_SETUP_INITIALIZING:
                    self.arduinologger.setup_init(params)
                elif functionName == Constants.ARDUINOSTATUS_SETUP_SUCCESS:
                    self.arduinologger.setup_success(params)
                elif functionName == Constants.ARDUINOSTATUS_SETUP_FAILURE:
                    self.arduinologger.setup_failure(params)
                elif functionName == Constants.ARDUINOSTATUS_SETUP_ERRORCODE:
                    self.arduinologger.setup_errorcode(params)
                elif functionName == Constants.ARDUINOSTATUS_SETUP_MESSAGE:
                    self.arduinologger.setup_message(params)
                elif functionName == "SETUP COMPLETED":
                    self.flag = True
                    return True

            else:
                # Message is a single line command

                if msg == Constants.IOSMESSAGE_HOVER:
                    self.ioslogger.hover()
                    self.quadcopter.set_mode_hover_enable()
                elif msg == Constants.IOSMESSAGE_LAND:
                    self.ioslogger.land()
                    self.quadcopter.land()
                elif msg == Constants.IOSMESSAGE_TAKEOFF:
                    self.ioslogger.takeoff()
                    self.quadcopter.takeoff()
                else:
                    self.ioslogger.error(msg)

            return False

        except ValueError as e:
            print e

# PID PID_motor_Yaw_FR(&ypr_current[0], &MotorSpeeds[0], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Yaw_FL(&ypr_current[0], &MotorSpeeds[1], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Yaw_BR(&ypr_current[0], &MotorSpeeds[2], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Yaw_BL(&ypr_current[0], &MotorSpeeds[3], &ypr_desired[0], Kp, Ki, Kd, REVERSE);
#
# // PITCH
# PID PID_motor_Pitch_FR(&ypr_current[1], &MotorSpeeds[0], &ypr_desired[1], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Pitch_FL(&ypr_current[1], &MotorSpeeds[1], &ypr_desired[1], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Pitch_BR(&ypr_current[1], &MotorSpeeds[2], &ypr_desired[1], Kp, Ki, Kd, DIRECT);
# PID PID_motor_Pitch_BL(&ypr_current[1], &MotorSpeeds[3], &ypr_desired[1], Kp, Ki, Kd, DIRECT);
# // ROLL
# PID PID_motor_Roll_FR(&ypr_current[2], &MotorSpeeds[0], &ypr_desired[2], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Roll_FL(&ypr_current[2], &MotorSpeeds[1], &ypr_desired[2], Kp, Ki, Kd, DIRECT);
# PID PID_motor_Roll_BR(&ypr_current[2], &MotorSpeeds[2], &ypr_desired[2], Kp, Ki, Kd, REVERSE);
# PID PID_motor_Roll_BL(&ypr_current[2], &MotorSpeeds[3], &ypr_desired[2], Kp, Ki, Kd, DIRECT);
#
# // Commented until Barometer is obtained
# // ALTITUDE
# PID PID_motor_Altitude_FR(&altitude_current, &MotorSpeeds[0], &altitude_desired, Kp, Ki, Kd, REVERSE);
# PID PID_motor_Altitude_FL(&altitude_current, &MotorSpeeds[1], &altitude_desired, Kp, Ki, Kd, REVERSE);
# PID PID_motor_Altitude_BR(&altitude_current, &MotorSpeeds[2], &altitude_desired, Kp, Ki, Kd, REVERSE);
# PID PID_motor_Altitude_BL(&altitude_current, &MotorSpeeds[3], &altitude_desired, Kp, Ki, Kd, REVERSE);
import Constants
from GY_86 import GY_86
from PID import PID


class Quadcopter:
    def __init__(self):
        self.should_hold_altitude = True
        self.altitudes = {'current':0,
                          'desired':0}
        self.should_stabilize = False
        self.motor_Speeds = [0, 0, 0, 0]
        self.ypr = {'current' : [0.0, 0.0, 0.0],
                    'desired' : [0.0, 0.0, 0.0]}

        self.heading_current = 0
        self.sensor = GY_86()

        self.PID_YAW = [PID()]

    def takeoff(self):
        self.set_Mode_Hover(Constants.TAKEOFF_PREFERED_ALTITUDE)

    def land(self):
        self.set_Mode_Altitude_Hold(0.0)

    def set_Mode_Altitude_Hold(self, height=None):
        self.should_hold_altitude = True
        self.altitudes['current'] = self.sensor.get_altitude()
        self.altitudes['desired'] = height if height else self.altitudes['current']

    def remove_Altitude_Hold(self):
        self.should_hold_altitude = False

    def set_Speed(self, speed):
        self.__set_Speeds__([speed for i in range(4)])

    def __set_Speeds__(self, speeds):
        # TODO Send Arduino New Height
        pass

    def __refresh_YPR__(self):
        self.ypr['current'] = self.sensor.get_ypr()

    def __refresh_Altitude__(self):
        self.altitudes['current'] = self.sensor.get_altitude()

    def __refresh_Heading__(self):
        self.heading_current = self.sensor.get_heading()

    def __compute__(self):
        """
        Modifies motor speeds
        """

        pass

    def refresh(self):
        """
        :returns Motorspeeds: The new motor speeds to set
        """
        self.__refresh_YPR__()
        self.__refresh_Altitude__()
        self.__refresh_Heading__()
        return self.__compute__()

    def set_Mode_Flight(self, hold_altitude=True):
        self.should_stabilize = False
        self.should_hold_altitude = hold_altitude

    def set_Mode_Hover(self, height=None):
        self.should_stabilize = True
        self.__set_YPR_Desired(Constants.YPR_STATIONARY)
        self.set_Mode_Altitude_Hold(height)

    def __check_YPR_Goodness(self, ypr):
        return ypr[1] <= Constants.MAX_PITCH and ypr[2] <= Constants.MAX_ROLL

    def get_ypr_current(self):
        return self.ypr['current']


    def __set_YPR_Desired(self, ypr):
        if self.__check_YPR_Goodness(ypr):
            self.ypr['desired'] = ypr
            return True
        else:
            return False

    def set_YPR(self, ypr):

        if self.__set_YPR_Desired(ypr):
            self.set_Mode_Flight()
        else:
            self.set_Mode_Hover()

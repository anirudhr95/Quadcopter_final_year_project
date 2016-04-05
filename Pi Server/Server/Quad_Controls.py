import Constants
from GY_86 import GY_86
from PID import PID


class Quadcopter:
    def __init_PID__(self):
        """
        Tilt forward = +ve pitch
        Tilt left = +ve roll
        """

        self.PID_YAW_FR = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=0,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_YAW_FL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=1,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_YAW_BR = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=2,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_YAW_BL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=3,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_PITCH_FR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=0,
                                Kp=Constants.Kp,
                                Kd=Constants.Kd,
                                Ki=Constants.Ki,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=True
                                )
        self.PID_PITCH_FL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=1,
                                Kp=Constants.Kp,
                                Kd=Constants.Kd,
                                Ki=Constants.Ki,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=True
                                )
        self.PID_PITCH_BR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=2,
                                Kp=Constants.Kp,
                                Kd=Constants.Kd,
                                Ki=Constants.Ki,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=False
                                )
        self.PID_PITCH_BL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=3,
                                Kp=Constants.Kp,
                                Kd=Constants.Kd,
                                Ki=Constants.Ki,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=False
                                )
        self.PID_ROLL_FR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=0,
                               Kp=Constants.Kp,
                               Kd=Constants.Kd,
                               Ki=Constants.Ki,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ROLL_FL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=1,
                               Kp=Constants.Kp,
                               Kd=Constants.Kd,
                               Ki=Constants.Ki,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=True
                               )
        self.PID_ROLL_BR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=0,
                               Kp=Constants.Kp,
                               Kd=Constants.Kd,
                               Ki=Constants.Ki,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ROLL_BL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=0,
                               Kp=Constants.Kp,
                               Kd=Constants.Kd,
                               Ki=Constants.Ki,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ALT_FR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=0,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_FL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=1,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_BR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=2,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_BL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=3,
                              Kp=Constants.Kp,
                              Kd=Constants.Kd,
                              Ki=Constants.Ki,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )

    def __init__(self):
        self.should_hold_altitude = True
        self.altitudes = {'current': 0,
                          'desired': 0}
        self.should_stabilize = False
        self.should_change_yaw = False
        self.motor_Speeds = [0, 0, 0, 0]
        self.ypr = {'current': [0.0, 0.0, 0.0],
                    'desired': [0.0, 0.0, 0.0]}

        self.heading_current = 0
        self.sensor = GY_86()

        self.__init_PID__()
        print 'Initialized Quadcopter'

    def takeoff(self):
        self.set_Mode_Hover(Constants.TAKEOFF_PREFERED_ALTITUDE)

    def land(self):
        self.set_Mode_Altitude_Hold(0.0)

    def set_Mode_Altitude_Hold(self, height=None):
        self.should_hold_altitude = True
        # TODO Fix Altitude Algorithm (Getting None Value)
        self.altitudes['current'] = self.sensor.get_altitude()
        self.altitudes['desired'] = height if height else self.altitudes['current']

    def set_Mode_Rotate(self):
        self.should_change_yaw = True

    def remove_Mode_Rotate(self):
        self.should_change_yaw = False

    def remove_Altitude_Hold(self):
        self.should_hold_altitude = False

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
        # self.refresh()
        if not self.should_change_yaw:
            self.PID_YAW_FR.compute()
            self.PID_YAW_FL.compute()
            self.PID_YAW_BR.compute()
            self.PID_YAW_BL.compute()

        if self.should_stabilize:
            self.PID_PITCH_FR.compute()
            self.PID_PITCH_FL.compute()
            self.PID_PITCH_BR.compute()
            self.PID_PITCH_BL.compute()

            self.PID_ROLL_FR.compute()
            self.PID_ROLL_FL.compute()
            self.PID_ROLL_BR.compute()
            self.PID_ROLL_BL.compute()
        if self.should_hold_altitude:
            self.PID_ALT_FR.compute()
            self.PID_ALT_FL.compute()
            self.PID_ALT_BR.compute()
            self.PID_ALT_BL.compute()
        return self.motor_Speeds

    def refresh(self):
        """
        :returns Motorspeeds: The new motor speeds to set
        """

        # TODO UNCOMMENT BEFORE HOSTING IN SERVER
        if not Constants.TESTING_MODE:
            self.__refresh_YPR__()
            self.__refresh_Altitude__()
            self.__refresh_Heading__()
        return self.__compute__()

    def set_Mode_Flight(self, hold_altitude=True):
        self.should_stabilize = False
        self.should_hold_altitude = hold_altitude

    def set_Mode_Hover(self, height=None):
        self.should_stabilize = True
        self.__set_YPR_Desired__(Constants.YPR_STATIONARY)
        self.set_Mode_Altitude_Hold(height)

    def __check_YPR_Goodness(self, ypr):
        return ypr[1] <= Constants.MAX_PITCH and ypr[2] <= Constants.MAX_ROLL

    def get_ypr_current(self):
        return self.ypr['current']
    def set_speed(self,height):
        self.set_Mode_Hover(height)
    def __set_YPR_Desired__(self, ypr):
        if self.__check_YPR_Goodness(ypr):
            self.ypr['desired'] = ypr
            return True
        else:
            return False

    def set_YPR(self, ypr):

        if self.__set_YPR_Desired__(ypr):
            self.set_Mode_Flight()
        else:
            self.set_Mode_Hover()


def test_quadcopter():
    a= Quadcopter()
    a.set_YPR([0, 20.0, 0])
    a.should_stabilize = True
    a.should_hold_altitude = False

    for i in range(20):
        a.refresh()
        print a.get_ypr_current(),a.refresh()
        a.ypr['current'][1]+=2

    print 'Decreasing PITCH'
    for i in range(20):
        a.refresh()
        print a.get_ypr_current(), a.refresh()
        a.ypr['current'][1] -= 3

test_quadcopter()


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
        self.__init_PID__()
        print 'Initialized Quadcopter'

    def takeoff(self):
        print 'Takeoff Mode On'
        self.set_Mode_Hover(Constants.TAKEOFF_PREFERED_ALTITUDE)

    def land(self):
        print 'Land Mode On'
        self.set_Mode_Altitude_Hold(0.0)

    def set_Mode_Altitude_Hold(self, height=None):
        print 'Altitude Hold Mode On at height : ' + height
        self.should_hold_altitude = True
        # TODO Fix Altitude Algorithm (Getting None Value)
        self.altitudes['current'] = self.altitudes['current']
        self.altitudes['desired'] = height if height else self.altitudes['current']

    def set_Mode_Rotate(self):
        self.should_change_yaw = True

    def remove_Mode_Rotate(self):
        self.should_change_yaw = False

    def remove_Altitude_Hold(self):
        print 'Altitude Hold Mode Off'
        self.should_hold_altitude = False

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

        print 'Motor Speeds : ', self.motor_Speeds
        return self.motor_Speeds

    def refresh(self):
        """
        :returns Motorspeeds: The new motor speeds to set
        """
        return self.__compute__()

    def set_Mode_Flight(self, hold_altitude=True):
        print 'Flight Mode On'
        self.should_stabilize = True
        self.should_hold_altitude = hold_altitude

    def set_Mode_Hover(self, height=None):
        print 'Hover Mode On'
        self.should_stabilize = True
        self.__set_YPR_Desired__(Constants.YPR_STATIONARY)
        self.set_Mode_Altitude_Hold(height)

    def __check_YPR_Goodness(self, ypr):
        return ypr[1] <= Constants.MAX_PITCH and ypr[2] <= Constants.MAX_ROLL

    def set_current_ypr(self, ypr):
        self.ypr['current'] = ypr
    def set_current_altitude(self,altitude):
        self.altitudes['current'] = altitude

    def set_heading(self, heading):
        self.heading_current = heading

    def get_ypr_current(self):
        return self.ypr['current']

    def set_speed(self, speed):
        val = [self.motor_Speeds[i]-min(self.motor_Speeds) for i in range(4)]
        self.motor_Speeds = [val[i] + speed for i in range(4)]

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


if __name__ == '__main__':
    a = Quadcopter()
    a.set_YPR([0, 20.0, 10.0])
    a.should_stabilize = True
    a.should_hold_altitude = False

    for i in range(20):
        a.refresh()
        print a.get_ypr_current(), a.refresh()
        a.ypr['current'][1] += 2
        a.ypr['current'][2] += 1

    print 'Decreasing PITCH'
    for i in range(20):
        a.refresh()
        print a.get_ypr_current(), a.refresh()
        a.ypr['current'][1] -= 3
        a.ypr['current'][2] -= 0.5

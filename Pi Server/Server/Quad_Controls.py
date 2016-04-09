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
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_YAW_FL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=1,
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_YAW_BR = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=2,
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_YAW_BL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=3,
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_PITCH_FR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=0,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=True
                                )
        self.PID_PITCH_FL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=1,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=True
                                )
        self.PID_PITCH_BR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=2,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=False
                                )
        self.PID_PITCH_BL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=3,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX,
                                min=Constants.MOTOR_MIN,
                                reverse_direction=False
                                )
        self.PID_ROLL_FR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=0,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ROLL_FL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=1,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=True
                               )
        self.PID_ROLL_BR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=0,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ROLL_BL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=0,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX,
                               min=Constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ALT_FR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=0,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_FL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=1,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_BR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=2,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_BL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=3,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX,
                              min=Constants.MOTOR_MIN,
                              reverse_direction=False
                              )

    def __init__(self, pi_logger):
        self.logger = pi_logger
        self.should_hold_altitude = True
        self.should_change_yaw = False

        self.__is_mode_Hover__ = True

        self.altitudes = {'current': 0,
                          'desired': 0}
        self.motor_Speeds = [Constants.MOTOR_MIN, Constants.MOTOR_MIN, Constants.MOTOR_MIN, Constants.MOTOR_MIN]
        self.ypr = {'current': [0.0, 0.0, 0.0],
                    'desired': [0.0, 0.0, 0.0]}
        self.__init_PID__()
        self.__PIDS__ = [self.PID_PITCH_FR,
                         self.PID_PITCH_FL,
                         self.PID_PITCH_BR,
                         self.PID_PITCH_BL,
                         self.PID_ROLL_FR,
                         self.PID_ROLL_FL,
                         self.PID_ROLL_BR,
                         self.PID_ROLL_BL
                         ]

    def takeoff(self):
        self.logger.mode_Takeoff()
        self.mode_Hover_Enable(Constants.TAKEOFF_PREFERED_ALTITUDE)

    def land(self):
        self.logger.mode_Land()
        self.mode_Altitude_Hold_Enable(0.0)


    def mode_Altitude_Hold_Enable(self, height=None):
        if not self.is_mode_Altitude_Hold():
            self.logger.mode_altitude_hold(1)
            self.should_hold_altitude = True
            # TODO Fix Altitude Algorithm (Getting None Value)
            if height:
                self.set_Altitude_Desired(height)
            else:
                self.set_Altitude_Desired(self.get_Altitude_Current())

    def mode_Altitude_Hold_Disable(self):
        if self.is_mode_Altitude_Hold():
            self.logger.mode_altitude_hold(0)
            self.should_hold_altitude = False

    # def mode_Rotate_Enable(self):
    #     self.should_change_yaw = True
    #
    # def mode_rotate_Disable(self):
    #     self.should_change_yaw = False

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

        self.logger.data_set_speeds(self.motor_Speeds)
        return self.motor_Speeds

    def refresh(self):
        """
        :returns Motorspeeds: The new motor speeds to set
        """
        return self.__compute__()

    def __mode_Flight_SET_PID__(self):
        for PID in self.__PIDS__:
            PID.change_pid(Constants.KP_FLIGHTMODE, Constants.KI_FLIGHTMODE, Constants.KD_NORMAL)

    def __mode_Hover_SET_PID_(self):
        for PID in self.__PIDS__:
            PID.change_pid(Constants.KP_NORMAL, Constants.KI_NORMAL, Constants.KD_NORMAL)

    def mode_Flight_Enable(self, hold_altitude=True):
        if not self.is_mode_Flight():
            self.logger.mode_flight()
            if hold_altitude:
                self.mode_Altitude_Hold_Enable()
            else:
                self.mode_Altitude_Hold_Disable()
            self.__mode_Flight_SET_PID__()
            self.__is_mode_Hover__ = False

    def mode_Hover_Enable(self, height=None):
        if not self.is_mode_Hover():
            self.logger.mode_hover()
            self.set_YPR_Desired(Constants.YPR_STATIONARY)
            self.mode_Altitude_Hold_Enable(height)
            self.__mode_Hover_SET_PID_()
            self.__is_mode_Hover__ = True

    def is_mode_Hover(self):
        return self.__is_mode_Hover__

    def is_mode_Altitude_Hold(self):
        return self.should_hold_altitude

    def is_mode_Flight(self):
        return not self.__is_mode_Hover__

    def __check_YPR_Goodness(self, ypr):
        return (ypr[1] <= Constants.MAX_PITCH and ypr[1] >= -Constants.MAX_PITCH) \
               and (ypr[2] <= Constants.MAX_ROLL and ypr[2] >= -Constants.MAX_ROLL)

    def get_YPR_Current(self):
        return self.ypr['current']

    def sensor_set_YPR_Current(self, ypr):
        """
        Called only by sensors
        :param ypr:
        :return:
        """
        self.ypr['current'] = ypr

    def get_YPR_Desired(self):
        return self.ypr['desired']

    def set_YPR_Desired(self, ypr):
        self.logger.data_set_ypr(ypr)
        if self.__check_YPR_Goodness(ypr):
            self.ypr['desired'] = ypr
            self.mode_Flight_Enable()
            return True
        else:
            # TODO Check
            self.logger.error("DESIRED YPR UNSUITABLE : %s" % ypr)
            self.mode_Hover_Enable()
            return False

    def sensor_set_Altitude_Current(self, altitude):
        """
        Should be called only by sensors.. Use set_altitude_desired for moving quad
        :param altitude:
        :return:
        """
        self.altitudes['current'] = altitude

    def get_Altitude_Current(self):
        return self.altitudes['current']

    def set_Altitude_Desired(self, altitude):
        self.logger.data_set_altitude(altitude)
        self.altitudes['desired'] = altitude

    def get_Altitude_Desired(self):
        return self.altitudes['desired']

    def set_speed(self, speed):
        self.logger.data_set_speeds([speed for i in range(4)])
        val = [self.motor_Speeds[i] - min(self.motor_Speeds) for i in range(4)]
        self.motor_Speeds = [val[i] + speed for i in range(4)]


if __name__ == '__main__':
    import CustomLogger
    a = Quadcopter(CustomLogger.PILogger())
    a.set_YPR_Desired([0, 20.0, 10.0])
    a.mode_Altitude_Hold_Enable()

    for i in range(20):
        a.refresh()
        print a.get_YPR_Current(), a.refresh()
        # INCREASE YPR BY [0,2,1]
        a.sensor_set_YPR_Current([x+y for x,y in zip(a.get_YPR_Current(),[0,2,1])])


    print 'Decreasing PITCH, setting hover mode'
    a.mode_Hover_Enable()
    for i in range(20):
        a.refresh()
        print a.get_YPR_Current(), a.refresh()
        a.sensor_set_YPR_Current([x + y for x, y in zip(a.get_YPR_Current(), [0, -3, -0.5])])

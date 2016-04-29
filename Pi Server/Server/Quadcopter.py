import constants
from pid import PID
from quadcopterComponents import altitude, gyro, ultrasonic, pid_handler, motor


class Quadcopter:
    """
    PID UPDATES
        3 Modes :
            1) Hover : PID = NORMAL.. update pitch yaw roll altitude pids
            2) Flight : PID = FLIGHT. update pitch yaw roll altitude pids
            3) Collision : Dont update pitch, yaw.. USE ULTRASOUND PIDS corresponding to the problematic side.. Update Altitudes too
    """

    # TODO When switching from Flight mode to hover, set ypr_desired to reverse(current ypr) with high kp,ki,kd

    def __init__(self, pi_logger):
        self.logger = pi_logger
        self.should_hold_altitude = True
        self.should_change_yaw = False
        self.__is_mode_Hover__ = True
        self.__is_mode_Collision_Avoid = False
        self.__has_taken_off__ = False



        self.gyro = gyro.Gyro(self.logger)
        self.altitude = altitude.Altitude(self.logger)
        self.ultra = ultrasonic.Ultrasonic(self.logger)
        self.motor = motor.Motor(self.logger)

        self.pidhandler = pid_handler.pid_handler(logger=self.logger, altitude=self.altitude.get_altitudes(),
                                                  ultra_values=self.ultra.get_ultra_values(),
                                                  ypr=self.gyro.get_ypr(), motor_speeds=self.motor.get_speed())

    def takeoff(self):
        print '\n\nENTERED TAKEOFF'
        self.logger.mode_Takeoff()
        self.__has_taken_off__ = True
        self.set_mode_hover_enable(height=constants.TAKEOFF_PREFERED_ALTITUDE)

    def land(self):
        self.logger.mode_Land()
        self.set_mode_hover_enable(height=constants.ULTRASOUND_TOGROUND_OFFSET)

    def set_mode_collision_avoid_enable(self):
        self.__is_mode_Collision_Avoid = True

    def set_mode_collision_avoid_disable(self):
        self.__is_mode_Collision_Avoid = False

    def is_mode_collision_avoid(self):
        return self.__is_mode_Collision_Avoid

    def set_mode_altitude_hold_enable(self, height=None):
        if not self.is_mode_altitude_hold():
            self.logger.mode_altitude_hold(1)
            self.should_hold_altitude = True

        if height != None:
            self.altitude.set_altitude_desired(height)

        # TODO FIX
        else:
            self.altitude.set_altitude_desired(self.altitude.get_altitude_current())

    def set_mode_altitude_hold_disable(self):
        if self.is_mode_altitude_hold():
            self.logger.mode_altitude_hold(0)
            self.should_hold_altitude = False

    def set_mode_flight_enable(self, hold_altitude=True):
        if not self.is_mode_flight():
            self.logger.mode_flight()
            if hold_altitude:
                self.set_mode_altitude_hold_enable()
            else:
                self.set_mode_altitude_hold_disable()
            self.pidhandler.__set_pid_flight__()
            self.__is_mode_Hover__ = False

    def set_mode_hover_enable(self, height=None, disable_Altitude_Hold=False):
        """

        :param height:
        :param disable_Altitude_Hold: Used by set_speed to prevent reduction in speeds by PID
        """
        # if not self.is_mode_hover():
        self.logger.mode_hover()
        self.gyro.set_ypr_desired([self.gyro.get_ypr_current()[0], 0, 0])
        if not disable_Altitude_Hold:
            self.set_mode_altitude_hold_enable(height)
        else:
            self.set_mode_altitude_hold_disable()
        self.pidhandler.__set_pid_hover__()
        self.__is_mode_Hover__ = True

    # ALTITUDE HOLD



    def is_mode_altitude_hold(self):
        return self.should_hold_altitude

    def is_mode_flight(self):
        return not self.__is_mode_Hover__

    def __compute__(self):
        """
        Modifies motor speeds
        """
        # Check for bad angles
        # TODO: Change PID Algorithm -> If reference parameters cross threshold, modify PID to bring it under control, then set pid to normal (Useful in case of wind)

        # CHECK FOR COLLISION
        print self
        self.set_mode_collision_avoid_disable()

        for i, val in enumerate(self.ultra.get_ultra_values_current()):

            if (val != 0) and (val < constants.ULTRASOUND_SAFE_DISTANCE):
                self.set_mode_collision_avoid_enable()
                self.logger.warn_collision(i, val)
                self.pidhandler.compute_ultra(i)

        # If collision possible, return the newly computed speeds, and return result without computing other PIDs except Altitude.
        if not self.is_mode_collision_avoid():
            self.pidhandler.compute_yaw()
            self.pidhandler.compute_roll()
            self.pidhandler.compute_pitch()

        # Allow Altitude hold to ensure that quad doesnt crash into the ground
        if self.is_mode_altitude_hold():
            self.pidhandler.compute_altitude()

        # TODO: Remove this line, after testing completed. Dont use this (uses 10KB for running a 40iteration simulation)
        self.logger.data_set_speeds(self.motor.get_speed())

        # Check if land target speed reached

        # print self.motor.get_speed()
        return self.motor.get_speed()

    def __str__(self):
        return "ALTITUDES : %s,\nYPRS : %s,\nMotorSpeeds : %s\nMode:%s" % (
        self.altitude.get_altitudes(), self.gyro.get_ypr(), self.motor.get_speed(),
        {'Hover': self.is_mode_hover(),
         'AltitudeHold': self.is_mode_altitude_hold(),
         'Flight': self.is_mode_flight()})

    def has_landed(self):
        return True if not filter(lambda x: x < constants.MOTOR_MIN + 50, self.motor.get_speed()) else False

    def has_taken_off(self):
        return self.__has_taken_off__

    def refresh(self):
        """
        :returns Motorspeeds: The new motor speeds to set
        """
        # Return existing speed if takeoff command has not been given
        # print self
        if not self.has_taken_off():
            return self.motor.get_speed()
        # Compute new motor speeds
        self.__compute__()

        # if self.has_landed():
        #     self.__has_taken_off__ = False
        print self.motor.get_speed()
        return self.motor.get_speed()

    def is_mode_hover(self):
        return self.__is_mode_Hover__


def sim_ypr_change(a, ypr=None):
    """
    Simulates ypr change
    :param a:
    :return:
    """

    # a.set_sensor_altitude_current(20.0)
    # a.self.altitude.set_altitude_desired(20.0)
    a.takeoff()
    a.set_mode_altitude_hold_disable()
    if ypr:
        a.gyro.set_ypr_desired(ypr)
    else:
        a.gyro.set_ypr_desired([0, 20.0, 10.0])
    for i in range(20):
        print a.gyro.get_ypr_current(), a.refresh()
        # INCREASE YPR BY [0,2,1]
        a.gyro.set_ypr_current([x + y for x, y in zip(a.gyro.get_ypr_current(), [0, 2, 1])])

    print 'Decreasing PITCH, setting hover mode'
    a.set_mode_hover_enable()
    for i in range(20):
        print a.gyro.get_ypr_current(), a.refresh()
        a.gyro.set_ypr_current([x + y for x, y in zip(a.gyro.get_ypr_current(), [0, -3, -0.5])])


def sim_altitude(a):
    """
    Simulates takeoff and landing
    :param a:
    :return:
    """
    a.takeoff()
    for i in range(20):
        b = a.refresh()
        a.altitude.set_sensor_altitude_current(a.altitude.get_altitude_current() + 3)
        print a.altitude.get_altitudes(), b
    a.land()
    a.motor.set_speed(2000.0)
    for i in range(20):
        b = a.refresh()
        a.altitude.set_sensor_altitude_current(a.altitude.get_altitude_current() - 3)
        print a.altitude.get_altitudes(), b


def sim_ultrasound(a):
    """
    Simulates Ultrasound detection
    :param a:
    :return:
    """
    a.takeoff()
    sensor_vals = [1, 2, 3, 4]
    a.ultra.set_sensor_ultra_values(25, 60, 60, 60)
    for i in range(20):
        b = a.refresh()


if __name__ == '__main__':
    import customlogger

    a = Quadcopter(customlogger.pi_logger())
    sim_ypr_change(a)
    a = Quadcopter(customlogger.pi_logger())
    sim_altitude(a)
    a = Quadcopter(customlogger.pi_logger())
    sim_ultrasound(a)

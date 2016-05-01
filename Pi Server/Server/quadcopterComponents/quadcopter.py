import constants
from quadcopterComponents import altitude, gyro, ultrasonic, pid_handler, motor
from quadcopterComponents.mode import Mode, Flight_Status, Altitude_Hold


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

        self.current_mode = Mode.off
        self.flight_status = Flight_Status.off
        self.altitude_hold_status = Altitude_Hold.off

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

        print 'YOYO%s'%self.current_mode
        self.set_mode_hover_enable(height=constants.TAKEOFF_PREFERED_ALTITUDE)
        self.flight_status = Flight_Status.taking_off



    def land(self):
        print 'CALLED LAND'
        self.logger.mode_Land()

        self.set_mode_hover_enable(height=constants.ULTRASOUND_TOGROUND_OFFSET)
        self.flight_status = Flight_Status.landing

    def set_mode_altitude_hold_enable(self, height=None):
        print 'CALLED ALTITUDEHOLD ENABLE WITH HEIGHT %s'%height
        if self.altitude_hold_status == Altitude_Hold.off:
            self.logger.mode_altitude_hold(1)
            self.altitude_hold_status = Altitude_Hold.on

        if height is None:
            # TODO FIX
            self.altitude.set_altitude_desired(self.altitude.get_altitude_current())

        else:
            self.altitude.set_altitude_desired(height)

    def set_mode_altitude_hold_disable(self):
        print 'CALLED ALTITUDEHOLD DISABLE'
        if self.altitude_hold_status == Altitude_Hold.on:
            self.logger.mode_altitude_hold(0)
            self.altitude_hold_status = Altitude_Hold.off

    def set_mode_flight_enable(self, hold_altitude=True):
        print 'CALLED FLIGHT ENABLE'
        if self.current_mode != Mode.flight:
            self.logger.mode_flight()
            if hold_altitude:
                self.set_mode_altitude_hold_enable()
            else:
                self.set_mode_altitude_hold_disable()
            self.pidhandler.set_pid_constants_for_flight()
            self.current_mode = Mode.flight

    def set_mode_hover_enable(self, height=None, disable_Altitude_Hold=False):
        """

        :param height:
        :param disable_Altitude_Hold: Used by set_speed to prevent reduction in speeds by PID
        """
        print 'CALLED HOVER'
        # if not self.is_mode_hover():
        self.logger.mode_hover()
        self.gyro.set_ypr_desired([self.gyro.get_ypr_current()[0], 0, 0])
        if not disable_Altitude_Hold:
            self.set_mode_altitude_hold_enable(height)
        else:
            self.set_mode_altitude_hold_disable()
        self.pidhandler.set_pid_constants_for_hover()
        self.current_mode = Mode.hover

        print self

    def __str__(self):
        return str({
            "Altitudes": self.altitude.get_altitudes(),
            "YPR": self.gyro.get_ypr(),
            "Mode": self.current_mode,
            "Flight_Status": self.flight_status,
            "Altitude_Hold": self.altitude_hold_status,
            "Motor_Speeds": self.motor.get_speed(),
            "Logger": self.logger
        })

    def update_flight_status(self):
        # print "MYSTATUS : %s"%self.flight_status
        if self.flight_status != Flight_Status.off:
            if self.flight_status == Flight_Status.taking_off:
                if self.altitude.get_altitude_current() > self.altitude.get_altitude_desired():
                    self.flight_status = Flight_Status.flying
            elif self.flight_status == Flight_Status.landing:
                if filter(lambda x: x == constants.MOTOR_MIN_LANDING, self.motor.get_speed()) is None:
                    self.flight_status = Flight_Status.off
        # print "MYSTATUSAFTER : %s" % self.flight_status

    def refresh(self):
        """
        :returns Motorspeeds: The new motor speeds to set
        """
        # Return existing speed if takeoff command has not been given
        print self
        if self.flight_status == Flight_Status.off:
            return self.motor.get_speed()
        # print 'YOYOaa%s' % self.current_mode
        # Compute new motor speeds
        # Check for bad angles
        # TODO: Change PID Algorithm -> If reference parameters cross threshold, modify PID to bring it under control, then set pid to normal (Useful in case of wind)

        # CHECK FOR COLLISION(Change from collision mode, and compute collision PIDs only if ultra values again might cause collision)
        self.current_mode = Mode.hover

        for i, val in enumerate(self.ultra.get_ultra_values_current()):

            if (val != 0) and (val < constants.ULTRASOUND_SAFE_DISTANCE):
                self.current_mode = Mode.collision_avoidance
                self.logger.warn_collision(i, val)
                # TODO : Uncomment this before uploading
                # self.pidhandler.compute_ultra(i)

        # If collision possible, return the newly computed speeds, and return result without computing other PIDs except Altitude.
        if self.current_mode != Mode.collision_avoidance:
            self.pidhandler.compute_yaw()
            self.pidhandler.compute_roll()
            self.pidhandler.compute_pitch()

        # Allow Altitude hold to ensure that quad doesnt crash into the ground
        if self.altitude_hold_status == Altitude_Hold.on:
            self.pidhandler.compute_altitude()

        # TODO: Remove this line, after testing completed. Dont use this (uses 10KB for running a 40iteration simulation)
        self.logger.data_set_speeds(self.motor.get_speed())


        self.update_flight_status()
        # print self.motor.get_speed()
        return map(lambda x: int(x),self.motor.get_speed())
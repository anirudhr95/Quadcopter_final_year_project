import constants
from pid import PID


class Quadcopter:
    """
    PID UPDATES
        3 Modes :
            1) Hover : PID = NORMAL.. update pitch yaw roll altitude pids
            2) Flight : PID = FLIGHT. update pitch yaw roll altitude pids
            3) Collision : Dont update pitch, yaw.. USE ULTRASOUND PIDS corresponding to the problematic side.. Update Altitudes too
    """

    # TODO When switching from Flight mode to hover, set ypr_desired to reverse(current ypr) with high kp,ki,kd
    def __init_pid__(self):
        """
        Tilt forward = +ve pitch
        Tilt left = +ve roll
        Rotate Left = +ve yaw
        """

        self.PID_YAW_FR = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=0,
                              Kp=constants.KP_NORMAL,
                              Kd=constants.KD_NORMAL,
                              Ki=constants.KI_NORMAL,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=not constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_YAW_FL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=1,
                              Kp=constants.KP_NORMAL,
                              Kd=constants.KD_NORMAL,
                              Ki=constants.KI_NORMAL,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_YAW_BR = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=2,
                              Kp=constants.KP_NORMAL,
                              Kd=constants.KD_NORMAL,
                              Ki=constants.KI_NORMAL,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_YAW_BL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              output_index_to_use=3,
                              Kp=constants.KP_NORMAL,
                              Kd=constants.KD_NORMAL,
                              Ki=constants.KI_NORMAL,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=not constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_PITCH_FR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=0,
                                Kp=constants.KP_NORMAL,
                                Kd=constants.KD_NORMAL,
                                Ki=constants.KI_NORMAL,
                                max=constants.MOTOR_MAX,
                                min=constants.MOTOR_MIN,
                                reverse_direction=True
                                )
        self.PID_PITCH_FL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=1,
                                Kp=constants.KP_NORMAL,
                                Kd=constants.KD_NORMAL,
                                Ki=constants.KI_NORMAL,
                                max=constants.MOTOR_MAX,
                                min=constants.MOTOR_MIN,
                                reverse_direction=True
                                )
        self.PID_PITCH_BR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=2,
                                Kp=constants.KP_NORMAL,
                                Kd=constants.KD_NORMAL,
                                Ki=constants.KI_NORMAL,
                                max=constants.MOTOR_MAX,
                                min=constants.MOTOR_MIN,
                                reverse_direction=False
                                )
        self.PID_PITCH_BL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                output_index_to_use=3,
                                Kp=constants.KP_NORMAL,
                                Kd=constants.KD_NORMAL,
                                Ki=constants.KI_NORMAL,
                                max=constants.MOTOR_MAX,
                                min=constants.MOTOR_MIN,
                                reverse_direction=False
                                )
        self.PID_ROLL_FR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=0,
                               Kp=constants.KP_NORMAL,
                               Kd=constants.KD_NORMAL,
                               Ki=constants.KI_NORMAL,
                               max=constants.MOTOR_MAX,
                               min=constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ROLL_FL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=1,
                               Kp=constants.KP_NORMAL,
                               Kd=constants.KD_NORMAL,
                               Ki=constants.KI_NORMAL,
                               max=constants.MOTOR_MAX,
                               min=constants.MOTOR_MIN,
                               reverse_direction=True
                               )
        self.PID_ROLL_BR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=2,
                               Kp=constants.KP_NORMAL,
                               Kd=constants.KD_NORMAL,
                               Ki=constants.KI_NORMAL,
                               max=constants.MOTOR_MAX,
                               min=constants.MOTOR_MIN,
                               reverse_direction=False
                               )
        self.PID_ROLL_BL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               output_index_to_use=3,
                               Kp=constants.KP_NORMAL,
                               Kd=constants.KD_NORMAL,
                               Ki=constants.KI_NORMAL,
                               max=constants.MOTOR_MAX,
                               min=constants.MOTOR_MIN,
                               reverse_direction=True
                               )
        self.PID_ALT_FR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=0,
                              Kp=constants.KP_ALTITUDE,
                              Kd=constants.KD_ALTITUDE,
                              Ki=constants.KI_ALTITUDE,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_FL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=1,
                              Kp=constants.KP_ALTITUDE,
                              Kd=constants.KD_ALTITUDE,
                              Ki=constants.KI_ALTITUDE,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_BR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=2,
                              Kp=constants.KP_ALTITUDE,
                              Kd=constants.KD_ALTITUDE,
                              Ki=constants.KI_ALTITUDE,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ALT_BL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              output_index_to_use=3,
                              Kp=constants.KP_ALTITUDE,
                              Kd=constants.KD_ALTITUDE,
                              Ki=constants.KI_ALTITUDE,
                              max=constants.MOTOR_MAX,
                              min=constants.MOTOR_MIN,
                              reverse_direction=False
                              )
        self.PID_ULTRA_FRONT_FR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      output_index_to_use=0,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_FRONT_FL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      output_index_to_use=1,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_FRONT_BR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      output_index_to_use=2,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=True
                                      )

        self.PID_ULTRA_FRONT_BL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      output_index_to_use=3,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=True
                                      )
        self.PID_ULTRA_RIGHT_FR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      output_index_to_use=0,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_RIGHT_FL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      output_index_to_use=1,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=True
                                      )

        self.PID_ULTRA_RIGHT_BR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      output_index_to_use=2,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_RIGHT_BL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      output_index_to_use=3,
                                      Kp=constants.KP_ULTRASOUND,
                                      Kd=constants.KD_ULTRASOUND,
                                      Ki=constants.KI_ULTRASOUND,
                                      max=constants.MOTOR_MAX,
                                      min=constants.MOTOR_MIN,
                                      reverse_direction=True
                                      )
        self.PID_ULTRA_LEFT_FR = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     output_index_to_use=0,
                                     Kp=constants.KP_ULTRASOUND,
                                     Kd=constants.KD_ULTRASOUND,
                                     Ki=constants.KI_ULTRASOUND,
                                     max=constants.MOTOR_MAX,
                                     min=constants.MOTOR_MIN,
                                     reverse_direction=True
                                     )

        self.PID_ULTRA_LEFT_FL = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     output_index_to_use=1,
                                     Kp=constants.KP_ULTRASOUND,
                                     Kd=constants.KD_ULTRASOUND,
                                     Ki=constants.KI_ULTRASOUND,
                                     max=constants.MOTOR_MAX,
                                     min=constants.MOTOR_MIN,
                                     reverse_direction=False
                                     )

        self.PID_ULTRA_LEFT_BR = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     output_index_to_use=2,
                                     Kp=constants.KP_ULTRASOUND,
                                     Kd=constants.KD_ULTRASOUND,
                                     Ki=constants.KI_ULTRASOUND,
                                     max=constants.MOTOR_MAX,
                                     min=constants.MOTOR_MIN,
                                     reverse_direction=True
                                     )

        self.PID_ULTRA_LEFT_BL = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     output_index_to_use=3,
                                     Kp=constants.KP_ULTRASOUND,
                                     Kd=constants.KD_ULTRASOUND,
                                     Ki=constants.KI_ULTRASOUND,
                                     max=constants.MOTOR_MAX,
                                     min=constants.MOTOR_MIN,
                                     reverse_direction=False
                                     )
        self.PID_ULTRA_TOP_FR = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    output_index_to_use=0,
                                    Kp=constants.KP_ULTRASOUND,
                                    Kd=constants.KD_ULTRASOUND,
                                    Ki=constants.KI_ULTRASOUND,
                                    max=constants.MOTOR_MAX,
                                    min=constants.MOTOR_MIN,
                                    reverse_direction=True
                                    )

        self.PID_ULTRA_TOP_FL = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    output_index_to_use=1,
                                    Kp=constants.KP_ULTRASOUND,
                                    Kd=constants.KD_ULTRASOUND,
                                    Ki=constants.KI_ULTRASOUND,
                                    max=constants.MOTOR_MAX,
                                    min=constants.MOTOR_MIN,
                                    reverse_direction=True
                                    )

        self.PID_ULTRA_TOP_BR = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    output_index_to_use=2,
                                    Kp=constants.KP_ULTRASOUND,
                                    Kd=constants.KD_ULTRASOUND,
                                    Ki=constants.KI_ULTRASOUND,
                                    max=constants.MOTOR_MAX,
                                    min=constants.MOTOR_MIN,
                                    reverse_direction=True
                                    )

        self.PID_ULTRA_TOP_BL = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    output_index_to_use=3,
                                    Kp=constants.KP_ULTRASOUND,
                                    Kd=constants.KD_ULTRASOUND,
                                    Ki=constants.KI_ULTRASOUND,
                                    max=constants.MOTOR_MAX,
                                    min=constants.MOTOR_MIN,
                                    reverse_direction=True
                                    )

    def __init__(self, pi_logger):
        self.logger = pi_logger
        self.should_hold_altitude = False
        self.should_change_yaw = False
        self.__is_mode_Hover__ = False
        self.__is_mode_Collision_Avoid = False
        self.__has_taken_off__ = False

        self.altitudes = {'current': 0.0,
                          'desired': 0.0}

        # ORDER IS FR,FL,BR,BL
        self.motor_Speeds = [constants.MOTOR_MIN, constants.MOTOR_MIN, constants.MOTOR_MIN, constants.MOTOR_MIN]

        # Which ultra sensor is about to collide
        self.collision_ultra_index = 0
        # ORDER IS F,R,L,T

        self.ultra_values = {'current': [0.0, 0.0, 0.0, 0.0],
                             'desired': [constants.ULTRASOUND_SAFE_DISTANCE, constants.ULTRASOUND_SAFE_DISTANCE,
                                         constants.ULTRASOUND_SAFE_DISTANCE, constants.ULTRASOUND_SAFE_DISTANCE]}

        self.ypr = {'current': [0.0, 0.0, 0.0],
                    'desired': [0.0, 0.0, 0.0]}
        self.__init_pid__()
        self.PIDS_Pitch = [self.PID_PITCH_FR,
                           self.PID_PITCH_FL,
                           self.PID_PITCH_BR,
                           self.PID_PITCH_BL]
        self.PIDS_Yaw = [self.PID_YAW_FR,
                         self.PID_YAW_FL,
                         self.PID_YAW_BR,
                         self.PID_YAW_BL]
        self.PIDS_Roll = [self.PID_ROLL_FR,
                          self.PID_ROLL_FL,
                          self.PID_ROLL_BR,
                          self.PID_ROLL_BL]
        self.PIDS_Altitude = [self.PID_ALT_FR,
                              self.PID_ALT_FL,
                              self.PID_ALT_BR,
                              self.PID_ALT_BL]
        self.PIDS_ULTRA_Front = [self.PID_ULTRA_FRONT_FR,
                                 self.PID_ULTRA_FRONT_FL,
                                 self.PID_ULTRA_FRONT_BR,
                                 self.PID_ULTRA_FRONT_BL]
        self.PIDS_ULTRA_Right = [self.PID_ULTRA_RIGHT_FR,
                                 self.PID_ULTRA_RIGHT_FL,
                                 self.PID_ULTRA_RIGHT_BR,
                                 self.PID_ULTRA_RIGHT_BL]
        self.PIDS_ULTRA_Left = [self.PID_ULTRA_LEFT_FR,
                                self.PID_ULTRA_LEFT_FL,
                                self.PID_ULTRA_LEFT_BR,
                                self.PID_ULTRA_LEFT_BL]
        self.PIDS_ULTRA_Top = [self.PID_ULTRA_TOP_FR,
                               self.PID_ULTRA_TOP_FL,
                               self.PID_ULTRA_TOP_BR,
                               self.PID_ULTRA_TOP_BL]
        self.PIDS_ULTRA = [self.PIDS_ULTRA_Front,
                           self.PIDS_ULTRA_Right,
                           self.PIDS_ULTRA_Left,
                           self.PIDS_ULTRA_Top]

    def get_ultra_values_current(self):
        return self.ultra_values['current']

    def set_sensor_ultra_values(self, front, right, left, top):

        self.ultra_values['current'][0] = front
        self.ultra_values['current'][1] = right
        self.ultra_values['current'][2] = left
        self.ultra_values['current'][3] = top
        for i in range(len(self.ultra_values['current'])):
            if self.ultra_values['current'][i] != 0:
                self.ultra_values['current'][i] -= constants.ULTRASOUND_TOWINGTIP_OFFSET

        self.logger.data_ultrasound(self.ultra_values['current'])

    def takeoff(self):
        print '\n\nENTERED TAKEOFF'
        self.logger.mode_Takeoff()
        self.__has_taken_off__ = True
        # To make sure speed doesnt reach lesser than min rotation speed(Instant crash)
        for PID in self.PIDS_Pitch:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_MIN)
        for PID in self.PIDS_Yaw:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_MIN)
        for PID in self.PIDS_Roll:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_MIN)
        for PID in self.PIDS_Altitude:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_MIN)
        for PID_TYPE in self.PIDS_ULTRA:
            for PID in PID_TYPE:
                PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_MIN)

        self.set_mode_hover_enable(constants.TAKEOFF_PREFERED_ALTITUDE)

    def land(self):
        self.logger.mode_Land()
        for PID in self.PIDS_Pitch:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_ABSOLUTE__MIN)
        for PID in self.PIDS_Yaw:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_ABSOLUTE__MIN)
        for PID in self.PIDS_Roll:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_ABSOLUTE__MIN)
        for PID in self.PIDS_Altitude:
            PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_ABSOLUTE__MIN)
        for PID_TYPE in self.PIDS_ULTRA:
            for PID in PID_TYPE:
                PID.set_output_limits(constants.MOTOR_MAX, constants.MOTOR_ABSOLUTE__MIN)
        self.set_mode_altitude_hold_enable(0.0)

    # COLLISION MODE STUFF
    def set_mode_collision_avoid_enable(self):
        self.__is_mode_Collision_Avoid = True

    def set_mode_collision_avoid_disable(self):
        self.__is_mode_Collision_Avoid = False

    def is_mode_collision_avoid(self):
        return self.__is_mode_Collision_Avoid

    # ALTITUDE HOLD
    def set_mode_altitude_hold_enable(self, height=None):
        if not self.is_mode_altitude_hold():
            self.logger.mode_altitude_hold(1)
            self.should_hold_altitude = True

        if height != None:
            self.__set_altitude_desired__(height)
        else:
            self.__set_altitude_desired__(self.get_altitude_current())

    def set_mode_altitude_hold_disable(self):
        if self.is_mode_altitude_hold():
            self.logger.mode_altitude_hold(0)
            self.should_hold_altitude = False

    def is_mode_altitude_hold(self):
        return self.should_hold_altitude

    def __compute__(self):
        """
        Modifies motor speeds
        """
        # Check for bad angles
        # TODO: Change PID Algorithm -> If reference parameters cross threshold, modify PID to bring it under control, then set pid to normal (Useful in case of wind)

        # CHECK FOR COLLISION
        self.set_mode_collision_avoid_disable()
        val = self.ultra_values['current']
        for i in range(len(val)):
            if (val[i] != 0) and (val[i] < constants.ULTRASOUND_SAFE_DISTANCE):
                self.set_mode_collision_avoid_enable()
                self.logger.warn_collision(i, self.ultra_values['current'][i])
                for pid in self.PIDS_ULTRA[i]:
                    pid.compute()

        # If collision possible, return the newly computed speeds, and return result without computing other PIDs except Altitude.
        if not self.is_mode_collision_avoid():
            for pid in self.PIDS_Yaw:
                pid.compute()

            for pid in self.PIDS_Pitch:
                pid.compute()
            for pid in self.PIDS_Roll:
                pid.compute()

        # Allow Altitude hold to ensure that quad doesnt crash into the ground
        if self.is_mode_altitude_hold():
            for pid in self.PIDS_Altitude:
                pid.compute()
        # TODO: Remove this line, after testing completed. Dont use this (uses 10KB for running a 40iteration simulation)
        self.logger.data_set_speeds(self.motor_Speeds)

        # Check if land target speed reached


        return self.motor_Speeds

    def __str__(self):
        return "ALTITUDES : %s,\nYPRS : %s,\nMotorSpeeds : %s\nMode:%s" % (self.altitudes, self.ypr, self.motor_Speeds,
                                                                           {'Hover': self.is_mode_hover(),
                                                                            'AltitudeHold': self.is_mode_altitude_hold(),
                                                                            'Flight': self.is_mode_flight()})

    def has_landed(self):
        return True if not filter(lambda x: x < constants.MOTOR_MIN, self.motor_Speeds) else False

    def has_taken_off(self):
        return self.__has_taken_off__

    def refresh(self):
        """
        :returns Motorspeeds: The new motor speeds to set
        """
        # Return existing speed if takeoff command has not been given
        if not self.has_taken_off():
            return self.motor_Speeds
        # Compute new motor speeds
        self.__compute__()

        if self.has_landed():
            self.__has_taken_off__ = False

        return self.motor_Speeds

    def __set_pid_test__(self, p, i, d):
        for PID in self.PIDS_Pitch:
            PID.change_pid(p, i, d)
        for PID in self.PIDS_Yaw:
            PID.change_pid(p, i, d)
        for PID in self.PIDS_Roll:
            PID.change_pid(p, i, d)

    def set_mode_flight_enable(self, hold_altitude=True):
        if not self.is_mode_flight():
            self.logger.mode_flight()
            if hold_altitude:
                self.set_mode_altitude_hold_enable()
            else:
                self.set_mode_altitude_hold_disable()
            self.__set_pid_flight__()
            self.__is_mode_Hover__ = False

    def __set_pid_flight__(self):
        for PID in self.PIDS_Pitch:
            PID.change_pid(constants.KP_FLIGHTMODE, constants.KI_FLIGHTMODE, constants.KD_NORMAL)

        for PID in self.PIDS_Yaw:
            PID.change_pid(constants.KP_FLIGHTMODE, constants.KI_FLIGHTMODE, constants.KD_NORMAL)
        for PID in self.PIDS_Roll:
            PID.change_pid(constants.KP_FLIGHTMODE, constants.KI_FLIGHTMODE, constants.KD_NORMAL)

    def is_mode_flight(self):
        return not self.__is_mode_Hover__

    def set_mode_hover_enable(self, height=None, disable_Altitude_Hold=False):
        """

        :param height:
        :param disable_Altitude_Hold: Used by set_speed to prevent reduction in speeds by PID
        """
        if not self.is_mode_hover():
            self.logger.mode_hover()
        self.set_ypr_desired([self.get_ypr_current()[0], 0, 0])
        if not disable_Altitude_Hold:
            self.set_mode_altitude_hold_enable(height)
        else:
            self.set_mode_altitude_hold_disable()
        self.__set_pid_hover__()
        self.__is_mode_Hover__ = True

    def __set_pid_hover__(self):
        for PID in self.PIDS_Pitch:
            PID.change_pid(constants.KP_NORMAL, constants.KI_NORMAL, constants.KD_NORMAL)

        for PID in self.PIDS_Yaw:
            PID.change_pid(constants.KP_NORMAL, constants.KI_NORMAL, constants.KD_NORMAL)
        for PID in self.PIDS_Roll:
            PID.change_pid(constants.KP_NORMAL, constants.KI_NORMAL, constants.KD_NORMAL)

    def is_mode_hover(self):
        return self.__is_mode_Hover__

    def __check_ypr_goodness__(self, ypr):
        return (ypr[1] <= constants.MAX_PITCH and ypr[1] >= -constants.MAX_PITCH) \
               and (ypr[2] <= constants.MAX_ROLL and ypr[2] >= -constants.MAX_ROLL)

    def get_ypr_current(self):
        return self.ypr['current']

    def sensor_set_ypr_current(self, ypr):
        """
        Called only by sensors
        :param ypr:
        :return:
        """
        self.ypr['current'] = ypr

    def get_ypr_desired(self):
        return self.ypr['desired']

    def set_ypr_desired(self, ypr):
        self.logger.data_set_ypr(ypr)
        if self.__check_ypr_goodness__(ypr):
            self.ypr['desired'] = ypr
            if ypr != [self.get_ypr_current()[0], 0, 0]:
                #
                # Helps prevent infinite loop while calling else condition
                self.set_mode_flight_enable()
            return True
        else:
            self.logger.error("DESIRED YPR UNSUITABLE : %s" % ypr)
            self.set_mode_hover_enable()
            return False

    def set_sensor_altitude_current(self, altitude):
        """
        Should be called only by sensors.. Use set_altitude_desired for moving quad
        :param altitude:
        :return:
        """
        if altitude == 0:
            # Sensor cant find floor(Ultrasound)
            self.set_mode_altitude_hold_disable()
        else:
            self.altitudes['current'] = altitude
            if not self.is_mode_altitude_hold():
                self.set_mode_altitude_hold_enable(self.get_altitude_desired())

    def get_altitude_current(self):
        return self.altitudes['current']

    def __set_altitude_desired__(self, altitude):
        """
        Should be called only by set_mode_altitude_hold_enable
        :param altitude:
        :return:
        """
        self.logger.data_set_altitude(altitude)
        self.altitudes['desired'] = altitude

    def get_altitude_desired(self):
        return self.altitudes['desired']

    def set_speed(self, speed):
        self.logger.data_set_speeds([speed for i in range(4)])

        for i in range(4):
            self.motor_Speeds[i] = speed if speed < constants.MOTOR_MIN else constants.MOTOR_MIN
            self.motor_Speeds[i] = speed if speed > constants.MOTOR_MAX else constants.MOTOR_MAX
        self.set_mode_hover_enable(disable_Altitude_Hold=True)


def sim_1(a, ypr=None):
    """
    Simulates ypr change
    :param a:
    :return:
    """
    if ypr:
        a.set_ypr_desired(ypr)
    else:
        a.set_ypr_desired([0, 20.0, 10.0])
    # a.set_sensor_altitude_current(20.0)
    # a.__set_altitude_desired__(20.0)

    for i in range(20):
        print a.get_ypr_current(), a.refresh()
        # INCREASE YPR BY [0,2,1]
        a.sensor_set_ypr_current([x + y for x, y in zip(a.get_ypr_current(), [0, 2, 1])])

    print 'Decreasing PITCH, setting hover mode'
    a.set_mode_hover_enable()
    for i in range(20):
        print a.get_ypr_current(), a.refresh()
        a.sensor_set_ypr_current([x + y for x, y in zip(a.get_ypr_current(), [0, -3, -0.5])])


def sim_2(a):
    """
    Simulates takeoff and landing
    :param a:
    :return:
    """
    a.takeoff()
    for i in range(20):
        b = a.refresh()
        a.set_sensor_altitude_current(a.get_altitude_current() + 3)
        print a.altitudes, b
    a.land()
    a.set_speed(2000.0)
    for i in range(20):
        b = a.refresh()
        a.set_sensor_altitude_current(a.get_altitude_current() - 3)
        print a.altitudes, b


def sim_3(a):
    """
    Simulates Ultrasound detection
    :param a:
    :return:
    """
    a.takeoff()
    sensor_vals = [1, 2, 3, 4]
    a = Quadcopter()
    a.set_sensor_ultra_values(25, 60, 60, 60)
    for i in range(20):
        b = a.refresh()


if __name__ == '__main__':
    import customlogger

    a = Quadcopter(customlogger.pi_logger())
    sim_1(a)
    a = Quadcopter(customlogger.pi_logger())
    sim_2(a)

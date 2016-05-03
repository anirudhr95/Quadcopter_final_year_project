import Constants
from PID import PID


class pid_handler:
    def __init_pid__(self):
        """
        Tilt forward = +ve pitch
        Tilt left = +ve roll
        Rotate Left = +ve yaw
        """

        self.PID_YAW_FR = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=0,
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=not Constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_YAW_FL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=1,
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=Constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_YAW_BR = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=2,
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=Constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_YAW_BL = PID(reference=self.ypr,
                              output=self.motor_Speeds,
                              reference_index_to_use=0,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=3,
                              Kp=Constants.KP_NORMAL,
                              Kd=Constants.KD_NORMAL,
                              Ki=Constants.KI_NORMAL,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=not Constants.WING_FR_ANTICLOCKWISE
                              )
        self.PID_PITCH_FR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                previous_output_update=self.previous_motorupdate,
                                output_index_to_use=0,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX_FLIGHT,
                                min=Constants.MOTOR_MIN_FLIGHT,
                                reverse_direction=True
                                )
        self.PID_PITCH_FL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                previous_output_update=self.previous_motorupdate,
                                output_index_to_use=1,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX_FLIGHT,
                                min=Constants.MOTOR_MIN_FLIGHT,
                                reverse_direction=True
                                )
        self.PID_PITCH_BR = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                previous_output_update=self.previous_motorupdate,
                                output_index_to_use=2,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX_FLIGHT,
                                min=Constants.MOTOR_MIN_FLIGHT,
                                reverse_direction=False
                                )
        self.PID_PITCH_BL = PID(reference=self.ypr,
                                output=self.motor_Speeds,
                                reference_index_to_use=1,
                                previous_output_update=self.previous_motorupdate,
                                output_index_to_use=3,
                                Kp=Constants.KP_NORMAL,
                                Kd=Constants.KD_NORMAL,
                                Ki=Constants.KI_NORMAL,
                                max=Constants.MOTOR_MAX_FLIGHT,
                                min=Constants.MOTOR_MIN_FLIGHT,
                                reverse_direction=False
                                )
        self.PID_ROLL_FR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               previous_output_update=self.previous_motorupdate,
                               output_index_to_use=0,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX_FLIGHT,
                               min=Constants.MOTOR_MIN_FLIGHT,
                               reverse_direction=False
                               )
        self.PID_ROLL_FL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               previous_output_update=self.previous_motorupdate,
                               output_index_to_use=1,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX_FLIGHT,
                               min=Constants.MOTOR_MIN_FLIGHT,
                               reverse_direction=True
                               )
        self.PID_ROLL_BR = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               previous_output_update=self.previous_motorupdate,
                               output_index_to_use=2,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX_FLIGHT,
                               min=Constants.MOTOR_MIN_FLIGHT,
                               reverse_direction=False
                               )
        self.PID_ROLL_BL = PID(reference=self.ypr,
                               output=self.motor_Speeds,
                               reference_index_to_use=2,
                               previous_output_update=self.previous_motorupdate,
                               output_index_to_use=3,
                               Kp=Constants.KP_NORMAL,
                               Kd=Constants.KD_NORMAL,
                               Ki=Constants.KI_NORMAL,
                               max=Constants.MOTOR_MAX_FLIGHT,
                               min=Constants.MOTOR_MIN_FLIGHT,
                               reverse_direction=True
                               )
        self.PID_ALT_FR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=0,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=False
                              )
        self.PID_ALT_FL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=1,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=False
                              )
        self.PID_ALT_BR = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=2,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=False
                              )
        self.PID_ALT_BL = PID(reference=self.altitudes,
                              output=self.motor_Speeds,
                              reference_index_to_use=None,
                              previous_output_update=self.previous_motorupdate,
                              output_index_to_use=3,
                              Kp=Constants.KP_ALTITUDE,
                              Kd=Constants.KD_ALTITUDE,
                              Ki=Constants.KI_ALTITUDE,
                              max=Constants.MOTOR_MAX_FLIGHT,
                              min=Constants.MOTOR_MIN_FLIGHT,
                              reverse_direction=False
                              )
        self.PID_ULTRA_FRONT_FR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=0,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_FRONT_FL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=1,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_FRONT_BR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=2,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=True
                                      )

        self.PID_ULTRA_FRONT_BL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=0,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=3,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=True
                                      )
        self.PID_ULTRA_RIGHT_FR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=0,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_RIGHT_FL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=1,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=True
                                      )

        self.PID_ULTRA_RIGHT_BR = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=2,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=False
                                      )

        self.PID_ULTRA_RIGHT_BL = PID(reference=self.ultra_values,
                                      output=self.motor_Speeds,
                                      reference_index_to_use=1,
                                      previous_output_update=self.previous_motorupdate,
                                      output_index_to_use=3,
                                      Kp=Constants.KP_ULTRASOUND,
                                      Kd=Constants.KD_ULTRASOUND,
                                      Ki=Constants.KI_ULTRASOUND,
                                      max=Constants.MOTOR_MAX_FLIGHT,
                                      min=Constants.MOTOR_MIN_FLIGHT,
                                      reverse_direction=True
                                      )
        self.PID_ULTRA_LEFT_FR = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     previous_output_update=self.previous_motorupdate,
                                     output_index_to_use=0,
                                     Kp=Constants.KP_ULTRASOUND,
                                     Kd=Constants.KD_ULTRASOUND,
                                     Ki=Constants.KI_ULTRASOUND,
                                     max=Constants.MOTOR_MAX_FLIGHT,
                                     min=Constants.MOTOR_MIN_FLIGHT,
                                     reverse_direction=True
                                     )

        self.PID_ULTRA_LEFT_FL = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     previous_output_update=self.previous_motorupdate,
                                     output_index_to_use=1,
                                     Kp=Constants.KP_ULTRASOUND,
                                     Kd=Constants.KD_ULTRASOUND,
                                     Ki=Constants.KI_ULTRASOUND,
                                     max=Constants.MOTOR_MAX_FLIGHT,
                                     min=Constants.MOTOR_MIN_FLIGHT,
                                     reverse_direction=False
                                     )

        self.PID_ULTRA_LEFT_BR = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     previous_output_update=self.previous_motorupdate,
                                     output_index_to_use=2,
                                     Kp=Constants.KP_ULTRASOUND,
                                     Kd=Constants.KD_ULTRASOUND,
                                     Ki=Constants.KI_ULTRASOUND,
                                     max=Constants.MOTOR_MAX_FLIGHT,
                                     min=Constants.MOTOR_MIN_FLIGHT,
                                     reverse_direction=True
                                     )

        self.PID_ULTRA_LEFT_BL = PID(reference=self.ultra_values,
                                     output=self.motor_Speeds,
                                     reference_index_to_use=2,
                                     previous_output_update=self.previous_motorupdate,
                                     output_index_to_use=3,
                                     Kp=Constants.KP_ULTRASOUND,
                                     Kd=Constants.KD_ULTRASOUND,
                                     Ki=Constants.KI_ULTRASOUND,
                                     max=Constants.MOTOR_MAX_FLIGHT,
                                     min=Constants.MOTOR_MIN_FLIGHT,
                                     reverse_direction=False
                                     )
        self.PID_ULTRA_TOP_FR = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    previous_output_update=self.previous_motorupdate,
                                    output_index_to_use=0,
                                    Kp=Constants.KP_ULTRASOUND,
                                    Kd=Constants.KD_ULTRASOUND,
                                    Ki=Constants.KI_ULTRASOUND,
                                    max=Constants.MOTOR_MAX_FLIGHT,
                                    min=Constants.MOTOR_MIN_FLIGHT,
                                    reverse_direction=True
                                    )

        self.PID_ULTRA_TOP_FL = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    previous_output_update=self.previous_motorupdate,
                                    output_index_to_use=1,
                                    Kp=Constants.KP_ULTRASOUND,
                                    Kd=Constants.KD_ULTRASOUND,
                                    Ki=Constants.KI_ULTRASOUND,
                                    max=Constants.MOTOR_MAX_FLIGHT,
                                    min=Constants.MOTOR_MIN_FLIGHT,
                                    reverse_direction=True
                                    )

        self.PID_ULTRA_TOP_BR = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    previous_output_update=self.previous_motorupdate,
                                    output_index_to_use=2,
                                    Kp=Constants.KP_ULTRASOUND,
                                    Kd=Constants.KD_ULTRASOUND,
                                    Ki=Constants.KI_ULTRASOUND,
                                    max=Constants.MOTOR_MAX_FLIGHT,
                                    min=Constants.MOTOR_MIN_FLIGHT,
                                    reverse_direction=True
                                    )

        self.PID_ULTRA_TOP_BL = PID(reference=self.ultra_values,
                                    output=self.motor_Speeds,
                                    reference_index_to_use=3,
                                    previous_output_update=self.previous_motorupdate,
                                    output_index_to_use=3,
                                    Kp=Constants.KP_ULTRASOUND,
                                    Kd=Constants.KD_ULTRASOUND,
                                    Ki=Constants.KI_ULTRASOUND,
                                    max=Constants.MOTOR_MAX_FLIGHT,
                                    min=Constants.MOTOR_MIN_FLIGHT,
                                    reverse_direction=True
                                    )

    def __init__(self, logger, motor_speeds, ultra_values, altitude, ypr):
        self.logger = logger
        self.ultra_values = ultra_values
        self.motor_Speeds = motor_speeds
        self.altitudes = altitude
        self.ypr = ypr
        from numpy import array
        self.previous_motorupdate = array([0, 0, 0, 0], dtype='int16')

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
        self.PIDS_YPRA = [self.PIDS_Yaw, self.PIDS_Pitch, self.PIDS_Roll, self.PIDS_Altitude]
        self.PIDS_YPR = [self.PIDS_Yaw, self.PIDS_Pitch, self.PIDS_Roll]
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
        for pid_class in self.PIDS_YPRA:
            for pid in pid_class:
                print pid.reverse_direction, pid.reference_index, pid.output_index, pid.Kp

    def compute_yaw(self):
        for pid in self.PIDS_Yaw:
            pid.compute()

    def compute_pitch(self):
        for pid in self.PIDS_Pitch:
            pid.compute()

    def compute_roll(self):
        for pid in self.PIDS_Roll:
            pid.compute()

    def compute_ultra(self, index):
        """

        :param index: index to compute pid (Order = FRONT RIGHT LEFT TOP)
        :return:
        """
        for pid in self.PIDS_ULTRA[index]:
            pid.compute()

    def compute_altitude(self):
        for pid in self.PIDS_Altitude:
            pid.compute()

    def __set_pid__(self, p, i, d):
        for pid_class in self.PIDS_YPR:
            for pid in pid_class:
                pid.change_pid(p, i, d)

    def set_pid_constants_for_test(self, p, i, d):
        self.__set_pid__(p, i, d)

    def set_pid_constants_for_flight(self):
        self.__set_pid__(Constants.KP_FLIGHTMODE, Constants.KI_FLIGHTMODE, Constants.KD_NORMAL)

    def set_pid_constants_for_hover(self):
        self.__set_pid__(Constants.KP_NORMAL, Constants.KI_NORMAL, Constants.KD_NORMAL)

    def set_speedlimit__flight(self):
        for pid_class in self.PIDS_YPRA:
            for pid in pid_class:
                pid.set_output_limits(Constants.MOTOR_MAX_FLIGHT, Constants.MOTOR_MIN_FLIGHT)

    def set_speedlimit_landing(self):
        for pid_class in self.PIDS_YPRA:
            for pid in pid_class:
                pid.set_output_limits(Constants.MOTOR_MAX_FLIGHT, Constants.MOTOR_MIN_LANDING)

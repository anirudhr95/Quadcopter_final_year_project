import constants
from pid import PID


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

    def __init__(self, logger, motor_speeds, ultra_values, altitude, ypr):
        self.logger = logger
        self.ultra_values = ultra_values
        self.motor_Speeds = motor_speeds
        self.altitudes = altitude
        self.ypr = ypr

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

    def __set_pid_test__(self, p, i, d):
        for PID in self.PIDS_Pitch:
            PID.change_pid(p, i, d)
        for PID in self.PIDS_Yaw:
            PID.change_pid(p, i, d)
        for PID in self.PIDS_Roll:
            PID.change_pid(p, i, d)

    def __set_pid_flight__(self):
        for PID in self.PIDS_Pitch:
            PID.change_pid(constants.KP_FLIGHTMODE, constants.KI_FLIGHTMODE, constants.KD_NORMAL)

        for PID in self.PIDS_Yaw:
            PID.change_pid(constants.KP_FLIGHTMODE, constants.KI_FLIGHTMODE, constants.KD_NORMAL)
        for PID in self.PIDS_Roll:
            PID.change_pid(constants.KP_FLIGHTMODE, constants.KI_FLIGHTMODE, constants.KD_NORMAL)

    def __set_pid_hover__(self):
        for PID in self.PIDS_Pitch:
            PID.change_pid(constants.KP_NORMAL, constants.KI_NORMAL, constants.KD_NORMAL)

        for PID in self.PIDS_Yaw:
            PID.change_pid(constants.KP_NORMAL, constants.KI_NORMAL, constants.KD_NORMAL)
        for PID in self.PIDS_Roll:
            PID.change_pid(constants.KP_NORMAL, constants.KI_NORMAL, constants.KD_NORMAL)

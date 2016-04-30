import constants
class Motor:
    def __init__(self,logger):
        self.logger = logger
        # ORDER IS FR,FL,BR,BL
        self.motor_Speeds = [constants.MOTOR_MIN_FLIGHT, constants.MOTOR_MIN_FLIGHT, constants.MOTOR_MIN_FLIGHT, constants.MOTOR_MIN_FLIGHT]

    def set_speed(self, speed):
        self.logger.data_set_speeds([speed for i in range(4)])
        for i in range(4):
            self.motor_Speeds[i] = speed if speed < constants.MOTOR_MIN_FLIGHT else constants.MOTOR_MIN_FLIGHT
            self.motor_Speeds[i] = speed if speed > constants.MOTOR_MAX_FLIGHT else constants.MOTOR_MAX_FLIGHT
        # TODO: Fix this
        # self.set_mode_hover_enable(disable_Altitude_Hold=True)

    def get_speed(self):
        """

        :return motor_speeds: passed by reference
        """
        return self.motor_Speeds
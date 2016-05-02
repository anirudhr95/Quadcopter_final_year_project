import Constants


class Ultrasonic:
    def __init__(self, logger):
        self.logger = logger
        self.ultra_values = {'current': [0.0, 0.0, 0.0, 0.0],
                             'desired': [Constants.ULTRASOUND_SAFE_DISTANCE, Constants.ULTRASOUND_SAFE_DISTANCE,
                                         Constants.ULTRASOUND_SAFE_DISTANCE, Constants.ULTRASOUND_SAFE_DISTANCE]}

    def set_sensor_ultra_values(self, front, right, left, top):
        self.ultra_values['current'] = [front, right, left, top]
        self.ultra_values['current'] = map(lambda x: x - Constants.ULTRASOUND_TOWINGTIP_OFFSET if x != 0 else x,
                                           self.ultra_values['current'])
        self.logger.data_ultrasound(self.ultra_values['current'])

    def get_ultra_values_current(self):
        return self.ultra_values['current']
    def get_ultra_values(self):
        """

        :return ultra_values: passed by reference
        """
        return self.ultra_values
import Constants
import numpy


class Ultrasonic:
    def __init__(self, logger):
        self.logger = logger
        self.ultra_values = {'current': numpy.array([0, 0, 0, 0], dtype='int8'),
                             'desired': numpy.array(
                                 [Constants.ULTRASOUND_SAFE_DISTANCE, Constants.ULTRASOUND_SAFE_DISTANCE,
                                  Constants.ULTRASOUND_SAFE_DISTANCE, Constants.ULTRASOUND_SAFE_DISTANCE],
                                 dtype='int8')}

    def set_sensor_ultra_values(self, front, right, left, top):
        self.ultra_values['current'][0] = (front - Constants.ULTRASOUND_TOWINGTIP_OFFSET) if front != 0 else front
        self.ultra_values['current'][1] = (right - Constants.ULTRASOUND_TOWINGTIP_OFFSET) if right != 0 else right
        self.ultra_values['current'][2] = (left - Constants.ULTRASOUND_TOWINGTIP_OFFSET) if left != 0 else left
        self.ultra_values['current'][3] = (top - Constants.ULTRASOUND_TOWINGTIP_OFFSET) if top != 0 else top

        self.logger.data_ultrasound(self.ultra_values['current'])

    def get_ultra_values_current(self):
        return self.ultra_values['current']

    def get_ultra_values(self):
        """

        :return ultra_values: passed by reference
        """
        return self.ultra_values

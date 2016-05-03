import Constants
import numpy


class Gyro:
    def __init__(self, logger):
        self.ypr = {'current': numpy.array([0.0, 0.0, 0.0],dtype='float16'),
                    'desired': numpy.array([0.0, 0.0, 0.0],dtype='float16')}
        self.logger = logger

    def set_ypr_current(self, ypr):
        """
        Called only by sensors
        :param ypr:
        :return:
        """
        self.ypr['current'][0] = ypr[0]
        self.ypr['current'][1] = ypr[1]
        self.ypr['current'][2] = ypr[2]

    def __check_ypr_goodness__(self, ypr):
        return ypr[1] <= Constants.MAX_PITCH and ypr[1] >= -Constants.MAX_PITCH and ypr[2] <= Constants.MAX_ROLL and \
               ypr[2] >= -Constants.MAX_ROLL

    def set_ypr_desired(self, ypr):
        self.logger.data_set_ypr(ypr)
        if self.__check_ypr_goodness__(ypr=ypr):
            self.ypr['desired'][0] = ypr[0]
            self.ypr['desired'][1] = ypr[1]
            self.ypr['desired'][2] = ypr[2]
            return True
        else:
            self.logger.error("DESIRED YPR UNSUITABLE : %s" % ypr)
            # TODO : What to do if ypr desired is incorrect
            return False

    def get_ypr_current(self):
        return self.ypr['current']

    def get_ypr_desired(self):
        return self.ypr['desired']

    def get_ypr(self):
        return self.ypr

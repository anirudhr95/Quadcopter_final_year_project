import constants


class Gyro:
    def __init__(self, logger):
        self.ypr = {'current': [0.0, 0.0, 0.0],
                    'desired': [0.0, 0.0, 0.0]}
        self.logger = logger


    def set_ypr_current(self, ypr):
        """
        Called only by sensors
        :param ypr:
        :return:
        """
        self.ypr['current'] = ypr

    def __check_ypr_goodness__(self,ypr):
        return ypr[1] <= constants.MAX_PITCH and ypr[1] >= -constants.MAX_PITCH and ypr[2] <= constants.MAX_ROLL and \
               ypr[2] >= -constants.MAX_ROLL


    def set_ypr_desired(self, ypr):
        self.logger.data_set_ypr(ypr)
        if self.__check_ypr_goodness__(ypr= ypr):
            self.ypr['desired'] = ypr
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

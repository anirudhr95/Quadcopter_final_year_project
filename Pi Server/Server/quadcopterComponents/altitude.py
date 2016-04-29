class Altitude:
    def __init__(self, logger):
        self.logger = logger

        self.altitudes = {'current': 0.0,
                          'desired': 0.0}

    def set_sensor_altitude_current(self, altitude):
        """
        Should be called only by sensors.. Use set_altitude_desired for moving quad
        :param altitude:
        :return:
        """
        if altitude == 0:
            # Sensor cant find floor(Ultrasound)
            # TODO Fix next line
            # self.set_mode_hover_enable()
            # self.set_mode_altitude_hold_disable()
            pass
        else:
            self.altitudes['current'] = altitude

    def set_altitude_desired(self, altitude):
        """
        Should be called only by set_mode_altitude_hold_enable
        :param altitude:
        :return:
        """
        self.logger.data_set_altitude(altitude)
        self.altitudes['desired'] = altitude
        print 'YOYO:%s' % self.altitudes

    def get_altitude_current(self):
        return self.altitudes['current']

    def get_altitude_desired(self):
        return self.altitudes['desired']
    def get_altitudes(self):
        """

        :return altitudes: passed by reference
        """
        return self.altitudes

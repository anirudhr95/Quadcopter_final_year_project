from quadcopterComponents.quadcopter import Quadcopter


def sim_ypr_change(a, ypr=None):
    """
    Simulates ypr change
    :param a:
    :return:
    """

    # a.set_sensor_altitude_current(20.0)
    # a.self.altitude.set_altitude_desired(20.0)
    a.takeoff()
    a.set_mode_altitude_hold_disable()
    if ypr:
        a.gyro.set_ypr_desired(ypr)
    else:
        a.gyro.set_ypr_desired([0, 20.0, 10.0])
    for i in range(20):
        print a.gyro.get_ypr_current(), a.refresh()
        # INCREASE YPR BY [0,2,1]
        a.gyro.set_ypr_current([x + y for x, y in zip(a.gyro.get_ypr_current(), [0, 2, 1])])

    print 'Decreasing PITCH, setting hover mode'
    a.set_mode_hover_enable()
    for i in range(20):
        print a.gyro.get_ypr_current(), a.refresh()
        a.gyro.set_ypr_current([x + y for x, y in zip(a.gyro.get_ypr_current(), [0, -3, -0.5])])


def sim_altitude(a):
    """
    Simulates takeoff and landing
    :param a:
    :return:
    """
    a.takeoff()
    for i in range(20):
        b = a.refresh()
        a.altitude.set_sensor_altitude_current(a.altitude.get_altitude_current() + 3)
        print a.altitude.get_altitudes(), b
    a.land()
    a.motor.set_speed(2000.0)
    for i in range(20):
        b = a.refresh()
        a.altitude.set_sensor_altitude_current(a.altitude.get_altitude_current() - 3)
        print a.altitude.get_altitudes(), b


def sim_ultrasound(a):
    """
    Simulates Ultrasound detection
    :param a:
    :return:
    """
    a.takeoff()
    sensor_vals = [1, 2, 3, 4]
    a.ultra.set_sensor_ultra_values(25, 60, 60, 60)
    for i in range(20):
        b = a.refresh()


if __name__ == '__main__':
    import CustomLogger

    a = Quadcopter(CustomLogger.pi_logger())
    sim_ypr_change(a)
    a = Quadcopter(CustomLogger.pi_logger())
    sim_altitude(a)
    a = Quadcopter(CustomLogger.pi_logger())
    sim_ultrasound(a)
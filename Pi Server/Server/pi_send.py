#i hef completely removed the serial part now!
import Constants


class pi_send_toArduino:

    def takeoff(self):
        return Constants.IOSMESSAGE_TAKEOFF

    def land(self):
        return Constants.IOSMESSAGE_LAND
    def set_speed(self,a):
        return str(Constants.IOSMESSAGE_SETSPEED + ':' + str(a))
    def hover(self):
        return str(Constants.IOSMESSAGE_HOVER)
    def altitude_hold(self):
        return str(Constants.IOSMESSAGE_HOLDALTITUDE)
    def setYPR(self,a,b,c):
        return '%s:%s;%s;%s'%(Constants.IOSMESSAGE_SETYPR , a, b, c)
    def set_speeds(self, speeds):
        return '%s:%s;%s;%s;%s'%(Constants.PIMESSAGE_SETSPEEDS, speeds[0], speeds[1], speeds[2], speeds[3])

class pi_send_toIOS:

    def error(self, message):
        return {
            'event' : Constants.ARDUINOSTATUS_ERROR,
            'data' : message
        }

    def collision(self, idANDval):
        return {
            'event' : Constants.ARDUINOSTATUS_ULTRASOUND_COLLISION,
            'data' : {'id': idANDval[0],
                      'val': idANDval[1]}

        }
    def ultra_data(self, ultraValues):
        return {
            'event' : Constants.ARDUINOSTATUS_ULTRASOUND_DATA,
            'data' : ultraValues
        }




class pi_receive_fromIOS:
    """
    USELESS CLASS  : REFERENCE FOR SENDING COMMANDS FROM IOS
    """
    def takeoff(self):
        return Constants.IOSMESSAGE_TAKEOFF

    def land(self):
        return Constants.IOSMESSAGE_LAND

    def set_speed(self, a):
        return str(Constants.IOSMESSAGE_SETSPEED + ' ' + str(a))

    def hover(self):
        return str(Constants.IOSMESSAGE_HOVER)

    def altitude_hold(self):
        return str(Constants.IOSMESSAGE_HOLDALTITUDE)

    def setYPR(self, a, b, c):
        return '%s %s;%s;%s' % (Constants.IOSMESSAGE_SETYPR, a, b, c)

    def set_speeds(self, a, b, c, d):
        return '%s %s;%s;%s;%s' % (Constants.PIMESSAGE_SETSPEEDS, a, b, c, d)

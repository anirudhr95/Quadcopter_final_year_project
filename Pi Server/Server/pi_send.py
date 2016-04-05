#i hef completely removed the serial part now!
import Constants


class pi_send_toArduino:

    def takeoff(self):
        return Constants.IOSCOMMAND_TAKEOFF

    def land(self):
        return Constants.IOSCOMMAND_LAND
    def set_speed(self,a):
        return str(Constants.IOSCOMMAND_SETSPEED  + ' ' + str(a))
    def hover(self):
        return str(Constants.IOSCOMMAND_HOVER)
    def altitude_hold(self):
        return str(Constants.IOSCOMMAND_HOLDALTITUDE)
    def setYPR(self,a,b,c):
        return str(Constants.IOSCOMMAND_SETYPR + ' ' + str(a)+';'+str(b)+';'+str(c))

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
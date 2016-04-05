import Constants
import pi_send


class Middleware_IOS:
    """
    Class for processing messages from IOS devices
    """

    def __init__(self, quadcopter):
        self.quadcopter = quadcopter

    def parseMessage(self, msg):
        if ':' in msg:
            functionName, params = msg.split(':')
            if functionName == Constants.IOSCOMMAND_SETSPEED:
                self.quadcopter.set_speed(params)
            elif functionName == Constants.IOSCOMMAND_SETYPR:
                params = map(lambda x: float(x), params.split(";"))
                self.quadcopter.set_YPR(params)
            else:
                self.erraneous_message(msg)

        else:
            # Message is a single line command
            if msg == Constants.IOSCOMMAND_HOLDALTITUDE:
                self.quadcopter.set_Mode_Altitude_Hold()
            elif msg == Constants.IOSCOMMAND_HOVER:
                self.quadcopter.set_Mode_Hover()
            elif msg == Constants.IOSCOMMAND_LAND:
                self.quadcopter.land()
            elif msg == Constants.IOSCOMMAND_TAKEOFF:
                self.quadcopter.takeoff()
            else:
                self.erraneous_message(msg)

    def erraneous_message(self, msg):
        # TODO         LOG AS INCORRECT COMMAND WITH PI AS MODULE
        pass


class Middleware_Arduino:
    """
    Class for processing messages from Arduino
    """

    def __init__(self, ios_message_queue):
        self.message_queue = ios_message_queue
        self.converter = pi_send.pi_send_toIOS()

    def parseMessage(self, msg):
        functionName, params = msg.split(':')
        if functionName == Constants.ARDUINOSTATUS_ERROR:
            # TODO LOG ERROR
            self.message_queue.append(self.converter.error(msg))
            pass
        if functionName == Constants.ARDUINOSTATUS_ULTRASOUND_COLLISION:
            self.message_queue.append(self.converter.collision(params.split(';')))

        if functionName == Constants.ARDUINOSTATUS_ULTRASOUND_DATA:
            self.message_queue.append(self.converter.ultra_data(params.split(';')))

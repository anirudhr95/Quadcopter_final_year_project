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
                # TODO Add support for off and on
                self.quadcopter.land()
            elif msg == Constants.IOSCOMMAND_TAKEOFF:
                self.quadcopter.takeoff()
            else:
                self.erraneous_message(msg)

    def erraneous_message(self, msg):
        # TODO         LOG AS INCORRECT COMMAND WITH PI AS MODULE
        print "Incorrect Message '%s'" %msg
        pass


class Middleware_Arduino:
    """
    Class for processing messages from Arduino
    """

    def __init__(self, quadcopter, ios_message_queue):
        self.message_queue = ios_message_queue
        self.quadcopter = quadcopter
        self.converter = pi_send.pi_send_toIOS()

    def parseMessage(self, msg):

        functionName, params = msg.split(':')
        if functionName == Constants.ARDUINOSTATUS_ERROR:
            self.message_queue.append(self.converter.error(msg))

        if functionName == Constants.ARDUINOSTATUS_DATA:
            # DATA:Y;P;R;Mx;My;Mz;Mh;Al;U1;U2;U3;U4
            y, p, r, mx, my, mz, mh, al, u1, u2, u3, u4 = params.split(';')
            self.quadcopter.set_current_ypr([y, p, r])
            self.quadcopter.set_current_altitude(al)
            self.quadcopter.set_heading(mh)

            # TODO Handle Ultrasonic Data

        if functionName == Constants.ARDUINOSTATUS_ULTRASOUND_COLLISION:
            self.message_queue.append(self.converter.collision(params.split(';')))

        if functionName == Constants.ARDUINOSTATUS_ULTRASOUND_DATA:
            self.message_queue.append(self.converter.ultra_data(params.split(';')))

import copy
import numpy
import Constants
import time as time_


def millis():
    return int(round(time_.time() * 1000))


class PID:
    def __init__(self, reference, output, reference_index_to_use, output_index_to_use, Kp, Ki, Kd,
                 previous_output_update, reverse_direction=False, max=2000, min=1000,
                 samplingTime=Constants.REFRESH_PID_TIME):
        """

        :param reference: A dict with 2 key-array pairs(current,desired)
        :param output: Array with output variables
        :param reference_index_to_use: array index to use as reference, in reference variable(-1 if single value)
        :param output_index_to_use: array index for output variable to modify
        :param Kp:
        :param Ki:
        :param Kd:
        :param direction:
        :param max:
        :param min:
        """
        self.reference = reference
        self.output = output
        self.reference_index = reference_index_to_use
        self.output_index = output_index_to_use
        
        self.PID = numpy.array([min,0,0],dtype = 'float16')
        self.max = numpy.int16(max)
        self.min = numpy.int16(min)
        self.error = numpy.float16(0)
        self.previous_output_update = previous_output_update

        self.samplingTime = samplingTime
        # self.samplingTime = 0.0003
        self.reverse_direction = reverse_direction

        self.Kp = numpy.float16(Kp)
        self.Kd = numpy.float16(Kd)
        self.Ki = numpy.float16(Ki)
        if self.reverse_direction:
            self.Kp *= -1
            self.Ki *= -1
            self.Kd *= -1

        self.lastinput = copy.copy(self.get_current_reference())
        self.lastTime = millis() - self.samplingTime

        self.Kd /= self.samplingTime
        self.Ki *= self.samplingTime
        # self.Kd /= Constants.REFRESH_PID_TIME
        # self.Ki *= Constants.REFRESH_PID_TIME

    def get_current_reference(self):
        a = self.reference['current'][self.reference_index] if self.reference_index != None else self.reference[
            'current']
        return a

    def get_desired_reference(self):
        a = self.reference['desired'][self.reference_index] if self.reference_index != None  else self.reference[
            'desired']
        return a

    def set_output(self, val):
        self.previous_output_update[self.output_index] = val - self.PID[1]

        self.output[self.output_index] = val

    

    def compute(self):
        if millis() - self.lastTime >= self.samplingTime*1000:
            self.error = self.get_desired_reference() - self.get_current_reference()
            if self.error == 0:
                return True
            self.PID[0] = self.Kp * self.error

            self.PID[2] = self.Kd * (self.get_current_reference() - self.lastinput)

            self.PID[1] += self.error * self.Ki
            if self.PID[1] < self.min:
                self.PID[1] = self.min
            elif self.PID[1] > self.max:
                self.PID[1] = self.max

            PID = self.PID[0] + self.PID[1] - self.PID[2]

            PID += self.previous_output_update[self.output_index]

            if PID > self.max:
                self.set_output(self.max)
            elif PID < self.min:
                self.set_output(self.min)
            else:
                self.set_output(PID)

            self.lastinput = copy.copy(self.get_current_reference())
            self.lastTime = millis()
            return True
        return False

    def change_pid(self, Kp, Ki, Kd):
        if not self.reverse_direction:
            self.Kp = Kp
            self.Ki = Ki
            self.Kd = Kd
        else:
            self.Kp = -Kp
            self.Ki = -Ki
            self.Kd = -Kd

    def set_output_limits(self, max, min):
        self.max = max
        self.min = min


if __name__ == "__main__":

    ypr = {'current': [0.0, 0.0, 0.0],
           'desired': [0.0, 20.0, 0.0]}
    motor_Speeds = [0, 0, 0, 0]
    a = PID(ypr, motor_Speeds, 1, 1, 2, 1, 1, min=1200, max=2000)
    print a.compute()
    ypr['current'][1] = 15.0
    for i in range(10):
        ypr['current'][1] += 1
        a.compute()
        print a.get_current_reference(), a.get_current_output()
    for i in range(10):
        ypr['current'][1] -= 1
        print a.get_current_reference(), a.get_current_output()

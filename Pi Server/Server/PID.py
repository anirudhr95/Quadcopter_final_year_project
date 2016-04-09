class PID:
    def __init__(self, reference, output, reference_index_to_use, output_index_to_use, Kp, Ki, Kd, reverse_direction = False, max=2000, min=1000):
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
        self.Kp = Kp
        self.Kd = Kd
        self.Ki = Ki
        self.Derivator = 0
        self.Integrator = 0
        self.max = max
        self.min = min
        self.error = 0.0
        self.reverse_direction = reverse_direction
    def get_current_reference(self):
        a= self.reference['current'][self.reference_index] if self.reference_index != None else self.reference['current']
        return a
    def get_desired_reference(self):
        a = self.reference['desired'][self.reference_index] if self.reference_index != None  else self.reference['desired']
        return a
    def set_output(self,val):
        self.output[self.output_index] = val

    def get_current_output(self):
        return self.output[self.output_index]
    def change_output_by(self, val):
        if self.error < 0:
            if self.reverse_direction:
                self.set_output(self.get_current_output() + val)
            else:
                self.set_output(self.get_current_output() - val)
        else:
            if self.reverse_direction:
                self.set_output(self.get_current_output() - val)
            else:
                self.set_output(self.get_current_output() + val)

        if self.get_current_output() > self.max:
            self.set_output(self.max)
        elif self.get_current_output() < self.min:
            self.set_output(self.min)
        return self.get_current_output()

    def compute(self):
        self.error = self.get_desired_reference() - self.get_current_reference()
        self.P_value = self.Kp * self.error
        self.D_value = self.Kd * (self.error - self.Derivator)
        self.Derivator = self.error

        self.Integrator = self.Integrator + self.error
        self.I_value = self.Integrator * self.Ki

        PID = self.P_value + self.I_value + self.D_value
        return self.change_output_by(PID)

    def change_pid(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    def set_output_limits(self, max, min):
        self.max = max
        self.min = min


if __name__ == "__main__":

    ypr = {'current': [0.0, 0.0, 0.0],
           'desired': [0.0, 20.0, 0.0]}
    motor_Speeds = [0, 0, 0, 0]
    a = PID(ypr,motor_Speeds,1,1,2,1,1, min = 1200, max = 2000)
    print a.compute()
    ypr['current'][1] = 15.0
    for i in range(10):
        ypr['current'][1] +=1
        print a.get_current_reference(), a.compute()
    for i in range(10):
        ypr['current'][1] -=1
        print a.get_current_reference(), a.compute()
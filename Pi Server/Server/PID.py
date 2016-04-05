class PID:
    def __init__(self, reference, output, reference_index_to_use, output_index_to_use, Kp, Ki, Kd, reverse_direction = True, max=2000, min=1000):



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
        return self.reference['current'] if self.reference_index == -1 else self.reference['current'][self.reference_index]
    def get_desired_reference(self):
        return self.reference['desired'] if self.reference_index == -1 else self.reference['desired'][self.reference_index]
    def set_output(self,val):
        self.output[self.output_index] = val

    def get_current_output(self):
        return self.output[self.output_index]
    def change_output_by(self, val):
        if self.reverse_direction:
            self.set_output(self.get_current_output() - val)

        else:
            self.set_output(self.get_current_output() + val)
        if self.get_current_output() > self.max:
            self.set_output(self.max)
        elif self.get_current_output() < self.min:
            self.set_output(self.min)

    def compute(self):
        self.error = self.get_desired_reference() - self.get_current_reference()

        self.P_value = self.Kp * self.error
        self.D_value = self.Kd * (self.error - self.Derivator)
        self.Derivator = self.error

        self.Integrator = self.Integrator + self.error
        self.I_value = self.Integrator * self.Ki

        PID = self.P_value + self.I_value + self.D_value
        self.change_output_by(PID)

    def change_pid(self, Kp, Ki, Kd):
        pass

    def set_output_limits(self, max, min):
        pass

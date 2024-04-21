class Device:
    __voltage : float
    __current : float

    def __init__(self):
        self.__voltage = 1.0
        self.__current = 0.0
        
    def _get_voltage(self):
        voltage = self.__voltage
        return voltage

    def _set_voltage(self, new_voltage):
        self.__voltage = new_voltage

    """
    @ is called a decorator in python that allows you to define a function
    that takes a function as input and returns a new function. It allows 
    in an easy way to take a function that is already written and using 
    this decorator syntaxe you mutate the inputs and also the outputs of
    a function.
    """
    @property
    def voltage(self):
        return self._get_voltage()
    
    @voltage.setter
    def voltage(self, new_voltage):
        self._set_voltage(new_voltage)

    def _get_current(self):
        current = self.__current
        return current

    def _set_current(self, new_current):
        self.__current = new_current

    @property
    def current(self):
        return self._get_current()
    
    @current.setter
    def current(self, new_current):
        self._set_current(new_current)

    @property    
    def resistance(self):
        voltage = self.voltage()
        current = self.current()
        if current == 0:
            return float('inf')
        else: 
            resistance = voltage / current
            return resistance
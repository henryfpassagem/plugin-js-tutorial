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

    def _get_current(self):
        current = self.__current
        return current

    def _set_current(self, new_current):
        self.__current = new_current
    
    def _calculate_resistance(self):
        voltage = self._get_voltage()
        current = self._get_current()
        if current == 0:
            resistance = float('inf')
        else: 
            resistance = voltage / current
        return resistance




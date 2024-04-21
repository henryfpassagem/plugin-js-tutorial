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
        



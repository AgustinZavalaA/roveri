class MockGPIO:
    BCM = 11
    OUT = 1
    IN = 0
    HIGH = 1
    LOW = 0

    def setmode(self, mode):
        pass

    def setup(self, channel, mode, initial=None):
        pass

    def output(self, channel, state):
        pass

    def input(self, channel):
        return self.LOW

    def cleanup(self):
        pass

    class PWM:
        def __init__(self, channel, frequency):
            pass

        def start(self, duty_cycle):
            pass

        def ChangeDutyCycle(self, duty_cycle):
            pass

        def stop(self):
            pass

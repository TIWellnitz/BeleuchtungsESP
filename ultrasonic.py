import machine
import time

class Ultrasonic:
    def __init__(self, trig_pin, echo_pin):
        self.trig = machine.Pin(trig_pin, machine.Pin.OUT)
        self.echo = machine.Pin(echo_pin, machine.Pin.IN)

    def distance_cm(self):
        self.trig.value(0)
        time.sleep_us(5)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        # warte auf Echo-Start
        while self.echo.value() == 0:
            pass
        start = time.ticks_us()

        # warte auf Echo-Ende
        while self.echo.value() == 1:
            pass
        end = time.ticks_us()

        # Schallgeschwindigkeit 343 m/s → Faktor 0.0343 cm/µs
        duration = time.ticks_diff(end, start)
        distance = (duration * 0.0343) / 2

        return distance
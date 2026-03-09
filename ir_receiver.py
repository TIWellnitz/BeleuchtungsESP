from machine import Pin
import time

#Receiver-Pin
ir_sensor = Pin(26, Pin.IN)

def listen():
    print("Fernbedienung betätigen")
    data = []
    #Warte auf das erste Signal
    while ir_sensor.value() == 1:
        pass

    last_tick = time.ticks_us()

#Zeichne die nächsten 100 Wechsel auf
    for i in range(100):
        current_val = ir_sensor.value()
        #Warte, bis sich der Pin ändert
        while ir_sensor.value() == current_val:
            if time.ticks_diff(time.ticks_us(), last_tick) > 200000: #Timeout 0.2s
                return data

        now = time.ticks_us()
        duration = time.ticks_diff(now, last_tick)
        data.append([current_val, duration])
        last_tick = now
    return data

results = listen()
print("AUFGEZEICHNETE DATEN:")
print(results)

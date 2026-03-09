from ultrasonic import Ultrasonic
import time
import sys

sensor_front = Ultrasonic(12, 13)
sensor_back  = Ultrasonic(27, 14)

counter = 0
state = "idle"

trigger_distance = 100

def detect(sensor):
    try:
        return sensor.distance_cm() < trigger_distance
    except:
        return False

print("INIT;SYSTEM;Counter gestartet")

def counting():
    
    global sensor_front
    global sensor_back
    global state
    global trigger_distance
    global counter
    front = detect(sensor_front)
    back  = detect(sensor_back)

    
    #Erster Sensor löst aus
    if state == "idle":
        if not front and not back:
            return
        elif front and not back:
            state = "start_entering"
            #print(f"Raum wird betreten")
        elif not front and back:
            state = "start_leaving"
            #print(f"Raum wird verlassen")
        elif front and back:
            print("INFO;SENSOR;blocked")
            return
            
    elif state == "start_entering":
        if not front and not back:
            #print("Betreten pausiert")
            state = "idle"
        elif front and not back:
            #Noch beim ersten Sensor
            pass
        elif not front and back:
            #unsicher, entweder sehr schnell oder betreten abgebrochen
            state = "entering"
        elif front and back:
            state = "entering"
        return
    
    elif state == "entering":
        if not front and not back:
            counter += 1
            print(f"COUNTER;{counter}")
            state = "idle"
        elif front and not back:
            state = "start_entering"
    
    elif state == "start_leaving":
        if not front and not back:
            #print("Raum verlassen pausiert")
            state = "idle"
        elif not front and back:
            #Noch beim ersten Sensor
            pass
        elif front and not back:
            #unsicher, sehr schnell oder Raum verlassen abgebrochen
            state = "leaving"
        elif front and back:
            #print("Raum verlassen")
            state = "leaving"
        return
    
    elif state == "leaving":
        if not front and not back:
            counter -= 1
            if counter < 0:
                counter = 0
            print(f"COUNTER;{counter}")
            state = "idle"
        elif not front and not back:
            state = "start_leaving"
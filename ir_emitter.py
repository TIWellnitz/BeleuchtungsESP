from machine import Pin, PWM
import esp32
import time
import sys
import ujson
import gc

ir_led = PWM(Pin(33), freq=38000, duty=0)

def send_signal(data):
    print("Sende neuen NEC-Code...")
    for level, duration in data:
        if level == 0:
            #0 meistens = an
            ir_led.duty(512)
        else:
            ir_led.duty(0)
        time.sleep_us(duration)

    ir_led.duty(0)
    




def get_ir(line):
    #auf serielle Daten warten
    print("read line"+line)
    if not line:
        return
    if line.startswith('['):
        try:
            #Pulsfolge als JSON empfangen
            gc.collect()
            pulses = ujson.loads(line)
            send_signal(pulses)
            print("IR Signal gesendet")
            gc.collect()
        except Exception as e:
            print("Fehler beim Senden:", e)
        else:
            pass
from machine import Pin, PWM
import esp32
import time
import sys
import ujson

ir_led = PWM(Pin(33), freq=38000, duty=0)

def send_signal(data):
    print("Sende neuen NEC-Code...")
    for level, duration in data:
        if level == 0:
            # Bei NEC bedeutet der 0-Level vom Receiver meistens: LED AN
            ir_led.duty(512)
        else:
            ir_led.duty(0)
        time.sleep_us(duration)

    ir_led.duty(0)
    




def get_ir():
    # auf serielle Daten warten
    line = sys.stdin.readline()
    print("read line"+line)
    if not line:
        return
    try:
        # Pulsfolge als JSON empfangen
        pulses = ujson.loads(line)
        for i in range (3):
            send_signal(pulses)
        print("IR Signal gesendet")
    except Exception as e:
        print("Fehler beim Senden:", e)
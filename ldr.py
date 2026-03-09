from machine import ADC, Pin
import time

ldr = ADC(Pin(32))
ldr.atten(ADC.ATTN_11DB)

print("INIT;SYSTEM;Lichtsensor aktiv")

def get_lightpercent():
    try:
        light_value = ldr.read()
        
        #Umrechnung der Werte in Prozent
        light_percent = round((light_value / 4095) * 100, 1)
        
        #senden an Pi
        print(f"LIGHT;{light_percent}")
        return light_percent
    
    except Exception as e:
        print(f"ERROR;LDR;{e}")
import time
import counter
import ldr
import ir_emitter
import select
import machine
import sys


print("warte 10 Sekunden um Programm abbrechen zu können")
time.sleep(10)


sleep_counter = 0
last_counter_send = 0

def handle_input():
    #USB-Puffer auf Daten prüfen
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline().strip()
        if not line:
            return

        #Reset-Check
        if line == "RESET_NOW":
            print("Reset-Befehl erkannt!")
            machine.reset()

        #IR-Check: Zeile an Emitter weitergeben
        elif line.startswith('['):
            ir_emitter.get_ir(line) 

        else:
            print(f"INFO;Empfangen: {line}")


while True:
    time.sleep_ms(10)
    handle_input()

    try:
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, last_counter_send) > 200:
            counter.counting()
            last_counter_send = current_time
        if sleep_counter == 300:
            ldr.get_lightpercent()
            sleep_counter = 0
    except Exception as e:
        print(f"Error;konnte Counter nicht laden: {e}")
    sleep_counter += 1



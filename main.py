import time
import counter
import ldr
import ir_emitter
import _thread


print("warte 20 Sekunden um Programm abbrechen zu können")
time.sleep(20)


sleep_counter = 0
last_counter_send = 0

def ir_receive():
    while True:
        ir_emitter.get_ir()
        
_thread.start_new_thread(ir_receive, ())

while True:
    time.sleep_ms(10)

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



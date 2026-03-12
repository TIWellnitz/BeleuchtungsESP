
# ESP32 Room Sensor & IR Controller

ESP32-based sensor system that detects room occupancy, measures ambient light, and can transmit infrared remote control signals.
The ESP32 communicates with a Raspberry Pi via serial interface(further details are described in the Bonehilda repository).

This project arose from the idea to create my own automated lighting control system for my home. It also serves as a portfolio project to demonstrate my knowledge of embedded programming with MicroPython, sensor integration, and the implementation of state machines in a real-world application.


## Features

- Room occupancy detection using two ultrasonic sensors
- State-machine based direction detection (entering / leaving)
- Ambient light measurement using LDR
- Infrared signal transmitter for remote control devices
- Serial communication with Raspberry Pi
- Modular code structure

## Hardware

- ESP32
- 2 × Ultrasonic Distance Sensors
- LDR (Light Dependent Resistor)
- IR LED
- Resistors
- Transistor
- Raspberry Pi 5 (serial communication partner)
## main.py

Central program loop.

Responsibilities:

- receives commands via serial
- triggers sensor measurements
- sends data to Raspberry Pi
- forwards IR commands to the IR module

The program checks:

- incoming serial commands
- counter updates every ~200 ms
- periodic light sensor measurements
## Serial Communication

Currently, the ESP32 uses structured serial messages for communication. This wired approach ensures high reliability during the development phase, with plans to transition to wireless protocols like MQTT in the next version to create a truly de-centralized smart home network.
## Occupancy Detection

instead of motion triggers, this system uses a dual-ultrasonic sensor setup to determine the direction of movement (entry vs. exit).

State Machine Logic: Implemented in counter.py, the system tracks the sequence of sensor interruptions to accurately increment or decrement the room's occupancy count.

Reliability: This approach ensures the lights only react when the room's actual occupancy state changes, preventing "false offs" when a person is simply sitting still.
## Light Intensity Monitoring

The system tracks ambient light levels to determine when artificial lighting is actually required.

Implemented in ldr.py, the script samples the analog signal from an LDR via the ESP32's 12-bit ADC.

Raw values (0–4095) are mapped to a human-readable percentage scale (0–100%) to simplify threshold logic on the Hub side.

Conversion Logic:
light_percent = ADC_value/4095*100

## IR Signal

A versatile IR remote control interface that allows the Raspberry Pi to control any 38kHz infrared device.

Instead of hardcoding static hex codes, the system processes raw pulse-duration pairs. This allows the emulation of various protocols (NEC, RC5, etc.) without changing the ESP32 firmware.

Implemented in ir_emitter.py, the system generates a 38kHz carrier frequency using the ESP32’s PWM hardware for signal stability.

Utilizes ujson for lightweight data parsing and gc.collect() for proactive memory management during large signal bursts.
## Authors

- [@Tony](https://www.github.com/TIWellnitz)


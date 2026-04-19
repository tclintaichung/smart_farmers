from machine import Pin
import time

# Define pins
relay_pin = Pin(9, Pin.OUT)        # GPIO9 → Relay IN
button_pin = Pin(10, Pin.IN, Pin.PULL_UP)  # GPIO4 → Push button
# Initial states
relay_pin.value(0)

print("System ready. Press button to start motor.")

while True:
    if button_pin.value() == 0:   # Button pressed (LOW)
        relay_pin.value(1)        # Relay ON
    else:
        relay_pin.value(0)        # Relay OFF
    time.sleep(0.01) 

    

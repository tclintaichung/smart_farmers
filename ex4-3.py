from machine import Pin
import time
import dht

# Configuration
sensor = dht.DHT22(Pin(11))

def measure_temp():
    sensor.measure()
    temp = sensor.temperature()
    humi = sensor.humidity()
    print(f"Temp = {temp}/Humi = {humi}")

# Main loop
while True:
    time.sleep(1)
    measure_temp()
    time.sleep(1)

from machine import Pin, PWM
import time

# Use GPIO18 for servo signal
servo = PWM(Pin(12), freq=50)  # 50 Hz for servo

def set_angle(angle):
    # Convert angle (0–180) to duty cycle
    # MG995 expects ~0.5 ms to 2.5 ms pulse width
    min_us = 500
    max_us = 2500
    us = min_us + (max_us - min_us) * angle / 180
    duty = int(us * 1023 * 50 / 1000000)  # convert to duty for ESP32 PWM
    servo.duty(duty)

# Sweep servo
for angle in range(0, 181, 30):
    set_angle(angle)
    time.sleep(1)

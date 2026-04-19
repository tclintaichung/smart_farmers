from machine import Pin, PWM
import time

# Define LED pin (GPIO 8)
led_pin = Pin(8, Pin.OUT)

# Create PWM object on that pin
pwm = PWM(led_pin)

# Set frequency (Hz) – 500–1000 Hz is good for LEDs
pwm.freq(1000)

# Duty cycle range: 0–1023
# 0 = OFF, 1023 = full brightness
pwm.duty(0)   # start OFF

# Example: fade LED in and out
while True:
    # Fade in
    for duty in range(0, 1024, 32):
        pwm.duty(duty)
        time.sleep(0.05)
    # Fade out
    for duty in range(1023, -1, -32):
        pwm.duty(duty)
        time.sleep(0.05)

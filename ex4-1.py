from machine import Pin
from time import sleep

# 設置 GPIO4 為輸出模式
led = Pin(8, Pin.OUT)

while True:
    led.value(1)  # 打開 LED
    sleep(1.5)    # 延遲 500 毫秒
    led.value(0)  # 關閉 LED
    sleep(1.5)    # 延遲 500 毫秒



import network
import time
from machine import Pin
from umqtt.robust2 import MQTTClient

# Wi-Fi credentials
ssid = 'mayandtclin'
password = '11041022'
# Wi-Fi 連線
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    time.sleep(1)

# LED 腳位
led = Pin(8, Pin.OUT)  # ESP32 開發板內建 LED 通常在 GPIO2

# MQTT 訊息回呼
def sub_cb(topic, msg, retained, duplicate):
    print((topic, msg))
    if msg == b"ON":
        led.value(1)
    elif msg == b"OFF":
        led.value(0)

# 連線到 Broker
client = MQTTClient("esp32_client", "192.168.0.121", user="", password="")
client.set_callback(sub_cb)
client.connect()
client.subscribe('smart_farmer00/fan')

print("等待 MQTT 訊息...")
while True:
    client.wait_msg()

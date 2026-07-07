import network
import time
from machine import Pin
import dht
from umqtt.robust2 import MQTTClient

# Wi-Fi credentials
ssid = '****'
password = '****'

#mqtt_server = 'broker.hivemq.com'
mqtt_server = '192.168.0.121'
mqtt_client_id = 'esp32-s3'

# DHT sensor initialization
sensor = dht.DHT22(Pin(11)) 

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to WiFi')
    print(wlan.ifconfig())

# Connect to MQTT broker
def connect_mqtt():
    client = MQTTClient(mqtt_client_id, mqtt_server)
    client.connect()
    return client

# Publish temperature data to ThingSpeak
def publish_temperature(client):
    try:
        sensor.measure()
        temp = sensor.temperature()
        humi = sensor.humidity()
        payload = f'temp={temp}/humi={humi}'
        client.publish('smart_farmer00/temp_humi', payload)
        print('Published: {}'.format(payload))
    except OSError as e:
        print('Failed to read sensor.')

# Main program
connect_wifi()
client = connect_mqtt()

while True:
    publish_temperature(client)
    time.sleep(20)  # Publish every 20 seconds

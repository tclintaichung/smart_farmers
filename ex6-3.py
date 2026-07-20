import ubluetooth
import dht
from machine import Pin
import time

# DHT11 sensor on GPIO11
dht_sensor = dht.DHT22(Pin(11))

# BLE setup
ble = ubluetooth.BLE()
ble.active(True)

# UUIDs for Nordic UART Service (NUS)
NUS_SERVICE_UUID = ubluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
RX_CHAR_UUID     = ubluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")
TX_CHAR_UUID     = ubluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

rx_char = (RX_CHAR_UUID, ubluetooth.FLAG_WRITE)
tx_char = (TX_CHAR_UUID, ubluetooth.FLAG_NOTIFY)
nus_service = (NUS_SERVICE_UUID, (tx_char, rx_char))

handles = ble.gatts_register_services((nus_service,))
tx_handle, rx_handle = handles[0][0], handles[0][1]

conn_handle = None

def bt_irq(event, data):
    global conn_handle
    if event == 1:  # _IRQ_CENTRAL_CONNECT
        conn_handle, _, _ = data
        print("Central connected")
    elif event == 2:  # _IRQ_CENTRAL_DISCONNECT
        conn_handle = None
        print("Central disconnected")
        ble.gap_advertise(100, adv_data)

ble.irq(bt_irq)

# Advertise with name
adv_data = bytes([
    0x02, 0x01, 0x06,
    0x07, 0x09
]) + b"ESP_00"

ble.gap_advertise(100, adv_data)

print("BLE NUS ready, DHT22 on Pin 11")

# Periodically read sensor and notify client
while True:
    try:
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()
        msg = "T:{}C H:{}%".format(temp, hum)
        print("Notify:", msg)
        if conn_handle is not None:
            ble.gatts_notify(conn_handle, tx_handle, msg.encode())
    except Exception as e:
        print("DHT error:", e)
    time.sleep(5)
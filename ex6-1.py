import ubluetooth
from machine import Pin

# LED pin
led = Pin(8, Pin.OUT)

# UUIDs for Nordic UART Service (NUS)
NUS_SERVICE_UUID = ubluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")
RX_CHAR_UUID     = ubluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")
TX_CHAR_UUID     = ubluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E")

# BLE setup
ble = ubluetooth.BLE()
ble.active(True)

# Define RX characteristic (write) and TX characteristic (notify)
rx_char = (RX_CHAR_UUID, ubluetooth.FLAG_WRITE)
tx_char = (TX_CHAR_UUID, ubluetooth.FLAG_NOTIFY)

nus_service = (NUS_SERVICE_UUID, (tx_char, rx_char))

# Register GATT server
handles = ble.gatts_register_services((nus_service,))
tx_handle, rx_handle = handles[0][0], handles[0][1]

# IRQ handler
def bt_irq(event, data):
    if event == 3:
        conn_handle, attr_handle = data
        if attr_handle == rx_handle:
            value = ble.gatts_read(rx_handle)
            print("RX:", value)
            if value == b"ON":
                led.value(1)
            elif value == b"OFF":
                led.value(0)

ble.irq(bt_irq)

# Advertise
adv_data = bytes([
    0x02, 0x01, 0x06,  # Flags
    0x0A, 0x09, 
]) + b"ESP32_NUS"

ble.gap_advertise(100, adv_data)

print("BLE NUS ready, connect and send 'ON'/'OFF'")

import network, time

SSID = "mayandtclin"
PASSWORD = "11041022"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

print("Connecting to WiFi...")
sta_if.connect(SSID, PASSWORD)

retry = 0
while not sta_if.isconnected() and retry < 15:
    time.sleep(1)
    retry += 1
    print("Retry:", retry)

if sta_if.isconnected():
    print("WiFi connected:", sta_if.ifconfig())
else:
    print("WiFi connection failed")

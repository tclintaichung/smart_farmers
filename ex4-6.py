import esp32

temp = esp32.mcu_temperature()   # 單位：攝氏度
print("CPU Temperature:", temp, "°C")

import serial, time

arduino = serial.Serial("COM3", 9600)
time.sleep(10)
arduino.write(b"VERDE")
time.sleep(10)
arduino.write(b"BLANCO")
time.sleep(10)
arduino.write(b"LA VERDAD ES QUE QUESO")

message = arduino.readline().decode("utf-8").rstrip()
print(message)
print(f"len(message) = {len(message)}")
arduino.close()

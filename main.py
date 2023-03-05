import serial

ser = serial.Serial()
ser.baudrate = 2000
ser.port = "/dev/ttyUSB0"
ser.dtr = False
ser.timeout = 0.5
ser.open()

ser.flushInput()

while True:
    pack = ser.read(1024)
    print(pack)
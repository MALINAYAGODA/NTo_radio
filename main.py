import serial

ser = serial.Serial()
ser.baudrate = 2000
ser.port = "/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.2:1.0-port0"
ser.dtr = False
ser.timeout = 0.5
ser.open()

ser.flushInput()

while True:
    pack = ser.read(1024)
    print(pack)

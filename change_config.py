from time import time, sleep

import serial

sv610 = serial.Serial()
sv610.baudrate = 9600
sv610.port = "/dev/ttyUSB0"
# sv610.dtr = False
sv610.setDTR(True)
sv610.open()
sv610.flushInput()
sv610.reset_input_buffer()
#sleep(0.1)
# sv610.setDTR(False)
sv610.setDTR(True)
#sleep(0.1)
# sleep(3)
old_time= time()
# sv610.write(b'\xaa\xfa\x03\x23\x01\x07\x07\x07\x02\x01\x01\x00\x00\x00\x00\x00\x00')
sv610.write(b'\xaa\xfa\x01')
print('start')
line = b''
while True:
    if sv610.in_waiting > 0:
        line += sv610.read(1)
        print(line)
    if abs(old_time - time()) > 2:
        break
sv610.setDTR(False)

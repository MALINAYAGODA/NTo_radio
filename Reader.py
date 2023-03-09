from time import time
from serial import Serial

class Reader:
    def __init__(self, a_serial:Serial , max_delay = 1, eol=b'\t\n\t\n'):
        self.a_serial= a_serial
        self.eol = eol
        self.max_delay= max_delay
        self.leneol = len(eol)
        self.line = bytearray()

    def readline(self):
        time_old = time()
        flag = True
        while True:
            # print('while')
            # print('self.a_serial.in_waiting =', self.a_serial.in_waiting)
            # if self.a_serial.in_waiting > 0:
            c = self.a_serial.read(1)
            if len(self.line) < 10:
                print(c)
            # print('read 1 bit')
            if c:
                # print('c')
                self.line += c
                if self.line[-self.leneol:] == self.eol:
                    # print('if eol')
                    break
            else:
                # print('not c')
                break
            # print(time)
            # if abs(time_old - time()) > self.max_delay and self.a_serial.in_waiting == 0:
            #     # print('max time')
            #     flag = False
            #     # print(flag)
            #     break
        # print('end')
        if flag:
            a = bytes(self.line)
            self.line = bytearray()
            return a[:-self.leneol:]
        return b''
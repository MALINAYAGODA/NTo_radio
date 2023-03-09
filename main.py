from time import sleep, time
import json
import serial
from Reader import Reader
import requests
import imageio.v3 as iio
from pprint import pprint

def bits_to_str(bits):
    with open("my_file_radio.txt", "wb") as binary_file:
        # Write bytes to file
        binary_file.write(bits)
    webm_bytes = bits
    pprint(webm_bytes)
    print(b'\xad\xdd\x06\x24\x01\x07\x07\x07\x02\x01\x01\x00\x00\x00\x00\x00\x00' == webm_bytes)
    print(type(bits))
    frames = iio.imread(webm_bytes)
    exit(0)
    print('1) ', frames.shape)
    st = frames.ravel().tolist()
    str_res = ''
    for i in st:
        str_res += str(i) + ';'
    return str_res

BASE_URL = 'http://10.8.0.5:5000/'

sv610 = serial.Serial()
sv610.baudrate = 57600
sv610.port = "/dev/ttyUSB0"
sv610.dtr = False
# sv610.timeout = 0.5
sv610.open()
sv610.flushInput()
sv610.reset_input_buffer()

reader = Reader(sv610, max_delay=1)
print(serial.__version__)

dct_camera = {"camera": b''}

def reading_data():
    global dct_camera
    read_data = reader.readline()
    print('read_data', '=', read_data)
    if read_data != '':
        dct_camera["camera"] = read_data
    return None


sv610.reset_input_buffer()
time_old = time()
while True:
    print('reading')
    reading_data()
    print('end reading: ', (time() - time_old) * 1000)
    time_old = time()

    print('post server')
    dct_camera["camera"] = bits_to_str(dct_camera["camera"])
    response = requests.post(f"{BASE_URL}/", json=dct_camera, timeout=1)
    print('post server end:',(time() - time_old) * 1000 )
    time_old = time()

    # sleep(0.2)
    print('write')
    sv610.write((json.dumps(response) + '\n').encode("utf-8"))
    print('end writing: ', (time() - time_old) * 1000)
    time_old = time()


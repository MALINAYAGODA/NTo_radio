# import json
# from time import sleep, time
#
# import serial
#
# import rospy
#
# from std_msgs.msg import String
# from std_msgs.msg import Int64
#
# rospy.init_node("SV610")
#
# sv610 = serial.Serial()
# sv610.baudrate = 9600
# sv610.port = "/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.2:1.0-port0"
# sv610.dtr = False
# # sv610.timeout = 0.5
# sv610.open()
# sv610.flushInput()
# sv610.reset_input_buffer()
#
# pub_move = rospy.Publisher("move_key", String, queue_size=10)
# pub_speed = rospy.Publisher("speed_movement", Int64, queue_size=10)
#
# move_s = String()
# speed_int64 = Int64()
#
# interval = 0.001
#
# def reading_data():
#     global move_s
#     global speed_int64
#     read_data = sv610.read_until('\n'.encode("utf-8")).decode("utf-8")
#     if read_data != '':
#         try:
#             dct = json.loads(read_data)
#             print(dct)
#             move_s = dct['move']
#             speed_int64 = dct['speed']
#             pub_move.publish(move_s)
#             pub_speed.publish(speed_int64)
#             return True
#         except json.JSONDecodeError as e:
#             print("JSON:", e, read_data)
#             return False
#         except KeyError as e:
#             print("KeyError", e)
#             return False
#     return None
#
# old_time = 0
# flag = False
#
# sv610.reset_input_buffer()
# while not rospy.is_shutdown():
#     sv610.reset_input_buffer()
#     while True:
#         resp = reading_data()
#         if resp is not None:
#             if resp:
#                 break
#             else:
#                 sv610.write(b'Error\n')
#     sleep(interval)
#     sv610.write(b'OK\n')
#     sleep(interval)
#     sv610.reset_input_buffer()
#     old_time = 0
#     while True:
#         if abs(round(time() - old_time, 1)) > 0.5:
#             sv610.write(json.dumps({"camera": 123}).encode("utf-8"))
#             old_time = time()
#         if sv610.readline().decode("utf-8") == 'Error\n':
#             sv610.reset_input_buffer()
#             old_time = 0
#         elif sv610.readline().decode("utf-8") == 'OK\n':
#             break
#         if sv610.in_waiting != 0:
#             flag = True
#         if flag:
#             flag = False
# from __future__ import print_function
# import imageio.v3 as iio
#
import requests
BASE_URL = 'http://localhost:5000'
#
# def bits_to_str(bits):
#     webm_bytes = bits
#     frames = iio.imread(webm_bytes)
#     print('1) ', frames.shape)
#     st = frames.ravel().tolist()
#     str_res = ''
#     for i in st:
#         str_res += str(i) + ';'
#     return str_res
#
# response = requests.post(f"{BASE_URL}/", json={"img": callback(b'11001100')})
# print(response.text)

import imageio.v3 as iio
def bits_to_str(bits):
    # with open("my_file_radio.txt", "wb") as binary_file:
    #     # Write bytes to file
    #     binary_file.write(bits)
    webm_bytes = bits
    # pprint(webm_bytes)
    frames = iio.imread(webm_bytes)
    st = frames.ravel().tolist()
    str_res = ''
    for i in st:
        str_res += str(i) + ';'
    return str_res

dct = {'camera': bits_to_str(open('my_file_test.txt', 'rb'))}

response = requests.post(f"{BASE_URL}/", json=dct, timeout=1)
print(response.json())
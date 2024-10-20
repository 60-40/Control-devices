import socket
import time
from os import path

host = "192.168.2.165"
port = 2001
START_PKG = b'\xff'
DEVICE_TYPE = b'\x06'
CONTROL1_BYTE = b'\x02'
DATA_BYTE_1 = b'\x00'
PKG_END = b'\xFF'


def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            print("sending command", command)
            sock.connect((host, port))

            sock.sendall(command)
            # print(1234)
            # res = sock.recvmsg(5)
            # print(sock.recvmsg(5))
            # print(res[0])
            # print(res[0][3])
            # time.sleep(1)
            return True
    except socket.error as e:
        print(f"Ошибка {e}")
        return False


n = 2
while True:
    # command = b'\xff\x40\x19\x03\xff'
    result1 = send_command(START_PKG + DEVICE_TYPE + CONTROL1_BYTE + DATA_BYTE_1 + PKG_END)
    # result2 = send_command(b'\xff\x41\x02\x1a\xff') # beep

    # if not result1 or not result2:
    #     break
    time.sleep(0.5)
#
#     # command = b'\xff\x40\x19\x08\xff'
#     # result1 = send_command(
#     #     START_PKG + DEVICE_TYPE + CONTROL1_BYTE + DATA_BYTE_2 + PKG_END)
#     # result2 = send_command(
#     #     START_PKG + DEVICE_TYPE + CONTROL2_BYTE + DATA_BYTE_2 + PKG_END)
#
#     # if not result1 or not result2:
#     #     break
#
#     # time.sleep(1)
#     # result1 = send_command(START_PKG + DEVICE_TYPE + b'\x00' + DATA_BYTE_1 + PKG_END)
#     # time.sleep(1)
# #
# #     # n *= 0.7

from sensors import SensorProvider
from irf import IRFSensor
from ultrasonic import Ultrasonic

sensor_provider = SensorProvider()
sensor_provider.main_loop()

ultrasonic = Ultrasonic()
ultrasonic.enable()

irf = IRFSensor()
irf.enable()

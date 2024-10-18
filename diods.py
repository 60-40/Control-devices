import socket
import time
from os import path

host = "192.16z8.2.165"
port = 2001
START_PKG = b'\xff'
DEVICE_TYPE = b'\x13'
CONTROL1_BYTE = b'\x05'
DATA_BYTE_1 = b'\x00'
PKG_END = b'\xFF'


def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))

            sock.sendall(command)
            print(1234)
            # print(sock.recvmsg(5))
            time.sleep(1)
            return True
    except socket.error as e:
        print(f"Ошибка {e}")
        return False


while True:
    command = b'\xff\x06\x02\x07\xff'
    # command = b'\xff\x40\x19\x08\xff'


    # result1 = send_command(START_PKG + DEVICE_TYPE + CONTROL1_BYTE + DATA_BYTE_1 + PKG_END)
    # result2 = send_command(START_PKG + DEVICE_TYPE + CONTROL1_BYTE + DATA_BYTE_1 + PKG_END)
    send_command(command)
    # break
    # if not result1 or not result2:
    #     break
    # time.sleep(0.5)
    #
    # command = b'\xff\x40\x19\x08\xff'
    # result1 = send_command(
    #     START_PKG + DEVICE_TYPE + CONTROL1_BYTE + DATA_BYTE_2 + PKG_END)
    # result2 = send_command(
        # START_PKG + DEVICE_TYPE + CONTROL2_BYTE + DATA_BYTE_2 + PKG_END)
    time.sleep(0.1)
    # if not result1 or not result2:
    #     break
    # time.sleep(0.5)

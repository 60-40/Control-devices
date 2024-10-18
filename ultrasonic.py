from device import Device
from sensors import SensorProvider

host = "192.168.2.165"
port = 2001


class Ultrasonic(Device):
    sensor: SensorProvider
    DEVICE_TYPE = b'\x13'
    CONTROL_BYTE = b'\x05'

    def __init__(self):
        super().__init__()
        self.sensor = SensorProvider()

    def enable(self):
        self.sensor.register_device(self, 49, 2)
        self.send_command(self.PKG_START + self.DEVICE_TYPE + self.CONTROL_BYTE + b'\00' + self.PKG_END)

    def disable(self):
        self.sensor.delete_device(49, 2)

    def get_event(self, data: int):
        print(f"Расстояние: {data}")


# def send_command(command):
#     try:
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#             print("sending command", command)
#             sock.connect((host, port))
#
#             sock.sendall(command)
#             print(1234)
#             res = sock.recvmsg(5)
#             print(res)
#             for i in range(len(res[0])):
#                 print(res[0][i])
#             print(res[0])
#             time.sleep(1)
            # return True
    # except socket.error as e:
    #     print(f"Ошибка {e}")
    #     return False
#
#
# def get_command():
#     while True:
#         try:
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#                 print("getting command")
#                 sock.connect((host, port))

                # sock.sendall(command)
                # print(1234)
                # res = sock.recvmsg(5)
                # print(sock.recvmsg(5))
                # print(res[0])
                # print(res[0][3])
                # time.sleep(1)
                # return True
        # except socket.error as e:
        #     print(f"Ошибка {e}")
        #     return False
#

# def main():
    # send_command(START_PKG + DEVICE_TYPE + CONTROL1_BYTE + DATA_BYTE_1 + PKG_END)
    # get_command()


# if __name__ == "__main__":
#     main()

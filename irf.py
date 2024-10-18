import socket

from device import Device
from sensors import SensorProvider

host = "192.168.2.165"
port = 2001
START_PKG = b'\xff'
DEVICE_TYPE = b'\x42'
CONTROL1_BYTE = b'\x01'
DATA_BYTE_1 = b'\x00'
PKG_END = b'\xFF'


class IRFSensor(Device):
    sensor: SensorProvider
    DEVICE_TYPE = b'\x42'
    CONTROL_BYTE = b'\x01'

    def __init__(self):
        super().__init__()
        self.sensor = SensorProvider()

    def enable(self):
        self.sensor.register_device(self, 49, 3)
        self.send_command(self.PKG_START + self.DEVICE_TYPE + self.CONTROL_BYTE + b'\01' + self.PKG_END)

    def disable(self):
        self.sensor.delete_device(49, 3)
        self.send_command(self.PKG_START + self.DEVICE_TYPE + self.CONTROL_BYTE + b'\00' + self.PKG_END)

    def get_event(self, data: int):
        print(f"Справа свободно: {data % 2}")
        print(f"Слева свободно: {data // 2 % 2}")



def send_command(command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            print("sending command", command)
            sock.connect((host, port))

            sock.sendall(command)
            return True
    except socket.error as e:
        print(f"Ошибка {e}")
        return False


def get_command():
    ...


def main():
    send_command(START_PKG + DEVICE_TYPE + CONTROL1_BYTE + DATA_BYTE_1 + PKG_END)
    get_command()


if __name__ == "__main__":
    main()

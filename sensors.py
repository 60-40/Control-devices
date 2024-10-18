import socket
import time

from device import Device, thread_decorator


class SensorProvider(Device):
    instance = None
    devices = {}

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(SensorProvider, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def get_command(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            while True:
                try:
                    # print("getting command")
                    res = sock.recv(5)
                    # print(res)
                    time.sleep(0.1)
                    yield res
                except socket.error as e:
                    print(f"Ошибка {e}")
                    return False

    @thread_decorator
    def main_loop(self):
        gen = self.get_command()
        while True:
            command = next(gen)
            device = self.devices.get((command[1], command[2]), None)
            if device is not None:
                device.get_event(command[3])

    def register_device(self, device: Device, device_type: int, control_id: int):
        self.devices[(device_type, control_id)] = device

    def delete_device(self, device_type: int, control_id: int):
        if (device_type, control_id) in self.devices:
            del self.devices[(device_type, control_id)]


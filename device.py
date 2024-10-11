import socket
from abc import ABC
from config import host, port


class Device(ABC):
    host: str = host
    port: int = port
    PKG_START: bytes = b'\xff'
    PKG_END: bytes = b'\xFF'

    def send_command(self, command):
        print(f'Sending command: {command}')
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.host, self.port))

                sock.sendall(command)
                return True
        except socket.error as e:
            print(f"Ошибка {e}")
            return False

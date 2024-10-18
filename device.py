import socket
import threading
from abc import ABC
from config import host, port


def thread_decorator(func):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.start()
    return wrapper


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

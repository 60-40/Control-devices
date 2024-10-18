import socket
import time
import struct

from device import Device

host = "192.168.2.165"
port = 2001


class Servo(Device):
    DIRECTION_DEVICE_BYTE = b'\x01'
    id: int
    angle: int
    default_angles = {
        1: 160,
        2: 150,
        3: 80,
        4: 0,
        7: 99,
        8: 0
    }

    def __init__(self, id_: int):
        self.id = id_
        self.angle = self.default_angles.get(id_, 90)

    def set_default_angle(self):
        self.angle = self.default_angles.get(self.id, 90)
        self.update_angle()

    def update_angle(self):
        self.send_command(self.PKG_START + self.DIRECTION_DEVICE_BYTE +
                          struct.pack('B', self.id) + struct.pack('B', self.angle) + self.PKG_END)

    def move_right(self, diff: int):
        self.angle += diff
        if self.angle > 180:
            self.angle = 180
        self.update_angle()

    def move_left(self, diff: int):
        self.angle -= diff
        if self.angle < 0:
            self.angle = 0
        self.update_angle()

    def set_angle(self, angle: int):
        self.angle = angle
        self.update_angle()

    def get_angle(self) -> int:
        return self.angle


class Manipulator(Device):
    def __init__(self):
        self.servo1 = Servo(1)
        self.servo2 = Servo(2)
        self.servo3 = Servo(3)
        self.servo4 = Servo(4)

    def set_default(self):
        self.servo4.set_default_angle()
        self.servo3.set_default_angle()
        self.servo1.set_default_angle()
        self.servo2.set_default_angle()

    def press_button(self):
        self.servo1.set_angle(60)
        time.sleep(0.5)
        self.set_default()

    def grub_item(self):
        self.servo1.set_angle(120)
        self.servo3.set_angle(40)
        self.servo2.set_angle(60)
        self.servo4.set_angle(90)

        time.sleep(0.5)
        self.servo1.set_angle(100)
        time.sleep(0.5)
        self.servo3.set_angle(80)
        time.sleep(0.5)
        self.servo3.set_angle(100)
        self.servo2.set_angle(130)
        time.sleep(0.5)
        self.servo4.set_angle(0)
        time.sleep(0.5)

        self.set_default()

    def put_item(self):
        self.servo1.set_angle(150)
        self.servo4.set_angle(100)
        self.servo2.set_angle(80)
        time.sleep(0.7)
        self.servo3.set_angle(40)
        time.sleep(0.7)
        self.set_default()

    def put_item_into_basket(self):
        self.servo1.set_angle(130)
        self.servo2.set_angle(80)
        time.sleep(0.7)
        self.servo4.set_angle(80)
        time.sleep(0.7)
        self.servo3.set_angle(40)
        time.sleep(0.7)
        self.servo3.set_default_angle()
        self.servo4.set_default_angle()
        time.sleep(0.7)
        self.set_default()


def main():
    # set_default()
    manipulator = Manipulator()
    manipulator.set_default()
    # manipulator.put_item_into_basket()
    # manipulator.press_button()
    # manipulator.grub_item()
    # manipulator.put_item()
    servo8 = Servo(8)
    # servo1 = Servo(1)
    # servo2 = Servo(2)
    # servo3 = Servo(3)
    # servo4 = Servo(4)
    servo7 = Servo(7)
    #
    def set_default():
    #     servo1.set_default_angle()
    #     servo2.set_default_angle()
    #     servo3.set_default_angle()
    #     servo4.set_default_angle()
        servo7.set_default_angle()
        servo8.set_default_angle()
    set_default()

if __name__ == "__main__":
    main()

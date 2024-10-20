import threading
import struct
import time
from enum import Enum
from device import Device, thread_decorator


class Direction(Enum):
    stop = b'\x00'
    forward = b'\x01'
    backward = b'\x02'
    left = b'\x03'
    right = b'\x04'


class Motor(Device):
    DIRECTION_DEVICE_BYTE = b'\x00'
    SPEED_DEVICE_BYTE = b'\x02'

    def set_direction(self, direction: Direction):
        self.send_command(self.PKG_START + self.DIRECTION_DEVICE_BYTE +
                          direction.value + b'\x00' + self.PKG_END)

    def set_left_speed(self, speed: int):
        self.send_command(self.PKG_START + self.SPEED_DEVICE_BYTE + b'\x01' + struct.pack('B', abs(speed) % 100) + struct.pack('B', int(speed < 0)) + self.PKG_END)

    def set_right_speed(self, speed: int):
        self.send_command(self.PKG_START + self.SPEED_DEVICE_BYTE + b'\x02' + struct.pack('B', abs(speed) % 100) + struct.pack('B', int(speed < 0)) + self.PKG_END)

    def set_speed(self, speed: int):
        self.set_right_speed(speed)
        self.set_left_speed(speed)

    def send_error(self, ex: int, ey: int):
        self.send_command(self.PKG_START + b'\x43' + struct.pack('B', ex))


class MotorController:
    motor: Motor
    cur_left_speed = 50
    cur_right_speed = 50
    cur_direction: Direction = Direction.stop

    @thread_decorator
    def set_right_speed(self, speed: int):
        self.cur_right_speed = speed
        if self.cur_right_speed > 100:
            self.cur_right_speed = 100
        if self.cur_right_speed < -100:
            self.cur_right_speed = -100
        self.motor.set_right_speed(self.cur_right_speed)

    @thread_decorator
    def set_left_speed(self, speed: int):
        self.cur_left_speed = speed
        if self.cur_left_speed > 100:
            self.cur_left_speed = 100
        if self.cur_left_speed < -100:
            self.cur_left_speed = -100
        self.motor.set_left_speed(self.cur_left_speed)

    def __init__(self):
        self.motor = Motor()
        # self.motor.set_speed(self.cur_right_speed)

    @thread_decorator
    def stop(self):
        self.motor.set_direction(Direction.stop)

    @thread_decorator
    def forward(self):
        self.cur_direction = Direction.forward
        self.motor.set_direction(self.cur_direction)

    @thread_decorator
    def backward(self):
        self.cur_direction = Direction.backward
        self.motor.set_direction(self.cur_direction)

    @thread_decorator
    def move_forward(self, moving_time: int):
        # self.forward()
        self.motor.set_speed(50)
        time.sleep(moving_time)
        self.stop()


    # @thread_decorator
    # def increase_speed(self):
    #     self.add_right_speed(10)
    #     self.add_left_speed(10)
    #     self.motor.set_right_speed(self.cur_right_speed)
    #     self.motor.set_left_speed(self.cur_left_speed)
    #     print(f"left speed: {self.cur_left_speed}    right: {self.cur_right_speed}")
    #
    # @thread_decorator
    # def degrease_speed(self):
    #     self.add_right_speed(-10)
    #     self.add_left_speed(-10)
    #     self.motor.set_right_speed(self.cur_right_speed)
    #     self.motor.set_left_speed(self.cur_left_speed)
    #     print(f"left speed: {self.cur_left_speed}    right: {self.cur_right_speed}")
    #
    # @thread_decorator
    # def right(self):
    #     self.add_right_speed(-10)
    #     self.add_left_speed(+10)
    #
    #     print(f"left speed: {self.cur_left_speed}    right: {self.cur_right_speed}")
    #     self.motor.set_right_speed(self.cur_right_speed)
    #     self.motor.set_left_speed(self.cur_left_speed)
    #
    # @thread_decorator
    # def left(self):
    #     self.add_right_speed(+10)
    #     self.add_left_speed(-10)40
    #
    #     print(f"left speed: {self.cur_left_speed}    right: {self.cur_right_speed}")
    #     self.motor.set_right_speed(self.cur_right_speed)
    #     self.motor.set_left_speed(self.cur_left_speed)

#
# def main():
#     import keyboard
#
#     controller = MotorController()
#     keyboard.add_hotkey('p', controller.stop)
#     keyboard.add_hotkey('w', controller.forward)
#     keyboard.add_hotkey('s', controller.backward)
#     keyboard.add_hotkey('d', controller.right)
#     keyboard.add_hotkey('a', controller.left)
#     keyboard.add_hotkey('k', controller.degrease_speed)
#     keyboard.add_hotkey('l', controller.increase_speed)
#
#
#     print("Нажмите ESC для остановки")
#     controller.stop()
#     keyboard.wait('esc')
#
#


if __name__ == '__main__':
    # main()
    motor = MotorController()
    motor.forward()
    motor.set_left_speed(99)
    motor.set_right_speed(99)

    # motor.backward()



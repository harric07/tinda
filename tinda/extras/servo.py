

from pyfirmata import SERVO, Arduino
from time import sleep

class HandServo:
    def __init__(self, port, pin, angle):
        self.port = port
        self.pin = pin
        self.angle = angle
        self.board = Arduino(port)
        self.board.digital[pin].mode = SERVO
    def rotate(self, angle):
        self.board.digital[self.pin].write(angle)
        sleep(0.015)
    def back_and_forth(self):
        try:
            while True:
                for i in range(0, self.angle):
                    self.rotate(i)
                for i in range(self.angle, 1, -1):
                    self.rotate(i)
        except KeyboardInterrupt:
            print("keyboard interrupted")
            self.board.digital[self.pin].write(0)
    def new_angle(self, x=int):
        self.board.digital[self.pin].write(x)
        sleep(0.010)
    def one(self):
        self.board.digital[self.pin].write(180)
        sleep(0.010)
    def zero(self):
        self.board.digital[self.pin].write(0)
        sleep(0.010)


p = HandServo("COM4", 9, 180)


class MyServo:
    def __init__(self, port, pin, angle):
        self.port = port
        self.pin = pin
        self.angle = angle
        self.board = Arduino(port)
        self.board.digital[pin].mode = SERVO
    def rotate(self, angle):
        self.board.digital[self.pin].write(angle)
        sleep(0.015)
    def back_and_forth(self):
        try:
            while True:
                for i in range(0, self.angle):
                    self.rotate(i)
                for i in range(self.angle, 1, -1):
                    self.rotate(i)
        except KeyboardInterrupt:
            print("keyboard interrupted")
            self.board.digital[self.pin].write(0)
    def one(self):
        self.board.digital[self.pin].write(180)
        sleep(0.015)
    def zero(self):
        self.board.digital[self.pin].write(0)
        sleep(0.015)





def test():
    finger = HandServo("COM4", 9, 180)
    finger.new_angle(45)
    sleep(1)
    finger.zero()
    sleep(1)
    finger.one()
    sleep(1)
    finger.zero()
    sleep(1)
    finger.new_angle(90)
    sleep(1)
    finger.zero()
    sleep(1)
    finger.one()
    sleep(1)
    finger.zero()
    sleep(1)











from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM4'
pin = 9
board = Arduino(port)
board.digital[pin].mode = SERVO








'''moves servo connected with arduino using pyfirmata'''
'''CURRENTLY SETUP TO MOVE BACK AND FORTH UNTIL KEYBOARD INTERRUPTED'''
# required (port, pin number, angle)
#example: move_servo("COM4", 9, 90)
def move_servo(port=str, pin=int, angle=int):
    from pyfirmata import SERVO, Arduino
    from time import sleep
    board = Arduino(port)
    board.digital[pin].mode = SERVO
    def rotate_servo(pin, angle):
        board.digital[pin].write(angle)
        sleep(0.015)
    def run_servo():
        try:
            while True:
                for i in range(0, angle):
                    rotate_servo(pin, i)
                for i in range(angle, 1, -1):
                    rotate_servo(pin, i)
        except KeyboardInterrupt:
            print("keyboard interrupted")
            board.digital[pin].write(0)
    run_servo()




move_servo("COM4", 9, 180)




def finger_move_one():
    from pyfirmata import SERVO, Arduino
    from time import sleep
    board = Arduino("COM4")
    board.digital[9].mode = SERVO
    def rotate_servo(pin, angle):
        board.digital[pin].write(angle)
        sleep(0.005)
    def run_servo():
        try:
            while True:
                for i in range(0, 45):
                    rotate_servo(9, i)
                for i in range(45, 1, -1):
                    rotate_servo(9, i)
                for i in range(0, 90):
                    rotate_servo(9, i)
                for i in range(90, 1, -1):
                    rotate_servo(9, i)
                for i in range(0, 180):
                    rotate_servo(9, i)
                for i in range(180, 1, -1):
                    rotate_servo(9, i)
        except KeyboardInterrupt:
            print("keyboard interrupted")
            board.digital[pin].write(0)
    run_servo()


finger_move_one()
















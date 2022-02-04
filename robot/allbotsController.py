from adafruit_servokit import ServoKit
from gpiozero import Motor
from time import sleep

kit = None

# set the range of motion for each motor. The index of the list is the motor's number
motors_range = [
    (30, 150), (0, 90),
    (30, 150), (0, 90),
    (30, 150), (0, 90),
    (30, 150), (0, 90)
]


def init():
    global kit
    kit = ServoKit(channels=16)
    kit.servo[0].angle = 30
    kit.servo[1].angle = 0
    kit.servo[2].angle = 30
    kit.servo[3].angle = 0
    kit.servo[4].angle = 30
    kit.servo[5].angle = 0
    kit.servo[6].angle = 30
    kit.servo[7].angle = 0

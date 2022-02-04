from adafruit_servokit import ServoKit
from gpiozero import Motor
from time import sleep


class AllbotsController:

    def reset_position(self):
        self.servo_kit.servo[0].angle = 10
        self.servo_kit.servo[1].angle = 30
        self.servo_kit.servo[2].angle = 10
        self.servo_kit.servo[3].angle = 300
        self.servo_kit.servo[4].angle = 10
        self.servo_kit.servo[5].angle = 150
        self.servo_kit.servo[6].angle = 10
        self.servo_kit.servo[7].angle = 150

    def __init__(self):
        # set the range of motion for each motor. The index of the list is the motor's number
        self.MOTORS_RANGES = [
            (30, 150), (0, 90),
            (30, 150), (0, 90),
            (30, 150), (0, 90),
            (30, 150), (0, 90)
        ]
        self.MIN_IMP, self.MAX_IMP = 500, 2500

        self.servo_kit = ServoKit(channels=16)
        for i in range(len(self.MOTORS_RANGES)):
            self.servo_kit.servo[i].set_pulse_width_range(self.MIN_IMP, self.MAX_IMP)

        self.reset_position()

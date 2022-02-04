from adafruit_servokit import ServoKit
from gpiozero import Motor
from time import sleep


class AllbotsController:

    # set of constants used to replace the motor numbers by more meaningful names
    FRONT_LEFT_ELBOW = 0
    FRONT_LEFT_SHOULDER = 1
    FRONT_RIGHT_ELBOW = 2
    FRONT_RIGHT_SHOULDER = 3
    BACK_LEFT_ELBOW = 4
    BACK_LEFT_SHOULDER = 5
    BACK_RIGHT_ELBOW = 6
    BACK_RIGHT_SHOULDER = 7

    # set the range of motion for each motor. The index of the list is the motor's number
    MOTORS_RANGES = [
        (30, 150), (0, 90),
        (30, 150), (0, 90),
        (30, 150), (0, 90),
        (30, 150), (0, 90)
    ]
    MIN_IMP, MAX_IMP = 500, 2500

    def reset_position(self):
        self.servo_kit.servo[self.FRONT_LEFT_ELBOW].angle = 10
        self.servo_kit.servo[self.FRONT_LEFT_SHOULDER].angle = 30
        self.servo_kit.servo[self.FRONT_RIGHT_ELBOW].angle = 10
        self.servo_kit.servo[self.FRONT_RIGHT_SHOULDER].angle = 300
        self.servo_kit.servo[self.BACK_LEFT_ELBOW].angle = 10
        self.servo_kit.servo[self.BACK_LEFT_SHOULDER].angle = 150
        self.servo_kit.servo[self.BACK_RIGHT_ELBOW].angle = 10
        self.servo_kit.servo[self.BACK_RIGHT_SHOULDER].angle = 150

    def __init__(self):

        self.servo_kit = ServoKit(channels=16)
        for i in range(len(self.MOTORS_RANGES)):
            self.servo_kit.servo[i].set_pulse_width_range(self.MIN_IMP, self.MAX_IMP)

        self.reset_position()

from adafruit_servokit import ServoKit
from time import sleep


class FrancasterController:
    # set of constants used to replace the motor numbers by more meaningful names
    LEFT_ELBOW = 0
    LEFT_SHOULDER_ABDUCTOR = 1
    LEFT_SHOULDER_ROTATOR = 2
    LEFT_SHOULDER_FLEXOR = 3
    RIGHT_SHOULDER_FLEXOR = 4
    RIGHT_SHOULDER_ABDUCTOR = 5
    RIGHT_SHOULDER_ROTATOR = 6
    RIGHT_ELBOW = 7
    LEFT_HIP = 8
    LEFT_KNEE = 9
    LEFT_ANKLE = 10
    RIGHT_HIP = 11
    RIGHT_KNEE = 12
    RIGHT_ANKLE = 13
    HEAD_YAW = 14
    HEAD_PITCH = 15

    # constants used for the is_in_range function
    IN_RANGE = 0
    BELOW_RANGE = -1
    ABOVE_RANGE = 1

    # set the range of motion for each motor. The index of the list is the motor's number
    MOTORS_RANGES = [(0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 170), (0, 180),
                     (0, 135), (0, 120), (0, 180), (45, 180), (0, 120), (0, 180), (35, 140)]

    servo_kit = ServoKit(channels=16)

    def __init__(self):
        self.reset_position()

    def is_in_range(self, motor_nb, angle):
        """
        return IN_RANGE if angle is within the range associated with motor_nb, BELOW_RANGE if below and
        ABOVE_RANGE if above
        """
        mi, ma = self.MOTORS_RANGES[motor_nb]
        if mi <= angle <= ma:
            return self.IN_RANGE
        elif mi > angle:
            return self.BELOW_RANGE
        else:
            return self.ABOVE_RANGE

    def set_motor_position(self, motor_nb, angle):
        motor_nb, angle = int(motor_nb), int(angle)
        mi, ma = self.MOTORS_RANGES[motor_nb]
        if self.is_in_range(motor_nb, angle) == 0:
            self.servo_kit.servo[motor_nb].angle = angle
        elif self.is_in_range(motor_nb, angle) == -1:
            self.servo_kit.servo[motor_nb].angle = mi
        elif self.is_in_range(motor_nb, angle) == 1:
            self.servo_kit.servo[motor_nb].angle = ma
        print(str(motor_nb) + " " + str(mi) + " " + str(ma) + " " + str(self.servo_kit.servo[motor_nb].angle))

    def shift_motor_position(self, motor_nb, angle):
        motor_nb, angle = int(motor_nb), int(angle)
        shifted_angle = self.servo_kit.servo[motor_nb].angle + angle
        mi, ma = self.MOTORS_RANGES[motor_nb]
        if self.is_in_range(motor_nb, shifted_angle) == 0:
            self.servo_kit.servo[motor_nb].angle += angle
        elif self.is_in_range(motor_nb, shifted_angle) == -1:
            self.servo_kit.servo[motor_nb].angle = mi
        elif self.is_in_range(motor_nb, shifted_angle) == 1:
            self.servo_kit.servo[motor_nb].angle = ma
        print(str(motor_nb) + " " + str(mi) + " " + str(ma) + " " + str(self.servo_kit.servo[motor_nb].angle))

    def reset_position(self):
        self.set_motor_position(self.LEFT_ELBOW, 180)
        self.set_motor_position(self.LEFT_SHOULDER_ABDUCTOR, 90)
        self.set_motor_position(self.LEFT_SHOULDER_ROTATOR, 180)
        self.set_motor_position(self.LEFT_SHOULDER_FLEXOR, 90)
        self.set_motor_position(self.RIGHT_SHOULDER_FLEXOR, 90)
        self.set_motor_position(self.RIGHT_SHOULDER_ABDUCTOR, 0)
        self.set_motor_position(self.RIGHT_SHOULDER_ROTATOR, 90)
        self.set_motor_position(self.RIGHT_ELBOW, 0)
        self.set_motor_position(self.LEFT_HIP, 90)
        self.set_motor_position(self.LEFT_KNEE, 0)
        self.set_motor_position(self.LEFT_ANKLE, 45)
        self.set_motor_position(self.RIGHT_HIP, 90)
        self.set_motor_position(self.RIGHT_KNEE, 180)
        self.set_motor_position(self.RIGHT_ANKLE, 75)
        self.set_motor_position(self.HEAD_YAW, 90)
        self.set_motor_position(self.HEAD_PITCH, 90)

    def walk_n_steps(self, n):
        for _ in range(0, n - 1):
            self.set_motor_position(self.LEFT_SHOULDER_FLEXOR, 60)
            sleep(.1)
            self.set_motor_position(self.RIGHT_SHOULDER_FLEXOR, 60)
            sleep(.1)
            self.set_motor_position(self.LEFT_HIP, 120)
            sleep(.1)
            self.set_motor_position(self.RIGHT_HIP, 120)
            sleep(0.5)
            self.set_motor_position(self.LEFT_SHOULDER_FLEXOR, 120)
            sleep(.1)
            self.set_motor_position(self.RIGHT_SHOULDER_FLEXOR, 120)
            sleep(.1)
            self.set_motor_position(self.LEFT_HIP, 60)
            sleep(.1)
            self.set_motor_position(self.RIGHT_HIP, 60)
            sleep(.5)

    def do_hi(self, ps):
        self.set_motor_position(self.RIGHT_SHOULDER_ABDUCTOR, 130)
        sleep(.1)
        self.set_motor_position(self.RIGHT_SHOULDER_ROTATOR, 180)
        sleep(.1)
        for _ in range(0, ps - 1):
            self.set_motor_position(self.RIGHT_ELBOW, 90)
            sleep(0.5)
            self.set_motor_position(self.RIGHT_ELBOW, 0)
            sleep(0.5)

    def walk_n_steps_with_knee_lift(self, ps):
        self.set_motor_position(self.LEFT_SHOULDER_ROTATOR, 170)
        self.set_motor_position(self.RIGHT_SHOULDER_ABDUCTOR, 10)
        for _ in range(0, ps - 1):
            self.set_motor_position(self.LEFT_ELBOW, 150)
            sleep(0.2)
            self.set_motor_position(self.LEFT_SHOULDER_FLEXOR, 90)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_SHOULDER_FLEXOR, 60)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_ELBOW, 0)
            sleep(0.2)
            self.set_motor_position(self.LEFT_HIP, 100)
            sleep(0.2)
            self.set_motor_position(self.LEFT_KNEE, 60)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_HIP, 120)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_KNEE, 180)
            sleep(0.2)
            self.set_motor_position(self.LEFT_ELBOW, 180)
            sleep(0.2)
            self.set_motor_position(self.LEFT_SHOULDER_FLEXOR, 120)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_SHOULDER_FLEXOR, 90)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_ELBOW, 30)
            sleep(0.2)
            self.set_motor_position(self.LEFT_HIP, 50)
            sleep(0.2)
            self.set_motor_position(self.LEFT_KNEE, 0)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_HIP, 80)
            sleep(0.2)
            self.set_motor_position(self.RIGHT_KNEE, 120)
            sleep(0.2)

    def do_no(self):
        for _ in range(0, 2):
            sleep(.5)
            self.set_motor_position(self.HEAD_YAW, 120)
            sleep(.5)
            self.set_motor_position(self.HEAD_YAW, 60)

    def do_yes(self):
        for _ in range(0, 2):
            sleep(.5)
            self.set_motor_position(self.HEAD_PITCH, 45)
            sleep(.5)
            self.set_motor_position(self.HEAD_PITCH, 90)

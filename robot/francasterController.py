from adafruit_servokit import ServoKit
from gpiozero import Motor
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

    # set the range of motion for each motor. The index of the list is the motor's number
    MOTORS_RANGES = [(0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 170), (0, 180),
                     (0, 135), (0, 120), (0, 180), (45, 180), (0, 120), (0, 180), (35, 140)]

    servo_kit = ServoKit(channels=16)

    def reset_position(self):
        self.servo_kit.servo[0].angle = 180
        self.servo_kit.servo[self.LEFT_SHOULDER_ABDUCTOR].angle = 90
        self.servo_kit.servo[self.LEFT_SHOULDER_ROTATOR].angle = 180
        self.servo_kit.servo[self.LEFT_SHOULDER_FLEXOR].angle = 90
        self.servo_kit.servo[self.RIGHT_SHOULDER_FLEXOR].angle = 90
        self.servo_kit.servo[self.RIGHT_SHOULDER_ABDUCTOR].angle = 0
        self.servo_kit.servo[self.RIGHT_SHOULDER_ROTATOR].angle = 90
        self.servo_kit.servo[self.RIGHT_ELBOW].angle = 0
        self.servo_kit.servo[self.LEFT_HIP].angle = 90
        self.servo_kit.servo[self.LEFT_KNEE].angle = 0
        self.servo_kit.servo[self.LEFT_ANKLE].angle = 45
        self.servo_kit.servo[self.RIGHT_HIP].angle = 90
        self.servo_kit.servo[self.RIGHT_KNEE].angle = 180
        self.servo_kit.servo[self.RIGHT_ANKLE].angle = 75
        self.servo_kit.servo[self.HEAD_YAW].angle = 90
        self.servo_kit.servo[self.HEAD_PITCH].angle = 90

    def __init__(self):
        self.reset_position()

    def verify_drange_min(self, motor, angle):
        mi, ma = self.MOTORS_RANGES[motor]
        return mi > angle

    def verify_drange_max(self, motor, angle):
        mi, ma = self.MOTORS_RANGES[motor]
        return ma < angle

    def verify_range(self, motor, angle):
        mi, ma = self.MOTORS_RANGES[motor]
        return mi <= angle <= ma

    def set_motor_power(self, motor, angle):
        motor = int(motor)
        angle = int(angle)
        mi, ma = self.MOTORS_RANGES[motor]
        if self.verify_range(motor, angle):
            self.servo_kit.servo[motor].angle = angle
        else:
            if self.verify_drange_min(motor, angle):
                self.servo_kit.servo[motor].angle = int(mi)
            if self.verify_drange_max(motor, angle):
                self.servo_kit.servo[motor].angle = int(ma)
        print(str(motor) + " " + str(mi) + " " + str(ma) + " " + str(self.servo_kit.servo[int(motor)].angle))

    def shift_motor_position(self, motor, angle):
        x = self.servo_kit.servo[int(motor)].angle + angle
        mi, ma = self.MOTORS_RANGES[motor]
        if self.verify_range(motor, x):
            self.servo_kit.servo[int(motor)].angle += int(angle)
        else:

            if self.verify_drange_min(motor, x):
                self.servo_kit.servo[int(motor)].angle = int(mi)
            if self.verify_drange_max(motor, x):
                self.servo_kit.servo[int(motor)].angle = int(ma)
        print(str(motor) + " " + str(mi) + " " + str(ma) + " " + str(self.servo_kit.servo[int(motor)].angle))

    def delay(self, time):
        sleep(float(time))
        print("motor  posé" + time)

    def walk_n_steps(self, n):
        for _ in range(0, n - 1):
            self.servo_kit.servo[self.LEFT_SHOULDER_FLEXOR].angle = 60
            sleep(.1)
            self.servo_kit.servo[self.RIGHT_SHOULDER_FLEXOR].angle = 60
            sleep(.1)
            self.servo_kit.servo[self.LEFT_HIP].angle = 120
            sleep(.1)
            self.servo_kit.servo[self.RIGHT_HIP].angle = 120
            sleep(0.5)
            self.servo_kit.servo[self.LEFT_SHOULDER_FLEXOR].angle = 120
            sleep(.1)
            self.servo_kit.servo[self.RIGHT_SHOULDER_FLEXOR].angle = 120
            sleep(.1)
            self.servo_kit.servo[self.LEFT_HIP].angle = 60
            sleep(.1)
            self.servo_kit.servo[self.RIGHT_HIP].angle = 60
            sleep(.5)

    def do_hi(self, ps):
        self.servo_kit.servo[self.RIGHT_SHOULDER_ABDUCTOR].angle = 130
        sleep(.1)
        self.servo_kit.servo[self.RIGHT_SHOULDER_ROTATOR].angle = 180
        sleep(.1)
        for _ in range(0, ps - 1):
            self.servo_kit.servo[self.RIGHT_ELBOW].angle = 90
            sleep(0.5)
            self.servo_kit.servo[self.RIGHT_ELBOW].angle = 0
            sleep(0.5)

    def walk_n_steps_with_knee_lift(self, ps):
        self.servo_kit.servo[self.LEFT_SHOULDER_ROTATOR].angle = 170
        self.servo_kit.servo[self.RIGHT_SHOULDER_ABDUCTOR].angle = 10
        for _ in range(0, ps - 1):
            self.servo_kit.servo[self.LEFT_ELBOW].angle = 150
            sleep(0.2)
            self.servo_kit.servo[self.LEFT_SHOULDER_FLEXOR].angle = 90
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_SHOULDER_FLEXOR].angle = 60
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_ELBOW].angle = 0
            sleep(0.2)
            self.servo_kit.servo[self.LEFT_HIP].angle = 100
            sleep(0.2)
            self.servo_kit.servo[self.LEFT_KNEE].angle = 60
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_HIP].angle = 120
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_KNEE].angle = 180
            sleep(0.2)
            self.servo_kit.servo[self.LEFT_ELBOW].angle = 180
            sleep(0.2)
            self.servo_kit.servo[self.LEFT_SHOULDER_FLEXOR].angle = 120
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_SHOULDER_FLEXOR].angle = 90
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_ELBOW].angle = 30
            sleep(0.2)
            self.servo_kit.servo[self.LEFT_HIP].angle = 50
            sleep(0.2)
            self.servo_kit.servo[self.LEFT_KNEE].angle = 0
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_HIP].angle = 80
            sleep(0.2)
            self.servo_kit.servo[self.RIGHT_KNEE].angle = 120
            sleep(0.2)

    def do_no(self):
        for _ in range(0, 2):
            sleep(.5)
            self.servo_kit.servo[self.HEAD_YAW].angle = 120
            sleep(.5)
            self.servo_kit.servo[self.HEAD_YAW].angle = 60

    def do_yes(self):
        for _ in range(0, 2):
            sleep(.5)
            self.servo_kit.servo[self.HEAD_PITCH].angle = 45
            sleep(.5)
            self.servo_kit.servo[self.HEAD_PITCH].angle = 90

    def motor_dc(self, speed=1):
        motor = Motor(pinA, pinB)
        motor.forward(speed)

    def motor_dc_backward(self, speed=1):
        motor = Motor(pinA, pinB)
        motor.backward(speed)

    def motor_dc_reverse(self):
        motor = Motor(pinA, pinB)
        motor.reverse()

    def motor_dc_stop(self):
        motor = Motor(pinA, pinB)
        motor.stop()

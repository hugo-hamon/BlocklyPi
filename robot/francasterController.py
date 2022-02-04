from adafruit_servokit import ServoKit
from gpiozero import Motor
from time import sleep


class FrancasterController:

    def reset_position(self):
        self.servo_kit.servo[0].angle = 180
        self.servo_kit.servo[1].angle = 90
        self.servo_kit.servo[2].angle = 180
        self.servo_kit.servo[3].angle = 90
        self.servo_kit.servo[4].angle = 90
        self.servo_kit.servo[5].angle = 0
        self.servo_kit.servo[6].angle = 90
        self.servo_kit.servo[7].angle = 0
        self.servo_kit.servo[8].angle = 90
        self.servo_kit.servo[9].angle = 0
        self.servo_kit.servo[10].angle = 45
        self.servo_kit.servo[11].angle = 90
        self.servo_kit.servo[12].angle = 180
        self.servo_kit.servo[13].angle = 75
        self.servo_kit.servo[14].angle = 90
        self.servo_kit.servo[15].angle = 90

    def __init__(self):
        # set the range of motion for each motor. The index of the list is the motor's number
        self.motors_range = [(0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 170), (0, 180),
                             (0, 135), (0, 120), (0, 180), (45, 180), (0, 120), (0, 180), (35, 140)]

        self.servo_kit = ServoKit(channels=16)
        self.reset_position()

    def verify_drange_min(self, motor, angle):
        mi, ma = self.motors_range[motor]
        return mi > angle

    def verify_drange_max(self, motor, angle):
        mi, ma = self.motors_range[motor]
        return ma < angle

    def verify_range(self, motor, angle):
        mi, ma = self.motors_range[motor]
        return mi <= angle <= ma

    def set_motor_power(self, motor, angle):
        motor = int(motor)
        angle = int(angle)
        mi, ma = self.motors_range[motor]
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
        mi, ma = self.motors_range[motor]
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
            self.servo_kit.servo[3].angle = 60
            sleep(.1)
            self.servo_kit.servo[4].angle = 60
            sleep(.1)
            self.servo_kit.servo[8].angle = 120
            sleep(.1)
            self.servo_kit.servo[11].angle = 120
            sleep(0.5)
            self.servo_kit.servo[3].angle = 120
            sleep(.1)
            self.servo_kit.servo[4].angle = 120
            sleep(.1)
            self.servo_kit.servo[8].angle = 60
            sleep(.1)
            self.servo_kit.servo[11].angle = 60
            sleep(.5)

    def do_hi(self, ps):
        self.servo_kit.servo[5].angle = 130
        sleep(.1)
        self.servo_kit.servo[6].angle = 180
        sleep(.1)
        for _ in range(0, ps - 1):
            self.servo_kit.servo[7].angle = 90
            sleep(0.5)
            self.servo_kit.servo[7].angle = 0
            sleep(0.5)

    def walk_n_steps_with_knee_lift(self, ps):
        self.servo_kit.servo[2].angle = 170
        self.servo_kit.servo[5].angle = 10
        for _ in range(0, ps - 1):
            self.servo_kit.servo[0].angle = 150
            sleep(0.2)
            self.servo_kit.servo[3].angle = 90
            sleep(0.2)
            self.servo_kit.servo[4].angle = 60
            sleep(0.2)
            self.servo_kit.servo[7].angle = 0
            sleep(0.2)
            self.servo_kit.servo[8].angle = 100
            sleep(0.2)
            self.servo_kit.servo[9].angle = 60
            sleep(0.2)
            self.servo_kit.servo[11].angle = 120
            sleep(0.2)
            self.servo_kit.servo[12].angle = 180
            sleep(0.2)
            self.servo_kit.servo[0].angle = 180
            sleep(0.2)
            self.servo_kit.servo[3].angle = 120
            sleep(0.2)
            self.servo_kit.servo[4].angle = 90
            sleep(0.2)
            self.servo_kit.servo[7].angle = 30
            sleep(0.2)
            self.servo_kit.servo[8].angle = 50
            sleep(0.2)
            self.servo_kit.servo[9].angle = 0
            sleep(0.2)
            self.servo_kit.servo[11].angle = 80
            sleep(0.2)
            self.servo_kit.servo[12].angle = 120
            sleep(0.2)

    def do_no(self):
        for _ in range(0, 2):
            sleep(.5)
            self.servo_kit.servo[14].angle = 120
            sleep(.5)
            self.servo_kit.servo[14].angle = 60

    def do_yes(self):
        for _ in range(0, 2):
            sleep(.5)
            self.servo_kit.servo[15].angle = 45
            sleep(.5)
            self.servo_kit.servo[15].angle = 90

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

from adafruit_servokit import ServoKit
from gpiozero import Motor
from time import sleep

kit = None

# set the range of motion for each motor. The index of the list is the motor's number
motors_range = [(0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 180), (0, 170), (0, 180),
                (0, 135), (0, 120), (0, 180), (45, 180), (0, 120), (0, 180), (35, 140)]


def init():
    global kit
    kit = ServoKit(channels=16)
    sleep(.1)
    kit.servo[0].angle = 180
    sleep(.1)
    kit.servo[1].angle = 90
    sleep(.1)
    kit.servo[2].angle = 180
    sleep(.1)
    kit.servo[3].angle = 90
    sleep(.1)
    kit.servo[4].angle = 90
    sleep(.1)
    kit.servo[5].angle = 0
    sleep(.1)
    kit.servo[6].angle = 90
    sleep(.1)
    kit.servo[7].angle = 0
    sleep(.1)
    kit.servo[8].angle = 90
    sleep(.1)
    kit.servo[9].angle = 0
    sleep(.1)
    kit.servo[10].angle = 45
    sleep(.1)
    kit.servo[11].angle = 90
    sleep(.1)
    kit.servo[12].angle = 180
    sleep(.1)
    kit.servo[13].angle = 75
    sleep(.1)
    kit.servo[14].angle = 90
    sleep(.1)
    kit.servo[15].angle = 90


def verify_drange_min(motor, angle):
    mi, ma = motors_range[motor]
    return mi > angle


def verify_drange_max(motor, angle):
    mi, ma = motors_range[motor]
    return ma < angle


def verify_range(motor, angle):
    mi, ma = motors_range[motor]
    return mi <= angle <= ma


def set_motor_power(motor, angle):
    motor = int(motor)
    angle = int(angle)
    mi, ma = motors_range[motor]
    if verify_range(motor, angle):
        kit.servo[motor].angle = angle
    else:
        if verify_drange_min(motor, angle):
            kit.servo[motor].angle = int(mi)
        if verify_drange_max(motor, angle):
            kit.servo[motor].angle = int(ma)
    print(str(motor) + " " + str(mi) + " " + str(ma) + " " + str(kit.servo[int(motor)].angle))


def shift_motor_position(motor, angle):
    x = kit.servo[int(motor)].angle + angle
    mi, ma = motors_range[motor]
    if verify_range(motor, x):
        kit.servo[int(motor)].angle += int(angle)
    else:

        if verify_drange_min(motor, x):
            kit.servo[int(motor)].angle = int(mi)
        if verify_drange_max(motor, x):
            kit.servo[int(motor)].angle = int(ma)
    print(str(motor) + " " + str(mi) + " " + str(ma) + " " + str(kit.servo[int(motor)].angle))


def delay(temps):
    sleep(float(temps))
    print("motor  posé" + temps)


def walk_n_steps(n):
    for _ in range(0, n - 1):
        kit.servo[3].angle = 60
        sleep(.1)
        kit.servo[4].angle = 60
        sleep(.1)
        kit.servo[8].angle = 120
        sleep(.1)
        kit.servo[11].angle = 120
        sleep(0.5)
        kit.servo[3].angle = 120
        sleep(.1)
        kit.servo[4].angle = 120
        sleep(.1)
        kit.servo[8].angle = 60
        sleep(.1)
        kit.servo[11].angle = 60
        sleep(.5)
    init()


def do_hi(ps):
    kit.servo[5].angle = 130
    sleep(.1)
    kit.servo[6].angle = 180
    sleep(.1)
    for _ in range(0, ps - 1):
        kit.servo[7].angle = 90
        sleep(0.5)
        kit.servo[7].angle = 0
        sleep(0.5)
    init()


def walk_n_steps_with_knee_lift(ps):
    kit.servo[2].angle = 170
    kit.servo[5].angle = 10
    for _ in range(0, ps - 1):
        kit.servo[0].angle = 150
        sleep(0.2)
        kit.servo[3].angle = 90
        sleep(0.2)
        kit.servo[4].angle = 60
        sleep(0.2)
        kit.servo[7].angle = 0
        sleep(0.2)
        kit.servo[8].angle = 100
        sleep(0.2)
        kit.servo[9].angle = 60
        sleep(0.2)
        kit.servo[11].angle = 120
        sleep(0.2)
        kit.servo[12].angle = 180
        sleep(0.2)
        kit.servo[0].angle = 180
        sleep(0.2)
        kit.servo[3].angle = 120
        sleep(0.2)
        kit.servo[4].angle = 90
        sleep(0.2)
        kit.servo[7].angle = 30
        sleep(0.2)
        kit.servo[8].angle = 50
        sleep(0.2)
        kit.servo[9].angle = 0
        sleep(0.2)
        kit.servo[11].angle = 80
        sleep(0.2)
        kit.servo[12].angle = 120
        sleep(0.2)
    init()


def do_no():
    for _ in range(0, 2):
        sleep(.5)
        kit.servo[14].angle = 120
        sleep(.5)
        kit.servo[14].angle = 60
    init()


def do_yes():
    for _ in range(0, 2):
        sleep(.5)
        kit.servo[15].angle = 45
        sleep(.5)
        kit.servo[15].angle = 90
    init()


def motor_dc(speed=1):
    motor = Motor(pinA, pinB)
    motor.forward(speed)


def motor_dc_backward(speed=1):
    motor = Motor(pinA, pinB)
    motor.backward(speed)


def motor_dc_reverse():
    motor = Motor(pinA, pinB)
    motor.reverse()


def motor_dc_stop():
    motor = Motor(pinA, pinB)
    motor.stop()

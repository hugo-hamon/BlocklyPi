import time
from time import sleep
from robot.robotMotor import RobotMotor

MOTORS = {
    "lEFT_ELBOW": RobotMotor(0, 0, 180, 180),
    "LEFT_SHOULDER_ABDUCTOR": RobotMotor(1, 0, 180, 90),
    "LEFT_SHOULDER_ROTATOR": RobotMotor(2, 0, 180, 180),
    "LEFT_SHOULDER_FLEXOR": RobotMotor(3, 0, 180, 90),
    "RIGHT_SHOULDER_FLEXOR": RobotMotor(4, 0, 180, 90),
    "RIGHT_SHOULDER_ABDUCTOR": RobotMotor(5, 0, 180, 0),
    "RIGHT_SHOULDER_ROTATOR": RobotMotor(6, 0, 180, 90),
    "RIGHT_ELBOW": RobotMotor(7, 0, 170, 0),
    "LEFT_HIP": RobotMotor(8, 0, 180, 90),
    "LEFT_KNEE": RobotMotor(9, 0, 135, 0),
    "LEFT_ANKLE": RobotMotor(10, 0, 120, 45),
    "RIGHT_HIP": RobotMotor(11, 0, 180, 90),
    "RIGHT_KNEE": RobotMotor(12, 45, 180, 180),
    "RIGHT_ANKLE": RobotMotor(13, 0, 120, 75),
    "HEAD_YAW": RobotMotor(14, 0, 180, 90),
    "HEAD_PITCH": RobotMotor(15, 35, 140, 90)
}


def set_motor_position(motor_nb: str, angle: str):
    motor_nb, angle = int(motor_nb), int(angle)
    for motor in MOTORS.values():
        if motor.id == motor_nb:
            motor.set_motor_position(angle)
            return


def shift_motor_position(motor_nb: str, angle: str):
    motor_nb, angle = int(motor_nb), int(angle)
    for v in MOTORS.values():
        if v.id == motor_nb:
            v.shift_motor_position(angle)
            return


def reset_position():
    for motor in MOTORS.values():
        motor.reset()
        time.sleep(0.2)


def set_delay(seconds: str):
    time.sleep(int(seconds))


def walk_n_steps(nb_steps: str):
    nb_steps = int(nb_steps)
    for _ in range(0, nb_steps - 1):
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(60)
        sleep(.1)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(60)
        sleep(.1)
        MOTORS["LEFT_HIP"].set_motor_position(120)
        sleep(.1)
        MOTORS["RIGHT_HIP"].set_motor_position(120)
        sleep(0.5)
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(120)
        sleep(.1)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(120)
        sleep(.1)
        MOTORS["LEFT_HIP"].set_motor_position(60)
        sleep(.1)
        MOTORS["RIGHT_HIP"].set_motor_position(60)
        sleep(.5)


def do_hi(nb_greetings: str):
    """
    :param nb_greetings: the number of times the hand will wave
    """
    nb_greetings = int(nb_greetings)
    MOTORS["RIGHT_SHOULDER_ABDUCTOR"].set_motor_position(130)
    sleep(.1)
    MOTORS["RIGHT_SHOULDER_ROTATOR"].set_motor_position(180)
    sleep(.1)
    for _ in range(nb_greetings):
        MOTORS["RIGHT_ELBOW"].set_motor_position(90)
        sleep(0.5)
        MOTORS["RIGHT_ELBOW"].set_motor_position(0)
        sleep(0.5)


def walk_n_steps_with_knee_lift(nb_steps):
    MOTORS["LEFT_SHOULDER_ROTATOR"].set_motor_position(170)
    MOTORS["RIGHT_SHOULDER_ABDUCTOR"].set_motor_position(10)
    for _ in range(nb_steps):
        MOTORS["LEFT_ELBOW"].set_motor_position(150)
        sleep(0.2)
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(90)
        sleep(0.2)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(60)
        sleep(0.2)
        MOTORS["RIGHT_ELBOW"].set_motor_position(0)
        sleep(0.2)
        MOTORS["LEFT_HIP"].set_motor_position(100)
        sleep(0.2)
        MOTORS["LEFT_KNEE"].set_motor_position(60)
        sleep(0.2)
        MOTORS["RIGHT_HIP"].set_motor_position(120)
        sleep(0.2)
        MOTORS["RIGHT_KNEE"].set_motor_position(180)
        sleep(0.2)
        MOTORS["LEFT_ELBOW"].set_motor_position(180)
        sleep(0.2)
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(120)
        sleep(0.2)
        MOTORS["RIGHT_SHOULDER_FLEXOR"].set_motor_position(90)
        sleep(0.2)
        MOTORS["RIGHT_ELBOW"].set_motor_position(30)
        sleep(0.2)
        MOTORS["LEFT_HIP"].set_motor_position(50)
        sleep(0.2)
        MOTORS["LEFT_KNEE"].set_motor_position(0)
        sleep(0.2)
        MOTORS["RIGHT_HIP"].set_motor_position(80)
        sleep(0.2)
        MOTORS["RIGHT_KNEE"].set_motor_position(120)
        sleep(0.2)


def do_no():
    for _ in range(0, 2):
        sleep(.5)
        MOTORS["HEAD_YAW"].set_motor_position(120)
        sleep(.5)
        MOTORS["HEAD_YAW"].set_motor_position(60)


def do_yes():
    for _ in range(0, 2):
        sleep(.5)
        MOTORS["HEAD_PITCH"].set_motor_position(45)
        sleep(.5)
        MOTORS["HEAD_PITCH"].set_motor_position(90)

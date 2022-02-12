from time import sleep
from robot import robotController
from robot.robotMotor import RobotMotor

# set of constants used to replace the motor numbers by more meaningful names
LEFT_ELBOW = RobotMotor(0, 0, 180)
LEFT_SHOULDER_ABDUCTOR = RobotMotor(1, 0, 180)
LEFT_SHOULDER_ROTATOR = RobotMotor(2, 0, 180)
LEFT_SHOULDER_FLEXOR = RobotMotor(3, 0, 180)
RIGHT_SHOULDER_FLEXOR = RobotMotor(4, 0, 180)
RIGHT_SHOULDER_ABDUCTOR = RobotMotor(5, 0, 180)
RIGHT_SHOULDER_ROTATOR = RobotMotor(6, 0, 180)
RIGHT_ELBOW = RobotMotor(7, 0, 170)
LEFT_HIP = RobotMotor(8, 0, 180)
LEFT_KNEE = RobotMotor(9, 0, 135)
LEFT_ANKLE = RobotMotor(10, 0, 120)
RIGHT_HIP = RobotMotor(11, 0, 180)
RIGHT_KNEE = RobotMotor(12, 45, 180)
RIGHT_ANKLE = RobotMotor(13, 0, 120)
HEAD_YAW = RobotMotor(14, 0, 180)
HEAD_PITCH = RobotMotor(15, 35, 140)


def reset_position():
    robotController.set_motor_position(LEFT_ELBOW, 180)
    robotController.set_motor_position(LEFT_SHOULDER_ABDUCTOR, 90)
    robotController.set_motor_position(LEFT_SHOULDER_ROTATOR, 180)
    robotController.set_motor_position(LEFT_SHOULDER_FLEXOR, 90)
    robotController.set_motor_position(RIGHT_SHOULDER_FLEXOR, 90)
    robotController.set_motor_position(RIGHT_SHOULDER_ABDUCTOR, 0)
    robotController.set_motor_position(RIGHT_SHOULDER_ROTATOR, 90)
    robotController.set_motor_position(RIGHT_ELBOW, 0)
    robotController.set_motor_position(LEFT_HIP, 90)
    robotController.set_motor_position(LEFT_KNEE, 0)
    robotController.set_motor_position(LEFT_ANKLE, 45)
    robotController.set_motor_position(RIGHT_HIP, 90)
    robotController.set_motor_position(RIGHT_KNEE, 180)
    robotController.set_motor_position(RIGHT_ANKLE, 75)
    robotController.set_motor_position(HEAD_YAW, 90)
    robotController.set_motor_position(HEAD_PITCH, 90)


def walk_n_steps(n):
    for _ in range(0, n - 1):
        robotController.set_motor_position(LEFT_SHOULDER_FLEXOR, 60)
        sleep(.1)
        robotController.set_motor_position(RIGHT_SHOULDER_FLEXOR, 60)
        sleep(.1)
        robotController.set_motor_position(LEFT_HIP, 120)
        sleep(.1)
        robotController.set_motor_position(RIGHT_HIP, 120)
        sleep(0.5)
        robotController.set_motor_position(LEFT_SHOULDER_FLEXOR, 120)
        sleep(.1)
        robotController.set_motor_position(RIGHT_SHOULDER_FLEXOR, 120)
        sleep(.1)
        robotController.set_motor_position(LEFT_HIP, 60)
        sleep(.1)
        robotController.set_motor_position(RIGHT_HIP, 60)
        sleep(.5)


def do_hi(ps):
    robotController.set_motor_position(RIGHT_SHOULDER_ABDUCTOR, 130)
    sleep(.1)
    robotController.set_motor_position(RIGHT_SHOULDER_ROTATOR, 180)
    sleep(.1)
    for _ in range(0, ps - 1):
        robotController.set_motor_position(RIGHT_ELBOW, 90)
        sleep(0.5)
        robotController.set_motor_position(RIGHT_ELBOW, 0)
        sleep(0.5)


def walk_n_steps_with_knee_lift(ps):
    robotController.set_motor_position(LEFT_SHOULDER_ROTATOR, 170)
    robotController.set_motor_position(RIGHT_SHOULDER_ABDUCTOR, 10)
    for _ in range(0, ps - 1):
        robotController.set_motor_position(LEFT_ELBOW, 150)
        sleep(0.2)
        robotController.set_motor_position(LEFT_SHOULDER_FLEXOR, 90)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_SHOULDER_FLEXOR, 60)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_ELBOW, 0)
        sleep(0.2)
        robotController.set_motor_position(LEFT_HIP, 100)
        sleep(0.2)
        robotController.set_motor_position(LEFT_KNEE, 60)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_HIP, 120)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_KNEE, 180)
        sleep(0.2)
        robotController.set_motor_position(LEFT_ELBOW, 180)
        sleep(0.2)
        robotController.set_motor_position(LEFT_SHOULDER_FLEXOR, 120)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_SHOULDER_FLEXOR, 90)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_ELBOW, 30)
        sleep(0.2)
        robotController.set_motor_position(LEFT_HIP, 50)
        sleep(0.2)
        robotController.set_motor_position(LEFT_KNEE, 0)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_HIP, 80)
        sleep(0.2)
        robotController.set_motor_position(RIGHT_KNEE, 120)
        sleep(0.2)


def do_no():
    for _ in range(0, 2):
        sleep(.5)
        robotController.set_motor_position(HEAD_YAW, 120)
        sleep(.5)
        robotController.set_motor_position(HEAD_YAW, 60)


def do_yes():
    for _ in range(0, 2):
        sleep(.5)
        robotController.set_motor_position(HEAD_PITCH, 45)
        sleep(.5)
        robotController.set_motor_position(HEAD_PITCH, 90)

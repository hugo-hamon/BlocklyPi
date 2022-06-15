from time import *
from robotMotor import RobotMotor

motor1 = RobotMotor(0, 0, 135)  # BACK_RIGHT_SHOULDER
motor2 = RobotMotor(1, 25, 180)  # FRONT_RIGHT_SHOULDER
motor3 = RobotMotor(2, 0, 135)  # FRONT_LEFT_SHOULDER
motor4 = RobotMotor(3, 25, 180)  # BACK_LEFT_SHOULDER
motor5 = RobotMotor(4, 0, 180)  # BACK_RIGHT_ELBOW
motor6 = RobotMotor(5, 0, 180)  # FRONT_RIGHT_ELBOW
motor7 = RobotMotor(6, 0, 180)  # FRONT_LEFT_ELBOW
motor8 = RobotMotor(7, 0, 180)  # BACK_LEFT_ELBOW


def angle_motor(motor, angle):
    if motor == '0':
        motor = motor1
    elif motor == '1':
        motor = motor2
    elif motor == '2':
        motor = motor3
    elif motor == '3':
        motor = motor4
    elif motor == '4':
        motor = motor5
    elif motor == '5':
        motor = motor6
    elif motor == '6':
        motor = motor7
    elif motor == '7':
        motor = motor8
    else:
        pass
    motor.shift_motor_position(angle)


def reset_position():
    motor1.set_motor_position(50)
    motor2.set_motor_position(70)
    motor3.set_motor_position(110)
    motor4.set_motor_position(110)
    motor5.set_motor_position(20)
    motor6.set_motor_position(20)
    motor7.set_motor_position(160)
    motor8.set_motor_position(20)


def reculer():
    motor6.set_motor_position(50)
    motor8.set_motor_position(50)
    sleep(0.2)
    motor2.shift_motor_position(-50)  #
    motor4.shift_motor_position(50)  #

    sleep(0.2)
    motor6.set_motor_position(20)
    motor8.set_motor_position(20)
    sleep(0.1)
    motor7.set_motor_position(130)
    motor5.set_motor_position(50)

    sleep(0.1)
    motor2.shift_motor_position(50)  #
    motor4.shift_motor_position(-50)  #
    sleep(0.2)
    # -----------------------------------------------#
    motor1.shift_motor_position(-50)  #
    motor3.shift_motor_position(50)  #
    sleep(0.2)
    motor7.set_motor_position(160)
    motor5.set_motor_position(20)
    sleep(0.1)
    motor6.set_motor_position(50)
    motor8.set_motor_position(50)
    sleep(0.1)
    motor1.shift_motor_position(50)  #
    motor3.shift_motor_position(-50)  #
    sleep(0.1)
    motor6.set_motor_position(20)
    motor8.set_motor_position(20)
    sleep(0.1)
    reset_position()


def coucou(motor):
    if motor == '0':
        motor = motor3
        other_motor = motor7
        reset_position()
        sleep(0.5)
        other_motor.set_motor_position(0)
    elif motor == '1':
        motor = motor2
        other_motor = motor6
        reset_position()
        sleep(0.5)
        other_motor.set_motor_position(180)

    for i in range(3):
        motor.shift_motor_position(50)
        sleep(0.4)
        motor.shift_motor_position(-50)
        sleep(0.4)
    reset_position()


def tourner_gauche():
    motor7.set_motor_position(120)
    motor5.set_motor_position(60)
    sleep(0.1)
    motor1.shift_motor_position(50)  #
    motor3.shift_motor_position(50)  #
    sleep(0.1)
    motor7.set_motor_position(160)
    motor5.set_motor_position(20)

    motor6.set_motor_position(60)
    motor8.set_motor_position(60)
    sleep(0.1)
    motor1.shift_motor_position(-50)  #
    motor3.shift_motor_position(-50)  #
    sleep(0.1)

    # -------------------------------------#

    sleep(0.1)
    motor2.shift_motor_position(50)  #
    motor4.shift_motor_position(50)  #
    sleep(0.1)
    motor6.set_motor_position(20)
    motor8.set_motor_position(20)

    motor7.set_motor_position(120)
    motor5.set_motor_position(60)
    sleep(0.1)
    motor2.shift_motor_position(-50)  #
    motor4.shift_motor_position(-50)  #
    sleep(0.2)
    reset_position()


def tourner_droite():
    motor7.set_motor_position(120)
    motor5.set_motor_position(60)
    sleep(0.1)
    motor1.shift_motor_position(-50)  #
    motor3.shift_motor_position(-50)  #
    sleep(0.1)
    motor7.set_motor_position(160)
    motor5.set_motor_position(20)

    motor6.set_motor_position(60)
    motor8.set_motor_position(60)
    sleep(0.1)
    motor1.shift_motor_position(50)  #
    motor3.shift_motor_position(50)  #
    sleep(0.1)

    # -------------------------------------#

    sleep(0.1)
    motor2.shift_motor_position(-70)  #
    motor4.shift_motor_position(-70)  #
    sleep(0.1)
    motor6.set_motor_position(20)
    motor8.set_motor_position(20)

    motor7.set_motor_position(120)
    motor5.set_motor_position(60)
    sleep(0.1)
    motor2.shift_motor_position(70)  #
    motor4.shift_motor_position(70)  #
    sleep(0.2)
    reset_position()


def avancer():
    motor6.set_motor_position(50)
    motor8.set_motor_position(50)
    sleep(0.2)
    motor2.shift_motor_position(70)
    motor4.shift_motor_position(-110)

    sleep(0.2)
    motor6.set_motor_position(20)
    motor8.set_motor_position(20)
    sleep(0.1)
    motor7.set_motor_position(130)
    motor5.set_motor_position(50)

    sleep(0.1)
    motor2.shift_motor_position(-70)
    motor4.shift_motor_position(110)
    sleep(0.2)
    # -----------------------------------------------#
    motor1.shift_motor_position(70)
    motor3.shift_motor_position(-70)
    sleep(0.2)
    motor7.set_motor_position(160)
    motor5.set_motor_position(20)
    sleep(0.1)
    motor6.set_motor_position(50)
    motor8.set_motor_position(50)
    sleep(0.1)
    motor1.shift_motor_position(-70)
    motor3.shift_motor_position(70)
    sleep(0.1)
    motor6.set_motor_position(20)
    motor8.set_motor_position(20)
    sleep(0.1)
    reset_position()

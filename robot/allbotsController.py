from robot import robotController
from robot.robotMotor import RobotMotor

# set of constants used to replace the motor numbers by more meaningful names
FRONT_LEFT_ELBOW = RobotMotor(0, 0, 180)
FRONT_LEFT_SHOULDER = RobotMotor(1, 30, 120)
FRONT_RIGHT_ELBOW = RobotMotor(2, 0, 180)
FRONT_RIGHT_SHOULDER = RobotMotor(3, 50, 150)
BACK_LEFT_ELBOW = RobotMotor(4, 0, 180)
BACK_LEFT_SHOULDER = RobotMotor(3, 50, 150)
BACK_RIGHT_ELBOW = RobotMotor(6, 0, 180)
BACK_RIGHT_SHOULDER = RobotMotor(7, 30, 120)


def reset_position():
    robotController.set_motor_position(FRONT_LEFT_ELBOW, 10)
    robotController.set_motor_position(FRONT_LEFT_SHOULDER, 30)
    robotController.set_motor_position(FRONT_RIGHT_ELBOW, 10)
    robotController.set_motor_position(FRONT_RIGHT_SHOULDER, 300)
    robotController.set_motor_position(BACK_LEFT_ELBOW, 10)
    robotController.set_motor_position(BACK_LEFT_SHOULDER, 150)
    robotController.set_motor_position(BACK_RIGHT_ELBOW, 10)
    robotController.set_motor_position(BACK_RIGHT_SHOULDER, 150)


def walk_n_steps(n):
    for _ in range(0, n - 1):
        return
        # TODO: implement walk_n_steps for AllbotsController

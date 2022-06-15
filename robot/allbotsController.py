from robot.robotMotor import RobotMotor
import time

MOTORS = {
    "FRONT_LEFT_ELBOW": RobotMotor(0, 0, 180, 160),
    "FRONT_LEFT_SHOULDER": RobotMotor(1, 0, 135, 110),
    "FRONT_RIGHT_ELBOW": RobotMotor(2, 0, 180, 20),
    "FRONT_RIGHT_SHOULDER": RobotMotor(3, 25, 180, 70),
    "BACK_LEFT_ELBOW": RobotMotor(4, 0, 180, 20),
    "BACK_LEFT_SHOULDER": RobotMotor(5, 25, 180, 110),
    "BACK_RIGHT_ELBOW": RobotMotor(6, 0, 180, 20),
    "BACK_RIGHT_SHOULDER": RobotMotor(7, 0, 135, 50)
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


def walk_n_steps(nb_steps: str):
    nb_steps = int(nb_steps)
    for _ in range(nb_steps):
        return
        # TODO: implement walk_n_steps for AllbotsController

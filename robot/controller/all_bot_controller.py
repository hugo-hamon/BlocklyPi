from ..robot_motor import RobotMotor
from time import sleep

MOTORS = {
    "FRONT_LEFT_ELBOW": RobotMotor(0, 10, 180, 160),
    "FRONT_LEFT_SHOULDER": RobotMotor(1, 10, 135, 110),
    "FRONT_RIGHT_ELBOW": RobotMotor(2, 10, 180, 20),
    "FRONT_RIGHT_SHOULDER": RobotMotor(3, 25, 180, 70),
    "BACK_LEFT_ELBOW": RobotMotor(4, 10, 180, 20),
    "BACK_LEFT_SHOULDER": RobotMotor(5, 25, 180, 110),
    "BACK_RIGHT_ELBOW": RobotMotor(6, 10, 180, 20),
    "BACK_RIGHT_SHOULDER": RobotMotor(7, 10, 135, 50)
}


def str_to_int(value: str) -> int:
    """Convert a string to an int"""
    try:
        return int(value)
    except ValueError:
        return 0


class AllBotController:

    def allbot_set_motor_position(self, motor_nb: str, angle: str) -> None:
        """Set the position of a motor by id and angle"""
        for motor in MOTORS.values():
            if motor.id == str_to_int(motor_nb):
                motor.set_motor_position(str_to_int(angle))
                return

    def allbot_shift_motor_position(self, motor_nb: str, angle: str) -> None:
        """Shift the position of a motor by id and angle"""
        for motor in MOTORS.values():
            if motor.id == str_to_int(motor_nb):
                motor.shift_motor_position(str_to_int(angle))
                return

    def allbot_reset_position(self) -> None:
        """Reset the position of all motors"""
        for motor in MOTORS.values():
            motor.reset()
            sleep(0.2)

    # TODO: implement walk_n_steps for AllbotsController
    def allbot_walk_n_steps(self, nb_steps: str) -> None:
        """Walk n steps"""
        for _ in range(str_to_int(nb_steps)):
            return

    def allbot_move_backward(self) -> None:
        """Move backward"""
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
        sleep(0.2)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-50)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(50)

        sleep(0.2)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
        sleep(0.1)
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(130)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(50)

        sleep(0.1)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(50)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-50)
        sleep(0.2)
        # -----------------------------------------------#
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-50)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(50)
        sleep(0.2)
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
        sleep(0.1)
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(50)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-50)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
        sleep(0.1)
        self.allbot_reset_position()

    def allbot_do_hi(self, motor: str) -> None:
        """Do a hi gesture"""
        if motor == '0':
            first_motor = self.allbot_do_hi_by_motor(
                "FRONT_LEFT_SHOULDER", "FRONT_LEFT_ELBOW", 0
            )
        elif motor == '1':
            first_motor = self.allbot_do_hi_by_motor(
                "FRONT_RIGHT_SHOULDER", "FRONT_RIGHT_ELBOW", 180
            )
        else:
            return

        for _ in range(3):
            first_motor.shift_motor_position(50)
            sleep(0.4)
            first_motor.shift_motor_position(-50)
            sleep(0.4)
        self.allbot_reset_position()

    def allbot_do_hi_by_motor(self, motor_1: str, motor_2: str, angle: int) -> RobotMotor:
        result = MOTORS[motor_1]
        other_motor = MOTORS[motor_2]
        self.allbot_reset_position()
        sleep(0.5)
        other_motor.set_motor_position(angle)
        return result
    
    def allbot_turn_left(self) -> None:
        """Turn the robot to the left"""
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
        sleep(0.1)
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(50)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(50)
        sleep(0.1)
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)

        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(60)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(60)
        sleep(0.1)
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-50)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-50)
        sleep(0.1)

        # -------------------------------------#

        sleep(0.1)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(50)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(50)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)

        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-50)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-50)
        sleep(0.2)
        self.allbot_reset_position()

    def allbot_turn_right(self) -> None:
        """Turn the robot to the right"""
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
        sleep(0.1)
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-50)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-50)
        sleep(0.1)
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)

        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(60)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(60)
        sleep(0.1)
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(50)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(50)
        sleep(0.1)

        # -------------------------------------#

        sleep(0.1)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-70)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-70)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)

        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(120)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(60)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(70)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(70)
        sleep(0.2)
        self.allbot_reset_position()


    def allbot_move_forward(self) -> None:
        """Move the robot forward"""
        print("ok")
        print(MOTORS)
        print(MOTORS["FRONT_LEFT_ELBOW"])
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
        sleep(0.2)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(70)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(-110)

        sleep(0.2)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
        sleep(0.1)
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(130)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(50)

        sleep(0.1)
        MOTORS["FRONT_RIGHT_SHOULDER"].shift_motor_position(-70)
        MOTORS["BACK_LEFT_SHOULDER"].shift_motor_position(110)
        sleep(0.2)
        # -----------------------------------------------#
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(70)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(-70)
        sleep(0.2)
        MOTORS["FRONT_LEFT_ELBOW"].set_motor_position(160)
        MOTORS["BACK_RIGHT_ELBOW"].set_motor_position(20)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(50)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(50)
        sleep(0.1)
        MOTORS["BACK_RIGHT_SHOULDER"].shift_motor_position(-70)
        MOTORS["FRONT_LEFT_SHOULDER"].shift_motor_position(70)
        sleep(0.1)
        MOTORS["FRONT_RIGHT_ELBOW"].set_motor_position(20)
        MOTORS["BACK_LEFT_ELBOW"].set_motor_position(20)
        sleep(0.1)
        self.allbot_reset_position()

    def allbot_sleep(self, time: str) -> None:
        """Sleep for a given time"""
        sleep(str_to_int(time))
from typing import Tuple
from time import sleep
import socket
"""
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
"""
MOTORS = {
    "0": "FRONT_LEFT_ELBOW",
    "1": "FRONT_LEFT_SHOULDER",
    "2": "FRONT_RIGHT_ELBOW",
    "3": "FRONT_RIGHT_SHOULDER",
    "4": "BACK_LEFT_ELBOW",
    "5": "BACK_LEFT_SHOULDER",
    "6": "BACK_RIGHT_ELBOW",
    "7": "BACK_RIGHT_SHOULDER"
}


def str_to_int(value: str) -> int:
    """Convert a string to an int"""
    try:
        return int(value)
    except ValueError:
        return 0


class AllBotController:

    def __init__(self, host: str, port: int, server: Tuple[str, int]) -> None:
        self.host = host
        self.port = port
        self.server = server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))

    def allbot_set_motor_position(self, motor_nb: str, angle: str) -> None:
        """Set the position of a motor by id and angle"""
        self.socket.sendto(str.encode(
            f"set {MOTORS[motor_nb]} {angle}"), self.server)

    def allbot_shift_motor_position(self, motor_nb: str, angle: str) -> None:
        """Shift the position of a motor by id and angle"""
        self.socket.sendto(str.encode(
            f"shift {MOTORS[motor_nb]} {angle}"), self.server)

    def allbot_reset_position(self) -> None:
        """Reset the position of all motors"""
        for motor_name in MOTORS.values():
            self.socket.sendto(str.encode(
                f"reset {motor_name}"), self.server)
            sleep(0.2)

    # TODO: implement walk_n_steps for AllbotsController
    def allbot_walk_n_steps(self, nb_steps: str) -> None:
        """Walk n steps"""
        for _ in range(str_to_int(nb_steps)):
            return

    def allbot_move_backward(self) -> None:
        """Move backward"""
        self.allbot_set_motor_position("2", "50")
        self.allbot_set_motor_position("4", "50")
        sleep(0.2)
        self.allbot_shift_motor_position("3", "-50")
        self.allbot_shift_motor_position("5", "50")

        sleep(0.2)
        self.allbot_set_motor_position("2", "20")
        self.allbot_set_motor_position("4", "20")
        sleep(0.1)
        self.allbot_set_motor_position("0", "130")
        self.allbot_set_motor_position("6", "50")

        sleep(0.1)
        self.allbot_shift_motor_position("3", "50")
        self.allbot_shift_motor_position("5", "-50")
        sleep(0.2)
        # -----------------------------------------------#
        self.allbot_shift_motor_position("7", "-50")
        self.allbot_shift_motor_position("1", "50")
        sleep(0.2)
        self.allbot_set_motor_position("0", "160")
        self.allbot_set_motor_position("6", "20")
        sleep(0.1)
        self.allbot_set_motor_position("2", "50")
        self.allbot_set_motor_position("4", "50")
        sleep(0.1)
        self.allbot_shift_motor_position("7", "50")
        self.allbot_shift_motor_position("1", "-50")
        sleep(0.1)
        self.allbot_set_motor_position("2", "20")
        self.allbot_set_motor_position("4", "20")
        sleep(0.1)
        self.allbot_reset_position()

    def allbot_do_hi(self, motor: str) -> None:
        """Do a hi gesture"""
        if motor not in ["0", "1"]:
            return
        first_motor = "1" if motor == '0' else "3"

        for _ in range(3):
            self.allbot_shift_motor_position(first_motor, "50")
            sleep(0.4)
            self.allbot_shift_motor_position(first_motor, "-50")
            sleep(0.4)
        self.allbot_reset_position()

    def allbot_do_hi_by_motor(self, motor_1: str, motor_2: str, angle: str) -> str:
        self.allbot_reset_position()
        sleep(0.5)
        self.allbot_set_motor_position(motor_2, angle)
        return motor_1

    def allbot_turn_left(self) -> None:
        """Turn the robot to the left"""
        self.allbot_set_motor_position("0", "120")
        self.allbot_set_motor_position("6", "60")
        sleep(0.1)
        self.allbot_shift_motor_position("7", "50")
        self.allbot_shift_motor_position("1", "50")
        sleep(0.1)
        self.allbot_set_motor_position("0", "160")
        self.allbot_set_motor_position("6", "20")

        self.allbot_set_motor_position("2", "60")
        self.allbot_set_motor_position("4", "60")
        sleep(0.1)
        self.allbot_shift_motor_position("7", "-50")
        self.allbot_shift_motor_position("1", "-50")
        sleep(0.1)

        # -------------------------------------#

        sleep(0.1)
        self.allbot_shift_motor_position("3", "50")
        self.allbot_shift_motor_position("5", "50")
        sleep(0.1)
        self.allbot_set_motor_position("2", "20")
        self.allbot_set_motor_position("4", "20")

        self.allbot_set_motor_position("0", "120")
        self.allbot_set_motor_position("6", "60")
        sleep(0.1)
        self.allbot_shift_motor_position("3", "-50")
        self.allbot_shift_motor_position("5", "-50")
        sleep(0.2)
        self.allbot_reset_position()

    def allbot_turn_right(self) -> None:
        """Turn the robot to the right"""
        self.allbot_set_motor_position("0", "120")
        self.allbot_set_motor_position("6", "60")
        sleep(0.1)
        self.allbot_shift_motor_position("7", "-50")
        self.allbot_shift_motor_position("1", "-50")
        sleep(0.1)
        self.allbot_set_motor_position("0", "160")
        self.allbot_set_motor_position("6", "20")

        self.allbot_set_motor_position("2", "60")
        self.allbot_set_motor_position("4", "60")
        sleep(0.1)
        self.allbot_shift_motor_position("7", "50")
        self.allbot_shift_motor_position("1", "50")
        sleep(0.1)

        # -------------------------------------#

        sleep(0.1)
        self.allbot_shift_motor_position("3", "-70")
        self.allbot_shift_motor_position("5", "-70")
        sleep(0.1)
        self.allbot_set_motor_position("2", "20")
        self.allbot_set_motor_position("4", "20")

        self.allbot_set_motor_position("0", "120")
        self.allbot_set_motor_position("6", "60")
        sleep(0.1)
        self.allbot_shift_motor_position("3", "70")
        self.allbot_shift_motor_position("5", "70")
        sleep(0.2)
        self.allbot_reset_position()

    def allbot_move_forward(self) -> None:
        """Move the robot forward"""
        print("ok")
        print(MOTORS)
        print(MOTORS["0"])
        self.allbot_set_motor_position("2", "50")
        self.allbot_set_motor_position("4", "50")
        sleep(0.2)
        self.allbot_shift_motor_position("3", "70")
        self.allbot_shift_motor_position("5", "-110")

        sleep(0.2)
        self.allbot_set_motor_position("2", "20")
        self.allbot_set_motor_position("4", "20")
        sleep(0.1)
        self.allbot_set_motor_position("0", "130")
        self.allbot_set_motor_position("6", "50")

        sleep(0.1)
        self.allbot_shift_motor_position("3", "-70")
        self.allbot_shift_motor_position("5", "110")
        sleep(0.2)
        # -----------------------------------------------#
        self.allbot_shift_motor_position("7", "70")
        self.allbot_shift_motor_position("1", "-70")
        sleep(0.2)
        self.allbot_set_motor_position("0", "160")
        self.allbot_set_motor_position("6", "20")
        sleep(0.1)
        self.allbot_set_motor_position("2", "50")
        self.allbot_set_motor_position("4", "50")
        sleep(0.1)
        self.allbot_shift_motor_position("7", "-70")
        self.allbot_shift_motor_position("1", "70")
        sleep(0.1)
        self.allbot_set_motor_position("2", "20")
        self.allbot_set_motor_position("4", "20")
        sleep(0.1)
        self.allbot_reset_position()

    def allbot_sleep(self, time: str) -> None:
        """Sleep for a given time"""
        sleep(str_to_int(time))

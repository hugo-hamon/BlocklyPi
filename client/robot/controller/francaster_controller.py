from typing import Tuple
from time import sleep
import socket

MOTORS = {
    "9": "LEFT_ELBOW",
    "6": "LEFT_SHOULDER_ABDUCTOR",
    "5": "LEFT_SHOULDER_ROTATOR",
    "3": "LEFT_SHOULDER_FLEXOR",
    "2": "RIGHT_SHOULDER_FLEXOR",
    "4": "RIGHT_SHOULDER_ABDUCTOR",
    "7": "RIGHT_SHOULDER_ROTATOR",
    "8": "RIGHT_ELBOW",
    "11": "LEFT_HIP",
    "12": "LEFT_KNEE",
    "15": "LEFT_ANKLE",
    "10": "RIGHT_HIP",
    "13": "RIGHT_KNEE",
    "14": "RIGHT_ANKLE",
    "1": "HEAD_YAW",
    "0": "HEAD_PITCH"
}


def str_to_int(value: str) -> int:
    """Convert a string to an int"""
    try:
        return int(value)
    except ValueError:
        return 0


class FrancasterController:

    def __init__(self, host: str, port: int, server: Tuple[str, int]) -> None:
        self.host = host
        self.port = port
        self.server = server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((host, port))

    def francaster_set_motor_position(self, motor_nb: str, angle: str) -> None:
        """Set the position of a motor by id and angle"""
        self.socket.sendto(str.encode(
            f"set {MOTORS[motor_nb]} {angle}"), self.server)

    def francaster_shift_motor_position(self, motor_nb: str, angle: str) -> None:
        """Shift the position of a motor by id and angle"""
        self.socket.sendto(str.encode(
            f"shift {MOTORS[motor_nb]} {angle}"), self.server)

    def francaster_sleep(self, seconds: str) -> None:
        """Set the delay between each motor movement"""
        sleep(str_to_int(seconds))

    def francaster_reset_position(self) -> None:
        """Reset the position of all motors"""
        for motor_name in MOTORS.values():
            self.socket.sendto(str.encode(
                f"reset {motor_name}"), self.server)
            sleep(0.2)

    def francaster_do_hello(self, nb_greetings: str) -> None:
        """Do a hello gesture"""
        self.francaster_set_motor_position("1", "170")
        self.francaster_set_motor_position("6", "10")
        for _ in range(str_to_int(nb_greetings)):
            self.francaster_set_motor_position("0", "0")
            sleep(0.5)
            self.francaster_set_motor_position("0", "150")
            sleep(0.5)

    def francaster_do_bye(self, nb_greetings: str) -> None:
        """Do a bye gesture"""
        self.francaster_set_motor_position("1", "170")
        self.francaster_set_motor_position("6", "10")
        for _ in range(str_to_int(nb_greetings)):
            self.francaster_set_motor_position("8", "60")
            sleep(0.5)
            self.francaster_set_motor_position("8", "0")
            sleep(0.5)
            self.francaster_set_motor_position("11", "60")
            sleep(0.5)
            self.francaster_set_motor_position("11", "0")
            sleep(0.5)

    def francaster_walk_n_steps_with_knee_lift(self, nb_steps: str) -> None:
        """Walk n steps with knee lift"""
        self.francaster_walk_n_steps(nb_steps)

    def francaster_walk_n_steps(self, nb_steps: str) -> None:
        """Walk n steps"""
        for _ in range(str_to_int(nb_steps)):
            self.francaster_set_motor_position("3", "60")
            sleep(0.1)
            self.francaster_set_motor_position("4", "60")
            sleep(0.1)
            self.francaster_set_motor_position("8", "120")
            sleep(0.1)
            self.francaster_set_motor_position("11", "120")
            sleep(0.5)
            self.francaster_set_motor_position("3", "120")
            sleep(0.1)
            self.francaster_set_motor_position("4", "120")
            sleep(0.1)
            self.francaster_set_motor_position("8", "60")
            sleep(0.1)
            self.francaster_set_motor_position("11", "60")
            sleep(0.5)

    def francaster_do_no(self, nb_gestures: str) -> None:
        """Do a no gesture"""
        for _ in range(str_to_int(nb_gestures)):
            sleep(0.5)
            self.francaster_set_motor_position("14", "120")
            sleep(0.5)
            self.francaster_set_motor_position("14", "60")

    def francaster_do_yes(self) -> None:
        """Do a yes gesture"""
        sleep(0.5)
        self.francaster_set_motor_position("14", "60")
        sleep(0.5)
        self.francaster_set_motor_position("14", "120")

    def francaster_speak(self, text: str) -> None:
        """Speak a text"""
        self.socket.sendto(str.encode(f"speak {text}"), self.server)

    def francaster_repeat(self) -> None:
        """Repeat what you said"""
        self.socket.sendto(str.encode("repeat"), self.server)

    def francaster_answer_question(self, question="") -> None:
        """Answer to a question"""
        self.socket.sendto(str.encode(f"answer {question}"), self.server)

    def francaster_slap(self) -> None:
        self.francaster_set_motor_position("0", "100")
        sleep(0.3)
        self.francaster_set_motor_position("2", "0")
        sleep(0.3)
        self.francaster_set_motor_position("3", "0")
        sleep(0.3)
        self.francaster_set_motor_position("2", "180")
        sleep(2)
        self.francaster_reset_position()

    def francaster_raise_right_foot(self) -> None:
        """Raise the right foot"""
        self.francaster_set_motor_position("11", "180")
        self.francaster_set_motor_position("12", "90")

    def francaster_raise_left_foot(self) -> None:
        """Raise the left foot"""
        self.francaster_set_motor_position("8", "180")
        self.francaster_set_motor_position("9", "90")

    def francaster_do_hi(self, nb_greetings: str) -> None:
        """Do a hi gesture"""
        self.francaster_set_motor_position("5", "90")
        sleep(0.5)
        

    def francaster_listen_and_answer(self) -> None:
        """Listen and answer"""
        self.socket.sendto(str.encode("question"), self.server)

    def francaster_dance(self) -> None:
        """Listen and answer"""
        self.francaster_set_motor_position("1", "180")
        self.francaster_set_motor_position("5", "0")
        sleep(1)
        self.francaster_set_motor_position("2", "60")
        self.francaster_set_motor_position("6", "120")
        sleep(1)
        self.francaster_set_motor_position("2", "60")
        self.francaster_set_motor_position("6", "120")
        sleep(1)
        self.francaster_set_motor_position("0", "30")
        self.francaster_set_motor_position("7", "150")
        sleep(1)
        self.francaster_set_motor_position("1", "0")
        self.francaster_set_motor_position("5", "180")

    def francaster_start_camera(self) -> None:
        """Start the camera"""
        self.socket.sendto(str.encode("video_start"), self.server)

    def francaster_stop_camera(self) -> None:
        """Stop the camera"""
        self.socket.sendto(str.encode("video_stop"), self.server)

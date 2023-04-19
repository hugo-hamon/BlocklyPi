from ..speech.francaster_speech import FrancasterSpeech
from ..robot_motor import RobotMotor
from time import sleep


# TODO: Revoir les moteurs
MOTORS = {
    "LEFT_ELBOW": RobotMotor(0, 0, 180, 180),
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
    "HEAD_PITCH": RobotMotor(15, 0, 140, 90),
}

def str_to_int(value: str) -> int:
    """Convert a string to an int"""
    try:
        return int(value)
    except ValueError:
        return 0


class FrancasterController:

    def __init__(self) -> None:
        self.speech = FrancasterSpeech()

    def francaster_set_motor_position(self, motor_nb: str, angle: str) -> None:
        """Set the position of a motor by id and angle"""
        for motor in MOTORS.values():
            if motor.id == str_to_int(motor_nb):
                motor.set_motor_position(str_to_int(angle))
                return

    def francaster_shift_motor_position(self, motor_nb: str, angle: str) -> None:
        """Shift the position of a motor by id and angle"""
        for motor in MOTORS.values():
            if motor.id == str_to_int(motor_nb):
                motor.shift_motor_position(str_to_int(angle))
                return

    def francaster_sleep(self, seconds: str) -> None:
        """Set the delay between each motor movement"""
        sleep(str_to_int(seconds))

    def francaster_reset_position(self) -> None:
        """Reset the position of all motors"""
        for motor in MOTORS.values():
            motor.reset()
            sleep(0.2)

    def francaster_do_hello(self, nb_greetings: str) -> None:
        """Do a hello gesture"""
        MOTORS["LEFT_SHOULDER_ABDUCTOR"].set_motor_position(170)
        MOTORS["RIGHT_SHOULDER_ROTATOR"].set_motor_position(10)
        for _ in range(str_to_int(nb_greetings)):
            MOTORS["LEFT_ELBOW"].set_motor_position(0)
            sleep(0.5)
            MOTORS["LEFT_ELBOW"].set_motor_position(150)
            sleep(0.5)

    def francaster_do_bye(self, nb_greetings: str) -> None:
        """Do a bye gesture"""
        MOTORS["LEFT_SHOULDER_ABDUCTOR"].set_motor_position(170)
        MOTORS["RIGHT_SHOULDER_ROTATOR"].set_motor_position(10)
        for _ in range(str_to_int(nb_greetings)):
            MOTORS["LEFT_HIP"].set_motor_position(60)
            sleep(.5)
            MOTORS["LEFT_HIP"].set_motor_position(0)
            sleep(.5)
            MOTORS["RIGHT_HIP"].set_motor_position(60)
            sleep(.5)
            MOTORS["RIGHT_HIP"].set_motor_position(0)
            sleep(.5)

    def francaster_walk_n_steps_with_knee_lift(self, nb_steps: str) -> None:
        """Walk n steps with knee lift"""
        MOTORS["LEFT_SHOULDER_ROTATOR"].set_motor_position(170)
        MOTORS["RIGHT_SHOULDER_ABDUCTOR"].set_motor_position(10)
        for _ in range(str_to_int(nb_steps)):
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

    def francaster_walk_n_steps(self, nb_steps: str) -> None:
        """Walk n steps"""
        for _ in range(str_to_int(nb_steps) - 1):
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

    def francaster_do_no(self, nb_gestures: str) -> None:
        """Do a no gesture"""
        for _ in range(str_to_int(nb_gestures)):
            sleep(.5)
            MOTORS["HEAD_YAW"].set_motor_position(120)
            sleep(.5)
            MOTORS["HEAD_YAW"].set_motor_position(60)

    def francaster_do_yes(self) -> None:
        """Do a yes gesture"""
        sleep(.5)
        MOTORS["HEAD_YAW"].set_motor_position(60)
        sleep(.5)
        MOTORS["HEAD_YAW"].set_motor_position(120)

    def francaster_speak(self, text: str) -> None:
        """Speak a text"""
        self.speech.speak(text)

    def francaster_repeat(self) -> None:
        """Repeat what you said"""
        FrancasterSpeech().repeat()

    def francaster_answer_question(self, question="") -> None:
        """Answer to a question"""
        FrancasterSpeech().answer(question)

    def francaster_slap(self) -> None:
        MOTORS["LEFT_ELBOW"].set_motor_position(100)
        sleep(0.3)
        MOTORS["LEFT_SHOULDER_ROTATOR"].set_motor_position(0)
        sleep(0.3)
        MOTORS["LEFT_SHOULDER_FLEXOR"].set_motor_position(0)
        sleep(0.3)
        MOTORS["LEFT_SHOULDER_ROTATOR"].set_motor_position(180)
        sleep(2)
        self.francaster_reset_position()

    def francaster_raise_right_foot(self) -> None:
        """Raise the right foot"""
        MOTORS["RIGHT_HIP"].set_motor_position(180)
        MOTORS["RIGHT_KNEE"].set_motor_position(90)

    def francaster_raise_left_foot(self) -> None:
        """Raise the left foot"""
        MOTORS["LEFT_HIP"].set_motor_position(180)
        MOTORS["LEFT_KNEE"].set_motor_position(90)

    def francaster_do_hi(self, nb_greetings: str) -> None:
        """Do a hi gesture"""
        MOTORS["RIGHT_SHOULDER_ABDUCTOR"].set_motor_position(130)
        sleep(.1)
        MOTORS["RIGHT_SHOULDER_ROTATOR"].set_motor_position(180)
        sleep(.1)
        for _ in range(str_to_int(nb_greetings)):
            MOTORS["RIGHT_ELBOW"].set_motor_position(90)
            sleep(0.5)
            MOTORS["RIGHT_ELBOW"].set_motor_position(0)
            sleep(0.5)

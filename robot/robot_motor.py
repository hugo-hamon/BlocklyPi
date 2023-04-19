from adafruit_servokit import ServoKit
import logging


class RobotMotor:
    """
    RobotMotor stores all the data relative to a motor
    """

    # constants used for the is_in_range function
    IN_RANGE = 0
    BELOW_RANGE = -1
    ABOVE_RANGE = 1

    def __init__(self, id: int, min_angle: int, max_angle: int, initial_angle: int):
        self.id = id
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.initial_angle = initial_angle
        # self.servo_kit = ServoKit(channels=16)

    def is_in_range(self, angle: int) -> int:
        """Check if the given angle is in the range of the motor"""
        if self.min_angle <= angle <= self.max_angle:
            return self.IN_RANGE
        elif self.min_angle > angle:
            return self.BELOW_RANGE
        else:
            return self.ABOVE_RANGE

    def set_motor_position(self, angle: int) -> None:
        """Set the motor position to the given angle"""
        in_range = self.is_in_range(angle)
        if in_range == 0:
            self.servo_kit.servo[self.id].angle = angle
        elif in_range == -1:
            self.servo_kit.servo[self.id].angle = self.min_angle
        elif in_range == 1:
            self.servo_kit.servo[self.id].angle = self.max_angle

    def shift_motor_position(self, angle: int) -> None:
        """Shift the motor position by the given angle"""
        servo_angle = self.servo_kit.servo[self.id].angle
        if servo_angle is None:
            logging.warning("Servo is not initialized")
            return
        shifted_angle = servo_angle + angle
        in_range = self.is_in_range(round(shifted_angle))
        if in_range == 0:
            servo_angle += angle
        elif in_range == -1:
            servo_angle = self.min_angle
        elif in_range == 1:
            servo_angle = self.max_angle
        self.servo_kit.servo[self.id].angle = round(servo_angle)

    def reset(self) -> None:
        """Reset the motor position to the initial angle"""
        self.set_motor_position(self.initial_angle)

from adafruit_servokit import ServoKit
from robotMotor import RobotMotor

"""
robotController implements the common methods on which every robot is based. any robot controller should inherit
from this class. It defines the general constants, the constants associated with the motors number should be defined
in the robot controller class.
"""

# constants used for the is_in_range function
IN_RANGE = 0
BELOW_RANGE = -1
ABOVE_RANGE = 1

servo_kit = ServoKit(channels=16)


def is_in_range(angle: int, motor: RobotMotor):
    """
    @:param
        - motor_nb: the motor number.
        - angle: the set-point angle.
        - motor: the motor tested.
    @:return
        - IN_RANGE if angle is within the value provided by angle is between the values provided by range.
        - BELOW_RANGE if it is below the minimum value.
        - ABOVE_RANGE if it is above the maximum value.
    """
    if motor.min_angle <= angle <= motor.max_angle:
        return IN_RANGE
    elif motor.min_angle > angle:
        return BELOW_RANGE
    else:
        return ABOVE_RANGE


def set_motor_position(motor: RobotMotor, angle: int):
    in_range = is_in_range(angle, motor)
    if in_range == 0:
        servo_kit.servo[motor.id].angle = angle
    elif in_range == -1:
        servo_kit.servo[motor.id].angle = motor.min_angle
    elif in_range == 1:
        servo_kit.servo[motor.id].angle = motor.max_angle


def shift_motor_position(motor: RobotMotor, angle: int):
    shifted_angle = servo_kit.servo[motor.id].angle + angle
    in_range = is_in_range(shifted_angle, motor)
    if in_range == 0:
        servo_kit.servo[motor.id].angle += angle
    elif in_range == -1:
        servo_kit.servo[motor.id].angle = motor.min_angle
    elif in_range == 1:
        servo_kit.servo[motor.id].angle = motor.max_angle

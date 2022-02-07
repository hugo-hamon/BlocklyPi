from adafruit_servokit import ServoKit


class RobotController:
    """
    RobotController implements the common methods on which every robot is based. any robot controller should inherit
    from this class. It defines the general constants, the constants associated with the motors number should be defined
    in the robot controller class.
    """

    # Indicate the range of motion of each motor in the robot.
    # - The keys are the motors numbers. Prefer to use class constants to name the motors for readability and
    #     maintainability.
    # - The values are a tuple of ints containing the minimum and the maximum angles of the range.
    MOTORS_RANGES = {}

    # constants used for the is_in_range function
    IN_RANGE = 0
    BELOW_RANGE = -1
    ABOVE_RANGE = 1

    servo_kit = ServoKit(channels=16)

    def is_in_range(self, motor_nb, angle):
        """
        return IN_RANGE if angle is within the range associated with motor_nb, BELOW_RANGE if below and ABOVE_RANGE if
        above
        """
        mi, ma = self.MOTORS_RANGES[motor_nb]
        if mi <= angle <= ma:
            return self.IN_RANGE
        elif mi > angle:
            return self.BELOW_RANGE
        else:
            return self.ABOVE_RANGE

    def set_motor_position(self, motor_nb: int, angle: int):
        mi, ma = self.MOTORS_RANGES[motor_nb]
        if self.is_in_range(motor_nb, angle) == 0:
            self.servo_kit.servo[motor_nb].angle = angle
        elif self.is_in_range(motor_nb, angle) == -1:
            self.servo_kit.servo[motor_nb].angle = mi
        elif self.is_in_range(motor_nb, angle) == 1:
            self.servo_kit.servo[motor_nb].angle = ma

    def shift_motor_position(self, motor_nb: int, angle: int):
        shifted_angle = self.servo_kit.servo[motor_nb].angle + angle
        mi, ma = self.MOTORS_RANGES[motor_nb]
        if self.is_in_range(motor_nb, shifted_angle) == 0:
            self.servo_kit.servo[motor_nb].angle += angle
        elif self.is_in_range(motor_nb, shifted_angle) == -1:
            self.servo_kit.servo[motor_nb].angle = mi
        elif self.is_in_range(motor_nb, shifted_angle) == 1:
            self.servo_kit.servo[motor_nb].angle = ma

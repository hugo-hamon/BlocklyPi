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

    def is_in_range(self, motor_nb: int, angle: int, range: (int, int)):
        """
        @:param
            - motor_nb: the motor number.
            - angle: the set-point angle.
            - range: a tuple containing the minimum and maximum angle of the motor.
        @:return
            - IN_RANGE if angle is within the value provided by angle is between the values provided by range.
            - BELOW_RANGE if it is below the minimum value.
            - ABOVE_RANGE if it is above the maximum value.
        above
        """
        if range[0] <= angle <= range[1]:
            return self.IN_RANGE
        elif range[0] > angle:
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

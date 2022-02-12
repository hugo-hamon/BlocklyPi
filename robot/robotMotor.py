class RobotMotor:
    """
    RobotController stores all the data relative to a motor.
    """

    # the number of the connector on which the motor is connected on the card
    id: int

    min_angle: int
    max_angle: int

    def __init__(self, id, min_angle, max_angle):
        self.id = id
        self.min_angle = min_angle
        self.max_angle = max_angle

from robot import RobotController


class AllbotsController(RobotController):
    # set of constants used to replace the motor numbers by more meaningful names
    FRONT_LEFT_ELBOW = 0
    FRONT_LEFT_SHOULDER = 1
    FRONT_RIGHT_ELBOW = 2
    FRONT_RIGHT_SHOULDER = 3
    BACK_LEFT_ELBOW = 4
    BACK_LEFT_SHOULDER = 5
    BACK_RIGHT_ELBOW = 6
    BACK_RIGHT_SHOULDER = 7

    MOTORS_RANGES = {
        FRONT_LEFT_ELBOW: (0, 180),
        FRONT_LEFT_SHOULDER: (30, 120),
        FRONT_RIGHT_ELBOW: (0, 180),
        FRONT_RIGHT_SHOULDER: (50, 150),
        BACK_LEFT_ELBOW: (0, 180),
        BACK_LEFT_SHOULDER: (50, 150),
        BACK_RIGHT_ELBOW: (0, 180),
        BACK_RIGHT_SHOULDER: (30, 120)
    }

    def reset_position(self):
        self.set_motor_position(self.FRONT_LEFT_ELBOW, 10)
        self.set_motor_position(self.FRONT_LEFT_SHOULDER, 30)
        self.set_motor_position(self.FRONT_RIGHT_ELBOW, 10)
        self.set_motor_position(self.FRONT_RIGHT_SHOULDER, 300)
        self.set_motor_position(self.BACK_LEFT_ELBOW, 10)
        self.set_motor_position(self.BACK_LEFT_SHOULDER, 150)
        self.set_motor_position(self.BACK_RIGHT_ELBOW, 10)
        self.set_motor_position(self.BACK_RIGHT_SHOULDER, 150)

    def __init__(self):
        self.reset_position()

    def walk_n_steps(self, n):
        for _ in range(0, n - 1):
            return
            # TODO: implement walk_n_steps for AllbotsController

from robot_motor import RobotMotor
import socket


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


class Server:

    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))

    def start(self) -> None:
        """Starts the server"""
        print("Server Started")
        while True:
            data, addr = self.socket.recvfrom(1024)
            data = data.decode('utf-8')
            print(f"Message from: {str(addr)}")
            print(f"Message: {data}")
            self.process_data(data)

    def process_data(self, data: str):
        datas = data.split()
        if not datas:
            return

        if datas[0] == "set":
            if len(datas) != 3:
                return
            if datas[1] in MOTORS:
                MOTORS[datas[1]].set_motor_position(str_to_int(datas[2]))
        elif datas[0] == "shift":
            if len(datas) != 3:
                return
            if datas[1] in MOTORS:
                MOTORS[datas[1]].shift_motor_position(str_to_int(datas[2]))
        elif datas[0] == "reset":
            if len(datas) != 2:
                return
            if datas[1] in MOTORS:
                MOTORS[datas[1]].reset()


if __name__ == '__main__':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host = s.getsockname()[0]
        s.close()
    except Exception as e:
        raise e
    port = 4000
    server = Server(host, port)
    server.start()

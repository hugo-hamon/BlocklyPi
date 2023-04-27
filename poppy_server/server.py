from speech.francaster_speech import FrancasterSpeech
from video_capture import capture_video
from robot_motor import RobotMotor
import threading
import socket


MOTORS = {
    "HEAD_PITCH": RobotMotor(0, 0, 60, 30),
    "HEAD_YAW": RobotMotor(1, 0, 180, 90),
    "RIGHT_SHOULDER_FLEXOR": RobotMotor(2, 0, 180, 90),
    "LEFT_SHOULDER_FLEXOR": RobotMotor(3, 0, 180, 90),
    "RIGHT_SHOULDER_ABDUCTOR": RobotMotor(4, 0, 180, 0),
    "LEFT_SHOULDER_ROTATOR": RobotMotor(5, 0, 180, 180),
    "LEFT_SHOULDER_ABDUCTOR": RobotMotor(6, 0, 180, 90),
    "RIGHT_SHOULDER_ROTATOR": RobotMotor(7, 0, 180, 90),
    "RIGHT_ELBOW": RobotMotor(8, 0, 140, 0),
    "LEFT_ELBOW": RobotMotor(9, 0, 180, 180),
    "RIGHT_HIP": RobotMotor(10, 0, 180, 90),
    "LEFT_HIP": RobotMotor(11, 0, 180, 90),
    "LEFT_KNEE": RobotMotor(12, 0, 135, 0),
    "RIGHT_KNEE": RobotMotor(13, 45, 180, 180),
    "RIGHT_ANKLE": RobotMotor(14, 0, 120, 75),
    "LEFT_ANKLE": RobotMotor(15, 0, 100, 45),
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
        elif datas[0] == "answer":
            questions = " ".join(datas[1:])
            FrancasterSpeech().answer(questions)
        elif datas[0] == "repeat":
            FrancasterSpeech().repeat()
        elif datas[0] == "reset":
            if len(datas) != 2:
                return
            if datas[1] in MOTORS:
                MOTORS[datas[1]].reset()
        elif datas[0] == "question":
            FrancasterSpeech().answer(FrancasterSpeech().record("Pose moi une question."))


def run_server() -> None:
    """Run the server"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host = s.getsockname()[0]
        s.close()
    except Exception as e:
        raise e
    print(f"The server will run on {host}")
    port = 4000
    server = Server(host, port)
    server.start()


def video_capture() -> None:
    """Run the video capture"""
    capture_video()


if __name__ == '__main__':
    run_server_thread = threading.Thread(target=run_server)
    run_server_thread.start()

    video_capture_thread = threading.Thread(target=video_capture)
    video_capture_thread.start()

    run_server_thread.join()
    video_capture_thread.join()

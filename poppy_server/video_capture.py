from speech.francaster_speech import FrancasterSpeech
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Lock
import face_recognition
import contextlib
import time
import cv2
import os


FRAME_RATE = 0.5


class FaceRecognition:

    def __init__(self):
        self.francaster = FrancasterSpeech()
        self.known_images = [
            face_recognition.load_image_file(f"image/{image}")
            for image in os.listdir("image")
        ]
        self.known_face_names = [name.split(".")[0]
                                 for name in os.listdir("image")]

        self.running = False

    def _load_known_images_encoding(self):
        """Load all known images and return their encoding"""
        known_images_encoding = []
        for image in self.known_images:
            with contextlib.suppress(IndexError):
                known_images_encoding.append(
                    face_recognition.face_encodings(image)[0])
        return known_images_encoding

    def _compare_face_encodings(self, known_images_encoding, face_encodings, face_locations, welcome_name, frame):
        """Compare face encoding with known images encoding and return the name of the person if it's in the known images"""
        for face_encoding, _ in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(
                known_images_encoding, face_encoding)
            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]
                if name not in welcome_name:
                    self.francaster.speak(f"Bonjour {name}")
                    welcome_name.append(name)
            else:
                self.register_face(frame)

    def register_face(self, frame: cv2.VideoCapture) -> None:
        """Register a face and save it in the image folder"""
        name = ""
        while not name:
            name = self.francaster.record(
                "Je vais prendre une photo de toi, quel est ton nom ?")
        self.francaster.speak("Photo dans")
        for i in range(3, 0, -1):
            self.francaster.speak(str(i))
            time.sleep(1)
        cv2.imwrite(f"image/{name}.jpg", frame)
        self.francaster.speak("Merci, je t'ai ajouté à ma base de donnée")

    def process_face(self, frame: cv2.VideoCapture) -> None:
        """Process the face and ask if the person want to register his face"""
        self.francaster.speak("Bonjour inconnu")
        answer = ""
        while not answer:
            answer = self.francaster.record(
                "Veut tu que j'enregistre ton visage ?")
        if "oui" in answer.lower() or "ok" in answer.lower():
            self.register_face(frame)
        elif "non" in answer.lower():
            self.francaster.speak("D'accord, je ne prendrais pas de photo")
        else:
            self.francaster.speak("Désolé je n'ai pas compris")

    def capture_video(self, video_capture: cv2.VideoCapture) -> None:
        """Capture the video and process the face"""
        known_images_encoding = self._load_known_images_encoding()

        welcome_name = []
        prev = 0
        while self.running:
            print("running", time.time())
            time_elapsed = time.time() - prev
            _, frame = video_capture.read()
            if time_elapsed < 1. / FRAME_RATE:
                continue
            prev = time.time()

            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(
                frame, face_locations)
            print("ok 1")
            # cv2.imshow('Video', frame)
            print("ok 2")
            self._compare_face_encodings(
                known_images_encoding, face_encodings, face_locations, welcome_name, frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or not self.running:
                break

    def run(self) -> None:
        """Run the face recognition"""
        video_capture = cv2.VideoCapture(0)

        self.capture_video(video_capture)
        video_capture.release()
        cv2.destroyAllWindows()

    def start(self) -> None:
        """Start in a new thread the face recognition"""
        if not self.running:
            self.running = True
            thread = Thread(target=self.run)
            thread.start()

    def stop(self) -> None:
        """Stop the face recognition"""
        if self.running:
            self.running = False
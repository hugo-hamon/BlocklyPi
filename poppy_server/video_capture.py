from speech.francaster_speech import FrancasterSpeech
import face_recognition
import cv2
import os


def capture_video():
    know_images = [
        face_recognition.load_image_file(f"image/{image}")
        for image in os.listdir("image")
    ]

    # Extraire les encodages de visages pour les images connues
    known_images_encoding = [
        face_recognition.face_encodings(image)[0]
        for image in know_images
    ]

    # Créer un tableau des encodages et des noms correspondants
    known_face_names = [name.split(".")[0] for name in os.listdir("image")]
    # Initialiser la capture vidéo
    video_capture = cv2.VideoCapture(0)

    welcome_name = []

    while True:
        _, frame = video_capture.read()

        # Trouver les visages et les encodages dans l'image actuelle
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Comparer les encodages des visages trouvés avec les encodages connus
        for face_encoding, _ in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(
                known_images_encoding, face_encoding)

            # Trouver le visage correspondant
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                if name not in welcome_name:
                    FrancasterSpeech().speak(f"Bonjour {name}")
                    welcome_name.append(name)


        # Quitter le programme en appuyant sur 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer la capture vidéo et fermer les fenêtres
    video_capture.release()
    cv2.destroyAllWindows()

from speech.francaster_speech import FrancasterSpeech
import face_recognition
import contextlib
import time
import cv2
import os


def capture_video():
    know_images = [
        face_recognition.load_image_file(f"image/{image}")
        for image in os.listdir("image")
    ]

    # Extraire les encodages de visages pour les images connues
    known_images_encoding = []
    for image in know_images:
        with contextlib.suppress(IndexError):
            known_images_encoding.append(face_recognition.face_encodings(image)[0])
    # Créer un tableau des encodages et des noms correspondants
    known_face_names = [name.split(".")[0] for name in os.listdir("image")]
    # Initialiser la capture vidéo
    video_capture = cv2.VideoCapture(0)

    welcome_name = []
    unknown_count = 0
    while True:
        _, frame = video_capture.read()
        print(unknown_count, time.time())
        # Trouver les visages et les encodages dans l'image actuelle
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Comparer les encodages des visages trouvés avec les encodages connus
        for face_encoding, _ in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(
                known_images_encoding, face_encoding)

            # Trouver le visage correspondant
            if True in matches:
                unknown_count = 0
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                if name not in welcome_name:
                    FrancasterSpeech().speak(f"Bonjour {name}")
                    welcome_name.append(name)
            else:
                unknown_count += 1
                if unknown_count == 2:
                    unknown_count = 0
                    FrancasterSpeech().speak("Bonjour inconnu")
                    answer = ""
                    while not answer:
                        answer = FrancasterSpeech().record("Veut tu que j'enregistre ton visage ?")
                    if "oui" in answer.lower() or "ok" in answer.lower():
                        name = ""
                        while not name:
                            name = FrancasterSpeech().record(
                                "Je vais prendre une photo de toi, quel est ton nom ?")
                        FrancasterSpeech().speak("Photo dans")
                        for i in range(3, 0, -1):
                            FrancasterSpeech().speak(str(i))
                            time.sleep(1)
                        cv2.imwrite(f"image/{name}.jpg", frame)
                        FrancasterSpeech().speak("Merci, je t'ai ajouté à ma base de donnée")
                    elif "non" in answer.lower():
                        FrancasterSpeech().speak("D'accord, je ne prendrais pas de photo")
                    else:
                        FrancasterSpeech().speak("Désolé je n'ai pas compris")

        # Quitter le programme en appuyant sur 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(1)

    # Libérer la capture vidéo et fermer les fenêtres
    video_capture.release()
    cv2.destroyAllWindows()

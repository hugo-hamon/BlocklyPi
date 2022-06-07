import webbrowser
import speech_recognition as sr
import os
import random
from gtts import gTTS
import pygame
import time

r = sr.Recognizer()
m = sr.Microphone()


def record_audio(ask='', lang='fr'):
    with m as source:
        r.adjust_for_ambient_noise(source)
        if ask != '':
            print(ask)
        audio = r.listen(source, timeout=5)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language=lang)
        except sr.UnknownValueError:
            francaster_speak("Désolé je n'ai pas compris")
        except sr.RequestError:
            francaster_speak("Une erreur c'est produite")
        return voice_data


def francaster_speak(audio_string, lang='fr'):
    pygame.mixer.init()
    print(audio_string)
    tts = gTTS(text=audio_string, lang=lang)
    random_int = random.randint(1, 1000)
    audio_file = "file-" + str(random_int) + ".mp3"
    tts.save(audio_file)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    time.sleep(0.25)
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    os.remove(audio_file)


def francaster_repeat(lang='fr'):
    a = record_audio("recording...", lang=lang)
    francaster_speak(a, lang=lang)


def answer(a=None):
    if a is None:
        a = record_audio("recording...")
    if "comment tu t'appelles" in a:
        francaster_speak("je m'appelle francaster")
    if "quelle heure est-il" in a:
        francaster_speak(time.strftime("%H:%M"))
    if "recherche" in a:
        search = record_audio("Que cherchez-vous?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print("Voila ce que j'ai trouvé pour \t" + search)
    if "trouve une adresse" in a:
        location = record_audio("Que cherchez-vous?")
        url = 'https://www.google.fr/maps/place/' + location
        webbrowser.get().open(url)
        print("Voila ce que j'ai trouvé pour \t" + location)
    if "stop" in a:
        francaster_speak("À bientôt!")
        exit()

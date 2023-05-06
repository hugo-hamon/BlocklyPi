from __future__ import annotations
from .event_handler import FrancasterEvent
import speech_recognition as sr
from unidecode import unidecode
from gtts import gTTS
import pygame as pg
import logging
import string
import time
import os


def generate_sound(name: str, text: str) -> None:
    """Generate sound file from text"""
    name = normalize_text(name)
    try:
        audio_file = f"speech/sound/{name}.mp3"
        if os.path.exists(audio_file):
            return
        tts = gTTS(text=text, lang="fr")
        tts.save(audio_file)
    except Exception:
        print(f"Erreur pour la question {name}")


def normalize_text(text: str) -> str:
    text = text.lower()
    text = unidecode(text)
    text = text.translate(str.maketrans(
        string.punctuation, ' ' * len(string.punctuation)))
    text = ' '.join(text.split())
    return text


class FrancasterSpeech:
    def __init__(self, language="fr") -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        self.event_handler = FrancasterEvent(self)

    def record(self, ask="") -> str:
        """Record audio from the microphone and return the recognized text"""
        try:
            return self.__record(ask)
        except Exception as e:
            print(e)
            return self.record("Répéter s'il vous plaît")

    def __record(self, ask):
        if ask != "":
            self.speak(ask)
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(
                source)
            voice_text = ""
            try:
                voice_text = self.recognizer.recognize_google(
                    audio, language=self.language)
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                self.speak(
                    "Désolé, mon service de reconnaissance vocale est indisponible")
            if type(voice_text) != str:
                voice_text = ""
            return unidecode(voice_text)

    def speak(self, text: str) -> None:
        """Speak the given text"""
        pg.mixer.init()
        logging.info(f"Speaking: {text}")

        if os.path.exists(f"speech/sound/{text}.mp3"):
            self.speak_from_file(f"speech/sound/{text}.mp3")
            return
        else:
            self.play_sound(text)

    def play_sound(self, text):
        tts = gTTS(text=text, lang=self.language)
        normalize = normalize_text(text)
        audio_file = f"speech/sound/{normalize}.mp3"
        tts.save(audio_file)
        pg.mixer.music.load(audio_file)
        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            time.sleep(0.1)

    def speak_from_file(self, path: str) -> None:
        pg.mixer.init()
        pg.mixer.music.load(path)
        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            time.sleep(0.1)

    def repeat(self) -> None:
        """Record audio from the microphone and repeat it"""
        self.speak(self.record("A vous de parler"))

    def answer(self, question: str) -> None:
        """Answer to the given question"""
        self.event_handler.process_question(question)

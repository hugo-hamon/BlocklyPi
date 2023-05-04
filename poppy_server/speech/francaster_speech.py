from __future__ import annotations
from .event_handler import FrancasterEvent
import speech_recognition as sr
from unidecode import unidecode
from gtts import gTTS
import pygame as pg
import logging
import random
import time
import os


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
        except Exception:
            return self.record("Répéter s'il vous plaît")

    def __record(self, ask):
        if ask != "":
            self.speak(ask)
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            voice_text = ""
            try:
                voice_text = self.recognizer.recognize_google(
                    audio, language=self.language)
            except sr.UnknownValueError:
                self.speak("Désolé, je n'ai pas compris")
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

        tts = gTTS(text=text, lang=self.language)

        r = random.randint(1, 1000000)
        audio_file = f"audio-{r}.mp3"
        tts.save(audio_file)
        pg.mixer.music.load(audio_file)
        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            time.sleep(0.1)
        os.remove(audio_file)

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

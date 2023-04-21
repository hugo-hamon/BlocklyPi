from __future__ import annotations
from .event_handler import FrancasterEvent
from typing import TYPE_CHECKING
import logging
import random
import time
import os
import speech_recognition as sr
from unidecode import unidecode
from gtts import gTTS
import pygame as pg
if TYPE_CHECKING:
    from ..controller.francaster_controller import FrancasterController


class FrancasterSpeech:

    def __init__(self, francaster_controller: FrancasterController, language="fr") -> None:
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.language = language
        self.event_handler = FrancasterEvent(self, francaster_controller)

    def record(self, ask="") -> str:
        """Record audio from the microphone and return the recognized text"""
        try:
            with self.microphone as source:
                return self.__record(source, ask)
        except Exception:
            self.speak("Désolé, une erreur est survenue")
            return self.record(ask)

    def __record(self, source, ask):
        self.recognizer.adjust_for_ambient_noise(source)
        if ask != "":
            self.speak(ask)
        audio = self.recognizer.listen(source)
        voice_data = self.recognizer.recognize_google(
            audio, language=self.language)
        if type(voice_data) != str:
            self.speak("Désolé, je n'ai pas compris")
            return self.record("Veuillez répéter s'il vous plaît")
        voice_data = voice_data.lower()
        voice_data = unidecode(voice_data)
        return voice_data

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

    def repeat(self) -> None:
        """Record audio from the microphone and repeat it"""
        self.speak(self.record("Recording..."))

    def answer(self, question: str) -> None:
        """Answer to the given question"""
        self.event_handler.process_question(question)

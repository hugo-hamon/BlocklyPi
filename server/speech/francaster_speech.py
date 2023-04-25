from __future__ import annotations
from .event_handler import FrancasterEvent
import speech_recognition as sr
from unidecode import unidecode
from gtts import gTTS
import pygame as pg
import whisper
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
        self.model = whisper.load_model("base")

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
            audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        result = self.model.transcribe("microphone-results.wav", language="fr")
        # os.remove("microphone-results.wav")
        return unidecode(result["text"])

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
        self.speak(self.record("A vous de parler"))

    def answer(self, question: str) -> None:
        """Answer to the given question"""
        self.event_handler.process_question(question)

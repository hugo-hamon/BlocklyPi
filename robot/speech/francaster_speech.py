from .event_handler import event_handler
import speech_recognition as sr
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

    def record(self, ask="") -> str:
        """Record audio from the microphone and return the recognized text"""
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source)
                if ask != "":
                    self.speak(ask)
                audio = self.recognizer.listen(
                    source, timeout=10, phrase_time_limit=10)
                voice_data = ""
                voice_data = self.recognizer.recognize_google(
                    audio, language=self.language)
                if type(voice_data) != str:
                    print(voice_data)
                    self.speak("Désolé, je n'ai pas compris")
                    return ""
                return voice_data
        except Exception as e:
            self.speak("Désolé, une erreur est survenue")
            return ""

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
        event_handler(self, question)

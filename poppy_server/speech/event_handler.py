from __future__ import annotations
from typing import Dict, TYPE_CHECKING, List
from unidecode import unidecode
import webbrowser
import requests
import random
import string
import json
import time
import sys
import os
if TYPE_CHECKING:
    from .francaster_speech import FrancasterSpeech

FRENCH_DAYS = {
    "Sunday": "Dimanche",
    "Monday": "Lundi",
    "Tuesday": "Mardi",
    "Wednesday": "Mercredi",
    "Thursday": "Jeudi",
    "Friday": "Vendredi",
    "Saturday": "Samedi"
}

WHEATHER_API = "8ef61edcf1c576d65d836254e11ea420"
WHEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?"


class FrancasterEvent:

    def __init__(self, francaster: FrancasterSpeech) -> None:
        self.francaster = francaster
        self.jokes = self.load_jokes()
        self.quotes = self.load_quotes()
        self.question_answer = self.load_question_answer()

        self.questions = list(self.question_answer.keys())
        self.word_frequency = self.load_word_frequency()

    def load_question_answer(self) -> Dict[str, str]:
        """Load the question answer"""
        with open("speech/json/normalized_questions.json", "r") as file:
            return json.load(file)

    def load_jokes(self) -> Dict[str, str]:
        """Load the jokes"""
        with open("speech/json/jokes.json", "r") as file:
            return json.load(file)

    def load_quotes(self) -> List[str]:
        """Load the quotes"""
        with open("speech/json/quotes.json", "r") as file:
            return json.load(file)

    def load_word_frequency(self) -> Dict[str, int]:
        """Load the word frequency"""
        # get all individual words from the questions
        words = {}
        for question in self.questions:
            splits = question.split(" ")
            for split in splits:
                if split not in words:
                    words[split] = 0
                words[split] += 1
        # inverse the frequency
        for word in words:
            words[word] = 1 / words[word]
        # normalize the frequency between 0 and 1
        max_frequency = max(words.values())
        for value in words.values():
            value /= max_frequency
        return words

    def process_question(self, question: str) -> None:
        """Process the given question"""
        # Check if the question is empty
        if not question:
            self.francaster.speak("Désolé je n'ai pas compris votre demande")
            return
        question = self.normalize_text(question)
        print(question)
        # Process the question
        if "quelle heure" in question:
            self.process_time()
        elif "quel jour" in question:
            self.process_day()
        elif "recherche" in question:
            self.process_search()
        elif "adresse" in question:
            self.process_address()
        elif "ouvre youtube" in question:
            self.process_youtube()
        elif "ouvre google" in question:
            self.process_google()
        elif "ouvre gmail" in question:
            self.process_gmail()
        elif "meteo" in question:
            self.process_weather()
        elif "stop" in question:
            self.process_stop()
        elif "blague" in question:
            self.process_joke()
        elif "calcule" in question:
            self.process_calcul()
        elif "citation" in question:
            self.process_quote()
        else:
            self.process_question_answer(question)

    def process_time(self) -> None:
        """Process the time"""
        self.francaster.speak(f"Il est actuellement {time.strftime('%H:%M')}")

    def process_day(self) -> None:
        """Process the day"""
        today = time.strftime("%A")
        if today not in FRENCH_DAYS:
            self.francaster.speak("Je ne sais pas quel jour nous sommes")
            return
        self.francaster.speak(f"Aujourd'hui nous sommes {FRENCH_DAYS[today]}")

    def process_search(self) -> None:
        """Process the search"""
        self.francaster.speak("Qu'est-ce que je dois rechercher ?")
        search = self.francaster.record("Je suis à l'écoute")
        url = f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        self.francaster.speak(f"Voici ce que j'ai trouvé pour {search}")

    def process_address(self) -> None:
        """Process the address"""
        self.francaster.speak("Quelle adresse dois-je rechercher ?")
        address = self.francaster.record("Je suis à l'écoute")
        url = f"https://google.nl/maps/place/{address}"
        webbrowser.get().open(url)
        self.francaster.speak(f"Voici l'adresse de {address}")

    def webbrowser_event(self, url: str, message: str) -> None:
        """Open the given url and speak the given message"""
        webbrowser.open_new_tab(url)
        self.francaster.speak(message)
        time.sleep(5)

    def process_youtube(self) -> None:
        """Process the youtube"""
        self.webbrowser_event("https://www.youtube.com",
                              "Je vous ouvre Youtube")

    def process_google(self) -> None:
        """Process the google"""
        self.webbrowser_event("https://www.google.com", "Je vous ouvre Google")

    def process_gmail(self) -> None:
        """Process the gmail"""
        self.webbrowser_event("https://www.gmail.com", "Je vous ouvre Gmail")

    def process_weather(self) -> None:
        """Process the weather"""
        try:
            self.francaster.speak("De quelle ville voulez-vous la météo ?")
            city = self.francaster.record("Je suis à l'écoute")
            complete_url = f"{WHEATHER_URL}appid={WHEATHER_API}&q={city}"
            response = requests.get(complete_url)
            data = response.json()
            if data["cod"] != "404":
                self.weather_speak(data)
            else:
                self.francaster.speak(
                    "Je n'ai pas pu trouver la météo de cette ville")
        except Exception as exception:
            self.francaster.speak("Désolé je n'ai pas pu trouver la météo")

    def weather_speak(self, data: Dict) -> None:
        """Speak the weather"""
        y = data["main"]
        current_humidity = y["humidity"]
        current_temperature = y["temp"] - 273.15
        text = f"La température est de {round(current_temperature, 3)} degrés" \
            f" avec une humidité de {current_humidity} pourcent"
        self.francaster.speak(text)

    def process_stop(self) -> None:
        """Process the stop"""
        self.francaster.speak("Au revoir et à bientôt")
        sys.exit()

    def process_joke(self) -> None:
        """Process the joke event"""
        joke = random.choice(list(self.jokes.items()))
        self.francaster.speak(joke[0])
        time.sleep(2)
        self.francaster.speak(joke[1])
        self.francaster.speak("C'était drôle non ?")

    def process_quote(self) -> None:
        """Process the quote event"""
        quote = random.choice(self.quotes)
        self.francaster.speak(quote)

    def process_calcul(self) -> None:
        """Process the calcul event"""
        self.francaster.speak("Quel calcul dois-je effectuer ?")
        calcul = self.francaster.record("Je suis à l'écoute")
        try:
            result = eval(calcul)
            self.francaster.speak(f"Le résultat est {result}")
        except Exception:
            self.francaster.speak("Je n'ai pas compris votre demande")

    # Question answer part
    def find_most_similar_question(self, input_question: str):
        similarities = [self.percentage_similarity(input_question, question)
                        for question in self.questions]
        max_similarity_index = similarities.index(max(similarities))
        max_similarity_value = max(similarities)
        return self.questions[max_similarity_index], max_similarity_value

    def percentage_similarity(self, text1: str, text2: str) -> float:
        """Return the percentage of similarity between two texts"""
        match_words = [word for word in text1.split() if word in text2.split()]
        similarity = sum(self.word_frequency[word] for word in match_words)
        # normalize the similarity
        return similarity / (abs(len(text1.split()) - len(text2.split())) + 1)

    def normalize_text(self, text: str) -> str:
        text = text.lower()
        text = unidecode(text)
        text = text.translate(str.maketrans(
            string.punctuation, ' ' * len(string.punctuation)))
        text = ' '.join(text.split())
        return text

    def process_question_answer(self, question: str) -> None:
        """Process the question answer event"""
        normalize_question = self.normalize_text(question)
        most_similar_question, _ = self.find_most_similar_question(
            normalize_question)
        answers = self.question_answer[most_similar_question]

        path = f"speech/sound/{most_similar_question}.mp3"
        if os.path.exists(path):
            self.francaster.speak_from_file(path)
        else:
            self.francaster.speak(answers)

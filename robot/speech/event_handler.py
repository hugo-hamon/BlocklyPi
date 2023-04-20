from __future__ import annotations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, TYPE_CHECKING, List
import webbrowser
import requests
import random
import json
from unidecode import unidecode
import string
import nltk
import time
import sys
if TYPE_CHECKING:
    from .francaster_speech import FrancasterSpeech
    from ..controller.francaster_controller import FrancasterController

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

    def __init__(self, francaster: FrancasterSpeech, controller: FrancasterController) -> None:
        self.francaster = francaster
        self.controller = controller
        self.jokes = self.load_jokes()
        self.quotes = self.load_quotes()
        self.question_answer = self.load_question_answer()

        self.stemmer = nltk.stem.PorterStemmer()
        self.questions = list(self.question_answer.keys())
        self.vect = TfidfVectorizer(min_df=1, tokenizer=self.normalize)
        self.tfidf_matrix = self.vect.fit_transform(self.questions)
        self.remove_punctuation_map = {
            ord(char): None for char in string.punctuation}

    def stem_tokens(self, tokens):
        """Stem the given tokens"""
        return [self.stemmer.stem(item) for item in tokens]

    def normalize(self, text: str):
        """Normalize the given text"""
        return self.stem_tokens(nltk.word_tokenize(text.lower().translate(self.remove_punctuation_map)))

    def load_question_answer(self) -> Dict[str, str]:
        """Load the question answer"""
        with open("robot/speech/json/normalized_question.json", "r") as file:
            return json.load(file)

    def load_jokes(self) -> Dict[str, str]:
        """Load the jokes"""
        with open("robot/speech/json/jokes.json", "r") as file:
            return json.load(file)

    def load_quotes(self) -> List[str]:
        """Load the quotes"""
        with open("robot/speech/json/quotes.json", "r") as file:
            return json.load(file)

    def process_question(self, question: str) -> None:
        """Process the given question"""
        # Check if the question is empty
        if not question:
            self.francaster.speak("Je n'ai pas compris votre demande")
            return

        # Process the question
        if "quel heure" in question:
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

    def weather_speak(self, data: Dict) -> None:
        """Speak the weather"""
        y = data["main"]
        current_humidity = y["humidity"]
        z = data["weather"]
        weather_description = z[0]["description"]
        current_temperature = y["temp"] - 273.15
        text = f"La température est de {current_temperature} degrés" \
            f" avec une humidité de {current_humidity} pourcent" \
            f" et {weather_description}"
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
        input_tfidf = self.vect.transform([input_question])
        similarities = cosine_similarity(input_tfidf, self.tfidf_matrix)
        print(similarities)
        max_similarity_index = similarities.argmax()
        max_similarity_value = similarities.max()
        return self.questions[max_similarity_index], max_similarity_value

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
        most_similar_question, similarity = self.find_most_similar_question(
            normalize_question)
        if similarity > 0.5:
            answers = self.question_answer[most_similar_question]
            self.francaster.speak(answers)
        else:
            self.francaster.speak("Je n'ai pas compris votre demande")

from __future__ import annotations
from typing import Dict, TYPE_CHECKING
import webbrowser
import requests
import logging
import time
import sys
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


def event_handler(francaster: FrancasterSpeech, question: str) -> None:
    if not question:
        francaster.speak("Je n'ai pas compris votre demande")
        return
    question = question.lower()
    if "comment tu t'appelle" in question:
        francaster.speak("Je m'appelle Francaster")
    elif "quel heure" in question:
        francaster.speak(f"Il est actuellement {time.strftime('%H:%M')}")
    elif "quel jour" in question:
        today = time.strftime("%A")
        if today not in FRENCH_DAYS:
            francaster.speak("Je ne sais pas")
            return
        francaster.speak(f"Aujourd'hui nous sommes {FRENCH_DAYS[today]}")
    elif "recherche" in question:
        francaster.speak("Qu'est-ce que je dois rechercher ?")
        search = francaster.record("Je suis à l'écoute")
        url = f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        francaster.speak(f"Voici ce que j'ai trouvé pour {search}")
    elif "trouve une adresse" in question:
        location = francaster.record("Ou est-ce que je dois chercher ?")
        url = f"https://google.nl/maps/place/{location}"
        webbrowser.get().open(url)
        francaster.speak(f"Voici l'adresse de {location}")
    elif "ouvre youtube" in question:
        webbrowser_event(
            francaster, "https://youtube.com", "Ouverture de Youtube"
        )
    elif "ouvre google" in question:
        webbrowser_event(
            francaster, "https://google.com", "Ouverture de Google"
        )
    elif "ouvre gmail" in question:
        webbrowser_event(
            francaster, "https://gmail.com", "Ouverture de Gmail"
        )
    elif "météo" in question:
        weather_event(francaster)
    elif "frabiquer par qui" in question or "qui t'as créer" in question:
        francaster.speak("Je suis un robot créé par francas")
    elif "qu'est-ce que tu sais faire" in question:
        francaster.speak(
            "Mon nom est francaster," +
            " je peux vous dire l'heure, le jour," +
            " je peux ouvrir google, youtube, gmail," +
            " je peux vous donner la météo," +
            " je peux vous faire une recherche sur google," +
            " je peux vous trouver une adresse," +
            "et encore plein d'autres choses."
        )
    elif "stop" in question or "arrête" in question:
        francaster.speak("Au revoir et à bientot")
        sys.exit(0)
    else:
        print(f"Question: {question}")
        francaster.speak("Désolé, je n'ai pas compris votre demande")


def webbrowser_event(francaster: FrancasterSpeech, url: str, message: str) -> None:
    """Open the given url and speak the given message"""
    webbrowser.open_new_tab(url)
    francaster.speak(message)
    time.sleep(5)


def weather_event(francaster: FrancasterSpeech) -> None:
    """Get the weather of the current location"""
    francaster.speak("De quelle ville voulez-vous la météo ?")
    city = francaster.record("Je suis à l'écoute")
    complete_url = f"{WHEATHER_URL}appid={WHEATHER_API}&q={city}"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        weather_speak(francaster, data)
    else:
        francaster.speak("Je n'ai pas pu trouver la météo de cette ville")



def weather_speak(francaster: FrancasterSpeech, data: Dict) -> None:
    y = data["main"]
    current_humidity = y["humidity"]
    z = data["weather"]
    weather_description = z[0]["description"]
    current_temperature = y["temp"] - 273.15
    text = f"La température est de {current_temperature} degrés" \
        f" avec une humidité de {current_humidity} pourcent" \
        f" et {weather_description}"
    francaster.speak(text)
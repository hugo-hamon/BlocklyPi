from typing import Dict
from gtts import gTTS
from tqdm import tqdm
import json
import os


def load_question_answer() -> Dict[str, str]:
    """Load the question answer"""
    with open("json/normalized_questions.json", "r") as file:
        return json.load(file)


def generate_sound(name: str, text: str) -> None:
    """Generate sound file from text"""
    try:
        audio_file = f"sound/{name}.mp3"
        if os.path.exists(audio_file):
            return
        tts = gTTS(text=text, lang="fr")
        tts.save(audio_file)
    except Exception:
        print(f"Erreur pour la question {name}")


if __name__ == "__main__":
    questions = load_question_answer()
    for key, value in tqdm(questions.items()):
        generate_sound(key, value)

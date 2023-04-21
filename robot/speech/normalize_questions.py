from unidecode import unidecode
import string
import json


def normalize_text(text):
    text = text.lower()
    text = unidecode(text)
    text = text.translate(str.maketrans(
        string.punctuation, ' ' * len(string.punctuation)))
    text = ' '.join(text.split())
    return text


with open('json/questions.json', 'r', encoding='utf-8') as jsonfile:
    questions_answers = json.load(jsonfile)
    normalized_questions_answers = {normalize_text(
        q): a for q, a in questions_answers.items()}

with open('json/normalized_questions.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(normalized_questions_answers,
              jsonfile, ensure_ascii=False, indent=4)

print("Fin de l'execution du script.")

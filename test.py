from pygame import mixer
from io import BytesIO
from gtts import gTTS
import time

def speak():
    mp3_fp = BytesIO()
    tts = gTTS("Je n'ai pas de style de musique préféré, car j'apprécie différents genres en fonction de l'humeur et de la situation.", lang='en')
    a = time.time()
    tts.write_to_fp(mp3_fp)
    print(f"time: {time.time() - a}")
    return mp3_fp

mixer.init()
sound = speak()
sound.seek(0)
mixer.music.load(sound, "mp3")
mixer.music.play()
time.sleep(5)
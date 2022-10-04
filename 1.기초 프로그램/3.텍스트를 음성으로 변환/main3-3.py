from gtts import gTTS
from playsound import playsound
import os

#경로를 .py파일의 실행결로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'my_text.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')

tts.save("my_text.mp3")

playsound("my_text.mp3")
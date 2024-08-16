from gtts import gTTS
from playsound import playsound

som = gTTS(text='Eu gosto de python', lang = 'pt', slow = False)
som.save('fala.mp3')

playsound('fala.mp3'),

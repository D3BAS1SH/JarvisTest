from gtts import gTTS
from playsound import playsound

myText='Say my name'
text = "यह हिंदी में पाठ है।"  # Hindi text
language = 'hi'


# language='en'

myTextSpeech=gTTS(text=text,lang=language,slow=False)

myTextSpeech.save('./TestHindiSpeech.mp3')

playsound('TestHindiSpeech.mp3')
print('playing sound using  playsound')
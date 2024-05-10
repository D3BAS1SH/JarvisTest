import speech_recognition as SR
import pyaudio
from google.cloud import speech
from google.oauth2 import service_account

client=speech.SpeechClient.from_service_account_json('./Key.json')
credential=service_account.Credentials.from_service_account_file('./Key.json')

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']}")

Rec=SR.Recognizer()
# print(Rec)
try:
    with SR.Microphone(device_index=2) as source:
        print("Say something!")
        audio = Rec.listen(source)
        print(audio.sample_rate)
        print(audio.frame_data)
        print(audio.sample_width)
    
    response=Rec.recognize_google_cloud(audio_data=audio,credentials_json='./Key.json')
    print(response)
except Exception as e:
    print(f"ERROR : {e}")
from google.cloud import speech

client = speech.SpeechClient.from_service_account_json('./Key.json')

with open('./untitled.wav','rb') as F:
    content=F.read()
    audioFile=speech.RecognitionAudio(content=content)

config=speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US'
)

response=client.recognize(audio=audioFile,config=config)

print(response)
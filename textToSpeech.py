""" from google.cloud import speech

client = speech.SpeechClient.from_service_account_json('./Key.json')

filename='./Test.mp3'

with open(filename,'rb') as F:
    mp3Data=F.read()

audioFile=speech.RecognitionAudio(content=mp3Data)

config = speech.RecognitionConfig(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US'
)

response = client.recognize(
    config=config,
    audio=audioFile
)

print(response) """


# Imports the Google Cloud client library


from google.cloud import speech



def run_quickstart() -> speech.RecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient.from_service_account_json('./Key.json')

    # The name of the audio file to transcribe
    gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")
run_quickstart()
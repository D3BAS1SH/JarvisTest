import speech_recognition as SR
import google.cloud.texttospeech as TTS
import pyaudio
import MyFunctionalities as MF

# playsound.playsound('output.mp3')

def getaudio(text):
    synthesis_input = TTS.SynthesisInput(text=text)
    voice=TTS.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=TTS.SsmlVoiceGender.MALE
    )
    audio_config = TTS.AudioConfig(audio_encoding=TTS.AudioEncoding.LINEAR16)
    responseGen = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    return responseGen

def playMySpeech(x):
    # Open an audio stream
        stream = pyaudio.PyAudio().open(
            format=pyaudio.paInt16,  # Sample format (can vary depending on file)
            channels=1,  # Number of channels (mono or stereo)
            rate=20000,  # Sampling rate (in Hz)
            output=True,  # Set output stream
            frames_per_buffer=512*8,  # Buffer size (in frames)
        )
        # Play the audio data
        stream.write(getaudio(x).audio_content)
        # Stop the stream and close it
        stream.stop_stream()
        stream.close()

        # Close PyAudio
        pyaudio.PyAudio().terminate()

MY_DEVICE_INDEX=1
Rec=SR.Recognizer()
client=TTS.TextToSpeechClient.from_service_account_json('./Key.json')

playMySpeech(MF.Greet("Debasish"))

while(True):
    try:
        
        with SR.Microphone(device_index=MY_DEVICE_INDEX) as source:
            print("Any command!?")
            audioData=Rec.listen(source,phrase_time_limit=3)
        response=Rec.recognize_google_cloud(audio_data=audioData,credentials_json='./Key.json')
        print(f"You have told me to : {response}")
        
        if('open notepad' in response.lower()):
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenApps('notepad')
        elif 'open discord' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenApps('discord')
        elif 'open calculator' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenApps('calculator')
        elif 'open code' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenApps('code')
        elif 'open steam' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenApps('steam')
        elif 'open camera' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenApps('camera')
        elif 'open this pc' in response.lower() or 'open computer' in response.lower() or 'open my computer' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenDir('Computer')
        elif 'open c drive' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenDir('c drive')
        elif 'open d drive' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.OpenDir('d drive')
        elif 'get ip' in response.lower() or 'get my ip' in response.lower():
            playMySpeech(MF.getRandomReplyRes())
            MF.getIP()
        elif('quit' in response or 'stop' in response):
            playMySpeech("See you around Debasish")
            break
        else:
            playMySpeech("Sorry the request you have asked is beyond my limit")
        
    except Exception as E:
        print(f"ERROR : {E}")
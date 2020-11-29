import io
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums, types

client = speech_v1.SpeechClient()
audio_file = io.open("output.mp3",'rb')
content = audio_file.read()

audio =types.RecognitionAudio(content=content)

config=types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en_US'
)

response = client.recognize(config, audio)
print(response)
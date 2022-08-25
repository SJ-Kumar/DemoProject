import SpeechRecognition as sr
r=sr.Recongnizer()
with sr.Microphone() as source:
    print ("Speak:")
audio=r.listen(source)
print(r.recognize_google(audio))

print(r.recognize_google(audio, language = "en-EN")) 
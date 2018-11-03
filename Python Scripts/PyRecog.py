import speech_recognition as sr
import PySelectF as FileSelect

r = sr.Recognizer()
file_path = FileSelect.selectFile()
swara = sr.AudioFile(file_path.name)
with swara as source:
    audio = r.record(source,duration=15)
text = r.recognize_google(audio)
print(text)
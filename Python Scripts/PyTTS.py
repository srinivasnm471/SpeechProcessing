#==============================================================================
#Project Modules
#==============================================================================
from gtts import gTTS
#Requires urllib3 --> pip install urllib3
#==============================================================================

def textToSpeech(text,fileName):
    tts = gTTS(text)
    tts.save(fileName)
    
textToSpeech('ondu','train.mp3')
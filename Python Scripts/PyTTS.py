#==============================================================================
import PySelectF as Folder
#==============================================================================
import playsound
from gtts import gTTS
#Requires a stable Network Connection
#==============================================================================

def textToSpeech(text,fileName='SavedFile',dest_path=''):
    tts = gTTS(text,lang='hi')
    file = dest_path+fileName+'.mp3'
    tts.save(file)
    playsound.playsound(file)
    
text = 'kaa'
dest_path = Folder.selectFolder()
textToSpeech(text,text,dest_path+'/')

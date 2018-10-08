"""
Created on Mon Oct  8 11:15:56 2018
@author: Shashank B Sharma
"""

import numpy as np
import wave as wave
import system as sys


"""
Documentation:
    file_path -> str
    file_type -> .wav
    Audio_type -> Mono
    file_open_type -> Read
    
    return -> signal
    return_type -> list
    
    Exits if file doesnt Exist/ Not readable
"""
#readFile Function
def readFile(file_path):
    try:
        spf = wave.open(file_path,'r')
        signal = spf.readframes(-1)
        spf.close()
        signal = list(np.fromstring(signal, 'int'))

        if spf.getnchannels() == 2:
            print('Cannot Plot Stereo Files')
        
        return signal
    
    except Exception as err:
        print(err)
        sys.exit(0)



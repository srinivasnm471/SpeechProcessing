import numpy as np
import wave as wave
import system as sys

#readFile Function
def readFile(file_path):
    try:
        spf = wave.open(file_path,'r')
        signal = spf.readframes(-1)
        spf.close()
        signal = list(np.fromstring(signal, 'int'))

        if spf.getnchannels() == 2:
            print('Only Mono Files Allowed')
        
        return signal
    
    except Exception as err:
        print(err)
        sys.exit(0)



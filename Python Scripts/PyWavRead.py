#==============================================================================
#Project Modules
#==============================================================================
import numpy as np
import wave as wave
import sys
#==============================================================================
#readFile Function
def readWAVFile(file_path):
    try:
        spf = wave.open(file_path,'r')
        signal = spf.readframes(-1)
        spf.close()
        signal = list(np.fromstring(signal, 'int'))

        if spf.getnchannels() == 2:
            print('Only Mono Files Allowed')
        spf.close()
        return signal
    
    except Exception as err:
        print(err)
        sys.exit(0)



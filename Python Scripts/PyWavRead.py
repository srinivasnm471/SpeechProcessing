#==============================================================================
#Project Modules
#==============================================================================
import scipy.io.wavfile as wave
import sys
#==============================================================================
#readFile Function
def readWAVFile(file_path):
    try:
        fs,signal = wave.read(file_path)
        return fs,signal
    except Exception as err:
        print(err)
        sys.exit(0)



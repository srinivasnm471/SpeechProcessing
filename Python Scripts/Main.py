#==============================================================================
import PyPlot as Plot
import PyWavRead as WavRead
import PySelectF as FileSelect
#==============================================================================
from python_speech_features import mfcc
#==============================================================================

#__init__

file_path = FileSelect.selectFile()
fs,signal = WavRead.readWAVFile(file_path.name)
mfcc_feat = mfcc(signal,fs,nfft=1103)
Plot.plotSpectrogram(signal,fs)
Plot.plotY(signal/max(signal))
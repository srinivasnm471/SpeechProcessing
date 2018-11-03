#==============================================================================
import PyPlot as Plot
import PyWavRead as WavRead
import PySelectF as FileSelect
#==============================================================================
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
#==============================================================================

#__init__

file_path = FileSelect.selectFile()
fs,signal = WavRead.readWAVFile(file_path.name)
mfcc_feat = mfcc(signal,fs,nfft=2048)

Plot.plotSpectrogram(signal,fs)
Plot.plotY(signal/max(signal))

d_mfcc_feat = delta(mfcc_feat, 2)
d_mfcc_feat_2=delta(d_mfcc_feat,2)

Plot.plotY(mfcc_feat)
Plot.plotY(d_mfcc_feat)
Plot.plotY(d_mfcc_feat_2)

fbank_feat = logfbank(signal,fs,nfft=2048)

print(fbank_feat[1:3,:])
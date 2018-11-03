#==============================================================================
import PyPlot as Plot
import PyWavRead as WavRead
import PySelectF as FileSelect
import matplotlib.pyplot as plt
#==============================================================================
from python_speech_features import mfcc
from python_speech_features import delta
from python_speech_features import logfbank
#==============================================================================

#__init__

file_path = FileSelect.selectFile()
fs,signal = WavRead.readWAVFile(file_path.name)
<<<<<<< HEAD
mfcc_feat = mfcc(signal,fs,nfft=1103)
=======
mfcc_feat = mfcc(signal,fs,nfft=2048)
>>>>>>> cf008897c8faf2e1858e0714935b44b255da6cab

Plot.plotSpectrogram(signal,fs)
Plot.plotY(signal/max(signal))

d_mfcc_feat = delta(mfcc_feat, 2)
d_mfcc_feat_2=delta(d_mfcc_feat,2)

<<<<<<< HEAD
plt.plot(mfcc_feat)
plt.show()
plt.plot(d_mfcc_feat)
plt.show()
plt.plot(d_mfcc_feat_2)
plt.show()
fbank_feat = logfbank(signal,fs)

print(fbank_feat[1:3,:])
=======
Plot.plotY(mfcc_feat)
Plot.plotY(d_mfcc_feat)
Plot.plotY(d_mfcc_feat_2)

fbank_feat = logfbank(signal,fs,nfft=2048)

print(fbank_feat[1:3,:])
>>>>>>> cf008897c8faf2e1858e0714935b44b255da6cab

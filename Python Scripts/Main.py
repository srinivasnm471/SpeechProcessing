#==============================================================================
import PyPlot as Plot
import PyWavRead as WavRead
import PySelectF as FileSelect
#==============================================================================
import numpy as np
#import scipy as sp
from sklearn import preprocessing as skpp
import librosa
#==============================================================================

#__init__

file_path = FileSelect.selectFile()
fs,signal = WavRead.readWAVFile(file_path.name)

#Signal Plot
Plot.plotY(signal/max(signal),title='Wavefrom',subPlot=211)
Plot.plotSpectrogram(signal,fs,subPlot=212)

#Feature Extraction
mfcc = librosa.feature.mfcc(np.float64(signal),np.float64(fs),n_mfcc=20,htk=True)
delta_feat= librosa.feature.delta(mfcc)
delta2_feat = librosa.feature.delta(mfcc,order=2)

#Pitch Tracking not verified yet
pitch_tracking = librosa.core.piptrack(np.float64(signal),float(fs),fmin=50,fmax=500)

#Feature Plotting
Plot.plotFeatures(mfcc,fs,'MFCC',311)
Plot.plotFeatures(delta_feat,fs,'Delta',312)
Plot.plotFeatures(delta2_feat,fs,'DeltaDelta',313)

#Scaling Features to make each dimension with Mean=0 and Variance = 1
mfcc = skpp.scale(mfcc,axis=1)
Plot.plotFeatures(mfcc,fs,'Scaled MFCC')
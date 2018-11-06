#==============================================================================
import PyPlot as Plot
import PyWavRead as WavRead
import PySelectF as FileSelect
#==============================================================================
import numpy as np
import librosa
#==============================================================================

#__init__

file_path = FileSelect.selectFile()
fs,signal = WavRead.readWAVFile(file_path.name)

#Signal Plot
Plot.plotY(signal/max(signal),title='Wavefrom',subPlot=211)
Plot.plotSpectrogram(signal,fs,subPlot=212)

#Feature Extraction
mfcc = librosa.feature.mfcc(np.float64(signal),np.float64(fs),n_mfcc=13,htk=True)
delta_feat= librosa.feature.delta(mfcc)
delta2_feat = librosa.feature.delta(mfcc,order=2)
pitch_tracking = librosa.core.piptrack(np.float64(signal),float(fs),fmin=50,fmax=500)

#Feature Plotting
Plot.plotFeatures(mfcc,'MFCC',311)
Plot.plotFeatures(delta_feat,'Delta',312)
Plot.plotFeatures(delta2_feat,'DeltaDelta',313)


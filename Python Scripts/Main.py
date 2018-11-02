"""
Created on Mon Oct  8 19:21:11 2018
@author: Shashank B Sharma
"""
#Project Files
import ReadWavFile as read
import plotSignal as plot
import SpectralAnalysis as spectrum

file_path = 'F:\\SpeechProcessing\\Modified Speech\\a.wav'
signal,fft = read.readFile(file_path)

#Plot Signal
plot.signalPlot(signal)

#Find Spectrum
fft_cmplx = spectrum.fft(signal)
fft_mag = spectrum.fftMagnitude(fft_cmplx)

#==============================================================================
#Project Modules
#==============================================================================
import matplotlib.pyplot as pyplot
import scipy.signal as sg
import librosa.display as disp
#==============================================================================

def plotY(signal,stem:bool = False,title:str='',xLabel:str='',yLabel:str='',subPlot:int=None):
    if subPlot==None:
        pyplot.figure()
    else:
        if str(subPlot)[-1]=='1':
            pyplot.figure()
        pyplot.subplot(subPlot)
        
    pyplot.title(title)
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.tight_layout()
    if not stem:
        plotted = pyplot.plot(signal)
    else:
        plotted = pyplot.stem(signal)
    
    pyplot.grid()
    pyplot.show()
    return plotted
    
         
def plotXY(x=[],y=[],stem:bool = False,title:str='',xLabel:str='',yLabel:str='',subPlot:int=None):
    if subPlot==None:
        pyplot.figure()
    else:
        if str(subPlot)[-1]=='1':
            pyplot.figure()
        pyplot.subplot(subPlot)
        
    pyplot.title(title)
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.xlim([x[0],x[-1]])
    pyplot.tight_layout()
    if not stem:
        plotted = pyplot.plot(x,y)
    else:
        plotted = pyplot.stem(x,y)
        
    pyplot.show()
    return plotted
        
def plotSpectrum(y,frequency,log=False,title:str='',xLabel:str='',yLabel:str='',subPlot:int=None):
    if subPlot==None:
        pyplot.figure()
    else:
        if str(subPlot)[-1]=='1':
            pyplot.figure()
        pyplot.subplot(subPlot)
        pyplot.tight_layout()
    
    pyplot.title(title)
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    
    
    if not log:
        plotted = pyplot.plot(frequency,y)
    else:
        plotted = pyplot.semilogx(frequency,y)
    
    pyplot.grid(which='both')
    pyplot.show()
    return plotted

        
def plotSpectrogram(signal,fs,ret:bool=False,subPlot:int=None):
    
    #Calculate Spectrogram Parameters
    #Default Window set to Hamming with length 2048
    #No of Spectrogram Points = 2000
    frequencies, times, spectrogram = sg.spectrogram(signal,fs,window=sg.get_window('hamming',2048),nperseg=2048,noverlap=2000)
    
    if subPlot==None:
        pyplot.figure()
    else:
        if str(subPlot)[-1]=='1':
            pyplot.figure()
        pyplot.subplot(subPlot)
        pyplot.tight_layout()
    
    pyplot.pcolormesh(times, frequencies, spectrogram,cmap='gist_earth')
    pyplot.title('Spectrogram')
    pyplot.ylim([0,5000])
    pyplot.ylabel('Frequency [Hz]')
    pyplot.xlabel('Time [sec]')
    pyplot.show()
    
    if ret:
        return frequencies,times,spectrogram
    
def plotFeatures(feature,fs=22050,title:str='',subPlot:int=None,):
    if subPlot==None:
        pyplot.figure()
    else:
        if str(subPlot)[-1]=='1':
            pyplot.figure()
        pyplot.subplot(subPlot)
    
    disp.specshow(feature,sr=float(fs),x_axis='time')
    pyplot.colorbar()
    pyplot.title(title)
    pyplot.tight_layout()
    pyplot.show()
    
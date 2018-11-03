#==============================================================================
#Project Modules
#==============================================================================
import matplotlib.pyplot as pyplot
import scipy.signal as sg
#==============================================================================

def plotY(signal,stem = False,title='',xLabel='',yLabel=''):
    try:
        signal = list(signal)
        pyplot.figure()
        pyplot.title(title)
        pyplot.xlabel(xLabel)
        pyplot.ylabel(yLabel)
        
        if not stem:
            plotted = pyplot.plot(signal)
        else:
            plotted = pyplot.stem(signal)
        
        pyplot.ylim([min(signal),max(signal)])
        pyplot.grid()
        pyplot.show()
        return plotted
    except:
        print('Error in Plot Signal')
        print('The function takes only List Arguements')
         
def plotXY(x=[],y=[],stem = False,title='',xLabel='',yLabel=''):
    try:
        pyplot.figure()
        pyplot.title(title)
        pyplot.xlabel(xLabel)
        pyplot.ylabel(yLabel)
        pyplot.xlim([x[0],x[-1]])
        
        if not stem:
            plotted = pyplot.plot(x,y)
        else:
            plotted = pyplot.stem(x,y)
            
        pyplot.show()
        return plotted
    
    except:
        print('Error in Plotting Signal')
        print('The size of lists must be same')
        
def plotSpectrum(y,frequency,log=False,title='',xLabel='',yLabel=''):
    try:
        pyplot.figure()
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
    
    except:
        print('Error in Plotting Signal')
        print('The size of lists must be same')
        
def plotSpectrogram(signal,fs):
    frequencies, times, spectrogram = sg.spectrogram(signal,fs)
    
    pyplot.pcolormesh(times, frequencies, spectrogram)
    pyplot.imshow(spectrogram)
    pyplot.ylabel('Frequency [Hz]')
    pyplot.xlabel('Time [sec]')
    pyplot.show()
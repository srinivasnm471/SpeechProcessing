#==============================================================================
import PySelectF as FSelect
import PyPlot as plot
#==============================================================================
#Python Built-In Packages
#==============================================================================
def spectrumDataFromAudacity(file_path,toplot=False):
    file = open(file_path,'r')
    frequency = list()
    level = list()
    
    #Define Dictionary of Frequency and Level
    keys = file.readline().split()
    keys[0]+=keys[1]
    keys[2]+=keys[3]
    del keys[3]
    del keys[1]
    
    for x in file:
        arr =  x.split('-')
        frequency.append(float(arr[0].strip()))
        level.append(-float(arr[1].strip()))
    file.close()    
    
    data = dict()
    data[keys[0]] = frequency
    data[keys[1]] = level
    
    if toplot:
        plot.plotSpectrum(level,frequency,True,'Spectrum','Frequency(log)','level(dB)')
    
    return data

#__init__
file_path = FSelect.selectFile()
data = spectrumDataFromAudacity(file_path.name,True)

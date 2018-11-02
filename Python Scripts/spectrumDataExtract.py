import plotSignal as plot

file = open('spectrumaaaa.txt','r')
frequency = list()
level = list()
file.readline()
for x in file:
    arr =  x.split('-')
    frequency.append(float(arr[0].strip()))
    level.append(-float(arr[1].strip()))
plot.plotXY(frequency,level,'Spectrum')
file.close()
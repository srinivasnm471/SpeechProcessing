"""
Created on Mon Oct  8 12:36:29 2018
@author: Shashank B Sharma
"""

import matplotlib.pyplot as plot



def signalPlot(signal):
    try:
        signal = list(signal)
        plot.figure()
        print('Figure Number: '+ str(plot.gcf().number))
        plot.title('Signal Wave...')
        plot.plot(signal)
        plot.show()
    except:
        print('Error in Plot Signal')
        print('The function takes only List Arguements')
 
def signalStem(signal):
    try:
        signal = list(signal)
        plot.figure()
        print('Figure Number: '+ str(plot.gcf().number))
        plot.title('Signal Wave...')
        plot.stem(signal)
        plot.show()
    except:
        print('Error in Plot Signal')
        print('The function takes only List Arguements')       
        
def plotXY(x=[],y=[],title='',xLabel='',yLabel=''):
    try:
        plot.figure()
        
        print(print('Figure Number: '+ str(plot.gcf().number)))
        plot.title(title)
        plot.xlabel(xLabel)
        plot.ylabel(yLabel)
        plot.xlim([x[0],x[-1]])
        
        lines = plot.plot(x,y)
        
        plot.setp(lines,linewidth = 0.75)
        plot.show()
    except:
        print('Error in Plotting Signal')
        print('The size of lists must be same')
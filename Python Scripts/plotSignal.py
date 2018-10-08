"""
Created on Mon Oct  8 12:36:29 2018
@author: Shashank B Sharma
"""

import matplotlib.pyplot as plot
import sys

def signal(signal):
    try:
        plot.figure()
        print('Figure Number: '+ str(plot.gcf().number))
        plot.title('Signal Wave...')
        plot.plot(signal/max(signal))
        plot.show()
    except:
        print('Error in Plot Signal')
        print('The function takes only List Arguements')
        sys.exit(0)
        
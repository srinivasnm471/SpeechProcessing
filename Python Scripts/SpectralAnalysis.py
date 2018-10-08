"""
Created on Mon Oct  8 19:02:10 2018
@author: Shashank B Sharma
"""

import numpy as np
import cmath as cmplx

def fft(signal):
    return list(np.fft.fft(signal))
    
def fftMagnitude(spectrum):
    return [cmplx.polar(x)[0] for x in spectrum]
    
    
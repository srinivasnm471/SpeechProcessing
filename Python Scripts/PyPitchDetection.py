#==============================================================================
#Project Modules
#==============================================================================
import numpy
#==============================================================================
PI = numpy.pi

def __covariance(x, k):
    N = len(x) - k
    return (x[:-k] * x[k:]).sum() / N

#Pisarenko Harmonic Distribution
def __phd(x):
    r1 = __covariance(x, 1)
    r2 = __covariance(x, 2)
    a = (r2 + numpy.sqrt(r2 ** 2 + 8 * r1 ** 2)) / 4 / r1
    if a > 1:
        a = 1
    elif a < -1:
        a = -1
    return numpy.arccos(a)


def pitch(x, sample_step=1, dt=1.0):
    omega = __phd(x[::sample_step])
    return omega / 2.0 / PI / sample_step / dt
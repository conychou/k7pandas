import numpy
from k7 import *

class kDataFrame(object):
    def __init__(
        self,
        data=None,
        index=None,
        columns=None,
        dtype=None,
        copy=False,
        kcopy=None,
    ):
        #should be able to accept different data : numpy ndarray (structured or homogeneous), dict, or DataFrame
        if isinstance(data,numpy.ndarray):
            self.kcopy = k('[]')
	    self.kcopy.x = data
            #numpy.asarray(self.kcopy)[:] = data
        else:
            if isinstance(data, list):
                #self.kcopy = shape(len(data),0.0)
            	self.kcopy = k('[]')
	    else:
                self.kcopy = k('[]')
            tmp = numpy.asarray(data)
            #numpy.asarray(self.kcopy)[:] = tmp
            self.kcopy.x = temp
        return        

    def append(self, other, ignore_index=False, verify_integrity=False, sort=None):
       return k('{},{}'.format(self.kcopy,other.kcopy))

    def mean(self):
        return k('(+/{0})%(#{0})'.format(self.kcopy))

    def rolling_mean(self, numpoints):
	print(self.k)
        return k('movavg[{1};{0}]'.format(self.kcopy.x, numpoints))

    def to_ndarray(self):
        return numpy.asarray(self.kcopy)


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
            self.kcopy = shape(data.size,0.0)
            numpy.asarray(self.kcopy)[:] = data
        else:
            if isinstance(data, list):
                self.kcopy = shape(len(data),0.0)
            else:
                self.kcopy = shape(data.size,0.0)
            tmp = numpy.asarray(data)
            numpy.asarray(self.kcopy)[:] = tmp

        return        

    def append(self, other, ignore_index=False, verify_integrity=False, sort=None):
       return k('{},{}'.format(self.kcopy,other.kcopy))

    def mean(self):
        return k('(+/{0})%(#{0})'.format(self.kcopy))

    def rolling_mean(self, numpoints):
        return k('movavg[{1};{0}]'.format(self.kcopy, numpoints))

    def to_ndarray(self):
        return numpy.asarray(self.kcopy)


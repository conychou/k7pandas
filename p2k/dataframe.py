import numpy
from k7 import *

class DataFrame(object):
    def __init__(
        self,
        data=None,
        index=None,
        columns=None,
        dtype=None,
        copy=False,
        name=None,
    ):
        #should be able to accept different data : numpy ndarray (structured or homogeneous), dict, or DataFrame
        if isinstance(data,numpy.ndarray) | isinstance(data, list):
            self.name = k(' '.join(map(str,data)))
            return        

    def append(self, other, ignore_index=False, verify_integrity=False, sort=None):
       return k('{},{}'.format(self.name,other.name))

    def mean(self):
        return k('(+/{0})%(#{0})'.format(self.name))

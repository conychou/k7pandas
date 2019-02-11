#!/usr/bin/env python

import time
from p2k import DataFrame
import numpy as np

#start = time.time()
x = DataFrame([1,2,3])
print(x.append(x))
print(x.mean())

y = DataFrame(np.random.randint(low=0, high=10, size=5))
print(y.name)
print(y.mean())
#print(time.time()-start)

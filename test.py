#!/usr/bin/env python

import time
import pandas as pd
from p2k import *
import numpy

#start = time.time()
opsd_daily = pd.read_csv('opsd_germany_daily.csv')
#data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']
opsd_7d = opsd_daily['Consumption'].rolling(7, min_periods=1).mean()

k_opsd_7d = kDataFrame(opsd_daily['Consumption'])
print(k_opsd_7d.rolling_mean(7))
#print(opsd_7d == numpy.asarray(k_opsd_7d.rolling_mean(7))) 

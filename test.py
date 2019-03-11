#!/usr/bin/env python

import time
import pandas as pd
from p2k import *
import numpy
import timeit

opsd_daily = pd.read_csv('opsd_germany_daily.csv')
#data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']

## Creating function so it can be timed in timeit 
## Timing pandas rolling mean
def pandas_rolling_mean(): 
	opsd_7d = opsd_daily['Consumption'].rolling(7, min_periods=1).sum()

duration = timeit.timeit(pandas_rolling_mean, number=1000)
print("Time in pandas: " + str(duration/1000))

k_opsd_7d = kDataFrame(opsd_daily['Consumption'])

## Timing k7 rolling mean
def k7_rolling_mean():
	k_opsd_7d.rolling_sum(7)

duration = timeit.timeit(k7_rolling_mean, number=1000)
print("Time in k7: " + str(duration/1000))


## Calculate difference in results
def percent_diff(a, b):
	percent = (b - a) / a
	print("percent difference in calculations:"+str(percent))

#percent_diff(opsd_daily['Consumption'].rolling(7, min_periods=1).mean(), numpy.asarray(k_opsd_7d.rolling_mean(7)))

## Moved your commented lines down
#print(k_opsd_7d.rolling_mean(7))
#print(opsd_7d == numpy.asarray(k_opsd_7d.rolling_mean(7)))

from k7 import k

k('movsum:{[k;myarray] +\/\'myarray[((!((#myarray)-k))+\:!k)]}')
#k('movsum:{[numpoints;myarray] x: +\myarray; xsub: $[numpoints < #myarray;(numpoints # 0),x[!(#x)-numpoints];0]; x - xsub}')
k('movavg:{[numpoints;myarray] x: movsum[numpoints; myarray]; mydivs: $[numpoints < #myarray; (1+!numpoints), numpoints _ (#myarray) # numpoints;(1+!#myarray)]; x%mydivs}')

from .kdataframe import kDataFrame



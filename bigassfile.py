import numpy
d = 3
n = 9000000
data = numpy.random.uniform(0, 1000,size=(n,d))
numpy.savetxt("input.txt", data, fmt='%.3f')

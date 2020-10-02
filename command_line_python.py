import sys
import numpy


action = sys.argv[1]
filenames = sys.argv[2:]

for filename in filenames:
    data = numpy.loadtxt(filename, delimiter=',')
    if action == '--mean':
        print(numpy.mean(data))
    
    if action == '--min':
        print(numpy.min(data))

    if action == '--printname':
        print(filename)

    else:
        print("command not recognised")
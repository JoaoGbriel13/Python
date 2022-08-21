import numpy
import random

matriz1 = numpy.random.randint(0,100,4).reshape(2,2)

matriz2 = numpy.random.randint(0,100,4).reshape(2,2)

print(matriz1)
print(matriz2)
print(numpy.multiply(matriz1,matriz2))
print(numpy.add(matriz1,matriz2))
import numpy.random as rand
import math


def uniform():
    return rand.uniform(0, 1)


def exp(mean):
    u = uniform()
    return - math.log(u)*mean


def bernoulli(mean):
    u = uniform()
    return int(u < mean)

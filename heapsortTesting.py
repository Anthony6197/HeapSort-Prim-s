"""
Contains some demo code for how you might go about testing heapsort (and
by extension the built-in sorting algorithm)
"""

import time
import random
import numpy as np
from heapSort import heapSort


# Set the random seed, so the same sequence of random values gets generated.
# This makes random results repeatable
random.seed(9159168)



def generateAndTime(arraySize):
    array = np.random.rand(arraySize)
    t1 = time.time()
    heapSort(array)
    t2 = time.time()
    # print(array)
    elapsed = t2 - t1
    return elapsed


def repeatForSize(size, reps):
    """generate and time the algorithm on data of the given
    size, reps number of times"""
    results = []
    for i in range(reps):
        res = generateAndTime(size)
        results.append(res)
    print("TEST  size:", size, "    reps:", reps)
    avg = sum(results) / len(results)
    print("min:", min(results), "    avg:", avg, "    max:", max(results))



def runTest(sizes, reps=10):
    for size in sizes:
        repeatForSize(size, reps)



runTest([1000, 2000, 3000, 4000, 5000])
runTest([10000, 20000, 30000, 40000, 50000])









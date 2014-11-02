import numpy as np
from random import random, randint, normalvariate, shuffle
from cost import cost
from allocation import generateRandomAllocation

def RandomSearch(maxiter, m=7, n=50):
    sCur = np.zeros([maxiter, m, n])
    sBest = np.zeros([maxiter, m, n])
    solution = np.zeros(maxiter)
    bestCost = 500.0

    for i in range(maxiter):
        sCur[i,:,:] = np.array(generateRandomAllocation())
        curCost = cost(sCur[i,:,:])

        if curCost < bestCost:
            sBest[i,:,:] = sCur[i,:,:]
            bestCost = curCost
        else:
            sBest[i,:,:] = sBest[i-1,:,:]

        solution[i] = bestCost

    return solution, sBest[maxiter - 1,:,:]

import numpy as np
from random import random, randint, normalvariate
from cost import cost

def DDS(s0, sMin, sMax, maxiter, r, pDecrease = 'exponential'):
    '''Returns a column vector of the best function value (for miminization problem)after each iteration and a row vector of the best solution found'''
    
    #Variable definitions:

    #s0 = initial solution; an n-dimensional vector where each dimension represents a decision variable
    #sMax = n-dimensional vector of the maximum value in the domain of each respective decision variable
    #sMin = n-dimensional vector of the minimum value in the domain of each respective decision variable
    #maxiter = total number of iterations to run

    #r = parameter between 0 and 1 that determines the standard deviation of the random Gaussian perturbation of each decision variable;
    #the standard deviation of each random Gaussian perturbation is equal to a fraction (r) of the total domain of that decision variable

    #pDecrease = string defining how the probability of perturbing each dimension varies with iteration number;
    #'linear' gives a linear decrease in probability with iterations, while the default is an exponential decrease

    #initialize all variables
    n = len(s0)
    sCur = np.zeros([maxiter, n])
    sBest = np.zeros([maxiter,n])
    solution = np.zeros(maxiter)
    sCur[0,:] = s0
    sBest[0,:] = s0
    bestCost = cost(sBest[0,:])
    solution[0] = bestCost
    sigma = []
    
    #determine the standard deviation of the random Gaussian perturbation for each dimension
    for i in range(n):
        sigma = sigma + [r*(sMax[i] - sMin[i])]

    #perform algorithm with a linear decrease in probability of perturbation with iterations
    if pDecrease != 'exponential':
        for i in range(maxiter-1):
            #determine the probability of perturbing each dimension
            p = 1 - (i+2)/maxiter
                
            #perturb dimensions probabilistically
            for j in range(n):
                if(random() < p):
                    sCur[i+1,j] = neighbor(sBest[i,j], sMax[j], sMin[j], sigma[j])
                else:
                    sCur[i+1,j] = sBest[i,j]

            #if no dimensions have been changed, choose one randomly to perturb
            if all(sCur[i+1,:] == sBest[i,:]):
                d = randint(0,n-1)
                sCur[i+1,d] = neighbor(sBest[i,d], sMax[d], sMin[d], sigma[d])

            #evaluate the cost of the new solution
            curCost = cost(sCur[i+1,:])

            #update the best cost and best solution if the new solution is better than the previous best
            if curCost < bestCost:
                sBest[i+1,:] = sCur[i+1,:]
                bestCost = curCost
            else:
                sBest[i+1,:] = sBest[i,:]

            #update the solution matrix
            solution[i+1] = bestCost
        
    #perform algorithm with an exponential decrease in probability of perturbation with iterations
    elif pDecrease == 'exponential':
        for i in range(maxiter-1):
            #determine the probability of perturbing each dimension
            p = 1 - np.log(i+2)/np.log(maxiter)
                
            #perturb dimensions probabilistically
            for j in range(n):
                if random() < p:
                    sCur[i+1,j] = neighbor(sBest[i,j], sMax[j], sMin[j], sigma[j])
                else:
                    sCur[i+1,j] = sBest[i,j]

            #if no dimensions have been changed, choose one randomly to perturb
            if all(sCur[i+1,:] == sBest[i,:]):
                d = randint(0,n-1)
                sCur[i+1,d] = neighbor(sBest[i,d], sMax[d], sMin[d], sigma[d])

            #evaluate the cost of the new solution
            curCost = cost(sCur[i+1,:])

            #update the best cost and best solution if the new solution is better than the previous best
            if curCost < bestCost:
                sBest[i+1,:] = sCur[i+1,:]
                bestCost = curCost
            else:
                sBest[i+1,:] = sBest[i,:]

            #update the solution matrix
            solution[i+1] = bestCost

    return solution, sBest[maxiter-1,:]

def neighbor(s, sMax, sMin, sigma):
    '''Returns a random Gaussian perturbation, with standard deviation sigma, of a scalar (s) on the domain [sMin, sMax].'''

    #perturb the input scalar
    s = s + sigma*normalvariate(0,1)

    #reflect the new value of the scalar over the boundary of its domain if the perturbation brings it outside
    if s < sMin:
        s = sMin + (sMin - s)
        if s > sMax:
            s = sMin
    
    elif s > sMax:
        s = sMax - (s - sMax)
        if s < sMin:
            s = sMax

    #determine the perturbed value
    neighbor = s

    return neighbor
